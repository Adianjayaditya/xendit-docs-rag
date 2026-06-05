import re
import json
import yaml
import hashlib
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class DocsChunk:
    text: str

    source_url: str
    product: str
    section: str
    title: str
    page_slug: str
    breadcrumbs: list
    chunk_type: str
    section_heading: Optional[str]
    chunk_index: int
    source_file: str

    def to_dict(self) -> dict:
        return asdict(self)

def parse_frontmatter(content: str) -> tuple[dict, str]:
    if not content.startswith("---"):
        return {}, content
    end = content.find("\n---", 3)
    if end == -1:
        return {}, content
    fm_text = content[3:end].strip()
    body    = content[end + 4:].strip()
    try:
        meta = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, body


def clean_text(text: str) -> str:
    """
    Hapus elemen yang tidak berguna untuk embedding:
    - Image tags (semua format: ![alt](url), ![alt](url "title"), ![](url))
    - Sisa URL CDN yang tertinggal
    - Baris yang hanya berisi artefak gambar
    - Link eksternal → pertahankan teks saja
    - Link internal → pertahankan teks saja
    - Whitespace berlebih
    """
    text = re.sub(r'!\[.*?\]\([^)]+\)', '', text)
    text = re.sub(r'https://cdn\.document360\.io\S+', '', text)
    text = re.sub(r'^\s*\.(png|jpg|jpeg|webp|gif)\S*.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'\[([^\]]+)\]\(https?://[^)]+\)', r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\(/[^)]+\)', r'\1', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def split_by_h2(body: str) -> tuple[str, list[tuple[str, str]]]:
    """
    Pisahkan body menjadi:
    - pre_content : teks sebelum ## pertama (bisa berisi #, ###, prose)
    - sections    : list of (heading_title, content)

    Hanya split di tepat ## (dua tanda pagar), bukan # atau ###.
    """
    pattern = re.compile(r'\n(## )(.+)', )

    parts = pattern.split(body)
    pre_content = parts[0].strip()
    sections = []

    i = 1
    while i < len(parts) - 2:
        heading = parts[i + 1].strip()
        content = parts[i + 2].strip()
        sections.append((heading, content))
        i += 3

    return pre_content, sections


def extract_slug(meta: dict, filepath: Path) -> str:
    url = meta.get("url", "")
    return url.rstrip("/").split("/")[-1] if url else filepath.stem

class DocsChunker:

    def __init__(self, meta: dict, body: str, filepath: Path):
        self.meta       = meta
        self.body       = body
        self.filepath   = filepath
        self.title      = meta.get("title", filepath.stem)
        self.source_url = meta.get("url", "")
        self.product    = meta.get("product", "xendit")
        self.breadcrumbs = meta.get("breadcrumbs", [])
        self.page_slug  = extract_slug(meta, filepath)

    def _context_header(self, section_heading: Optional[str] = None) -> str:
        """
        Format: [Page Title — page-slug]
                Section: <heading>   ← hanya jika ada heading
        """
        header = f"[{self.title} — {self.page_slug}]\n"
        if section_heading:
            header += f"Section: {section_heading}\n"
        return header

    def _base_meta(self, chunk_type: str, idx: int,
                   section_heading: Optional[str] = None) -> dict:
        return dict(
            source_url=self.source_url,
            product=self.product,
            section="docs",
            title=self.title,
            page_slug=self.page_slug,
            breadcrumbs=self.breadcrumbs,
            chunk_type=chunk_type,
            section_heading=section_heading,
            chunk_index=idx,
            source_file=self.filepath.name,
        )

    def chunk(self) -> list[DocsChunk]:
        chunks: list[DocsChunk] = []
        body = clean_text(self.body)

        pre_content, sections = split_by_h2(body)

        if not sections:
            text = self._context_header() + "\n" + pre_content
            chunks.append(DocsChunk(
                text=text.strip(),
                **self._base_meta("full_page", 0),
            ))
            return chunks

        first_heading, first_content = sections[0]

        first_text = self._context_header(first_heading) + "\n"
        if pre_content:
            first_text += pre_content + "\n\n"
        first_text += first_content

        chunks.append(DocsChunk(
            text=first_text.strip(),
            **self._base_meta("section", 0, section_heading=first_heading),
        ))

        for idx, (heading, content) in enumerate(sections[1:], start=1):
            text = self._context_header(heading) + "\n" + content
            chunks.append(DocsChunk(
                text=text.strip(),
                **self._base_meta("section", idx, section_heading=heading),
            ))

        return chunks


def generate_id(chunk: dict) -> str:
    raw = f"{chunk['source_file']}::{chunk['chunk_index']}"
    return hashlib.md5(raw.encode()).hexdigest()

def chunk_file(filepath: Path) -> list[DocsChunk]:
    content = filepath.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(content)
    return DocsChunker(meta, body, filepath).chunk()


def chunk_directory(docs_dir: Path,
                    output_file: Optional[Path] = None) -> list[dict]:
    all_chunks = []
    md_files   = sorted(docs_dir.rglob("*.md"))
    print(f"Ditemukan {len(md_files)} file .md")

    for fp in md_files:
        try:
            chunks = chunk_file(fp)
            all_chunks.extend(chunks)
            print(f"  ✓ {fp.name}: {len(chunks)} chunks")
        except Exception as e:
            print(f"  ✗ {fp.name}: ERROR — {e}")

    print(f"\nTotal: {len(all_chunks)} chunks dari {len(md_files)} file")
    result = [c.to_dict() for c in all_chunks]

    if output_file:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            for chunk in result:
                f.write(json.dumps(chunk, ensure_ascii=False) + "\n")
        print(f"Tersimpan ke: {output_file.resolve()}")

    return result


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python docs_chunker.py path/to/file.md [output.jsonl]")
        print("  python docs_chunker.py path/to/docs_dir/ [output.jsonl]")
        sys.exit(1)

    target = Path(sys.argv[1])

    if len(sys.argv) > 2:
        output_file = Path(sys.argv[2])
    elif target.is_dir():
        output_file = target.parent / "docs_chunks.jsonl"
    else:
        output_file = target.parent / (target.stem + "_chunks.jsonl")

    if target.is_dir():
        chunk_directory(target, output_file=output_file)
    else:
        chunks = chunk_file(target)
        result = [c.to_dict() for c in chunks]

        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            for chunk in result:
                f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

        print(f"\nTotal: {len(chunks)} chunks")
        for c in chunks:
            d = c.to_dict()
            print(f"  [{d['chunk_index']}] {d['chunk_type']:12}"
                  + (f" | ## {d['section_heading']}" if d.get('section_heading') else ""))
        print(f"\nTersimpan ke: {output_file.resolve()}")