"""
xendit_chunker.py
-----------------
Chunker untuk dokumentasi Xendit hasil scraping (.md files).
Menghasilkan chunk dengan contextual header injection dan metadata lengkap.

Output: List of dicts, siap di-embed atau disimpan ke vector store.
"""

import re
import json
import yaml
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Optional

@dataclass
class Chunk:
    text: str
    source_url: str
    product: str
    section: str                 
    title: str
    endpoint_path: Optional[str] 
    http_method: Optional[str]
    chunk_type: str              
    chunk_index: int         
    source_file: str

    parent_chunk_type: Optional[str] = None
    status_code: Optional[str] = None   
    nested_field: Optional[str] = None  

    def to_dict(self) -> dict:
        return asdict(self)

def parse_frontmatter(content: str) -> tuple[dict, str]:
    """
    Pisahkan YAML frontmatter dari body markdown.
    Return (metadata_dict, body_string).
    """
    if not content.startswith("---"):
        return {}, content

    end = content.find("\n---", 3)
    if end == -1:
        return {}, content

    fm_text = content[3:end].strip()
    body = content[end + 4:].strip()

    try:
        meta = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        meta = {}

    return meta, body

def detect_section(meta: dict, filepath: Path) -> str:
    """Deteksi apakah file ini apidocs atau docs biasa."""
    if meta.get("section"):
        return meta["section"]
    url = meta.get("url", "")
    if "apidocs" in url or "apidocs" in str(filepath):
        return "apidocs"
    return "docs"

class ApiDocsChunker:
    """
    Memecah file apidocs .md menjadi chunk-chunk:
    1. overview      — method, path, deskripsi singkat
    2. request_params — header/path/body params
    3. response_200  — response sukses (+ sub-chunks jika ada nested object panjang)
    4. response_error — response 4xx / 5xx
    """
    NESTED_SPLIT_THRESHOLD = 12

    def __init__(self, meta: dict, body: str, filepath: Path):
        self.meta = meta
        self.body = body
        self.filepath = filepath
        self.title = meta.get("title", filepath.stem)
        self.source_url = meta.get("url", "")
        self.product = meta.get("product", "xendit")
        self.section = detect_section(meta, filepath)

    def _extract_endpoint(self) -> tuple[str, str]:
        """Ambil HTTP method dan path dari baris ## Endpoint atau backtick."""
        m = re.search(r"`(GET|POST|PUT|PATCH|DELETE|HEAD)\s+(/[^\`]+)`", self.body)
        if m:
            return m.group(1), m.group(2).strip()
        return "", ""

    def _base_meta(self, chunk_type: str, chunk_index: int, method: str, path: str) -> dict:
        return dict(
            source_url=self.source_url,
            product=self.product,
            section=self.section,
            title=self.title,
            endpoint_path=path or None,
            http_method=method or None,
            chunk_type=chunk_type,
            chunk_index=chunk_index,
            source_file=self.filepath.name,
        )

    def chunk(self) -> list[Chunk]:
        chunks: list[Chunk] = []
        method, path = self._extract_endpoint()
        ctx_header = f"[{self.title}] {method} {path}\n" if path else f"[{self.title}]\n"
        sections = self._split_into_sections(self.body)

        overview_lines = []
        param_lines = []
        response_sections: dict[str, list[str]] = {}

        PARAM_KEYWORDS = [
            "parameter", "param",
            "header param", "path param", "body param", "query param",
            "query parameter", "header parameter", "path parameter", "body parameter",
            "request body", "request param",
        ]
        SECURITY_KEYWORDS = ["security", "authentication", "authorization", "auth"]
        OVERVIEW_KEYWORDS = ["endpoint", "overview", "description", "introduction"]

        for sec_title, sec_body in sections:
            tl = sec_title.lower().strip()

            if re.match(r"^2\d\d", sec_title.strip()):
                response_sections.setdefault("200", []).append(sec_body.strip())
                continue

            if re.match(r"^[45]\d\d|^4xx|^5xx", sec_title.strip(), re.IGNORECASE):
                response_sections.setdefault("error", []).append(sec_body.strip())
                continue

            if any(kw in tl for kw in SECURITY_KEYWORDS):
                param_lines.append(f"### {sec_title}\n{sec_body.strip()}")
                continue
            if any(kw in tl for kw in PARAM_KEYWORDS):
                param_lines.append(f"### {sec_title}\n{sec_body.strip()}")
                continue

            if any(kw in tl for kw in OVERVIEW_KEYWORDS):
                overview_lines.append(sec_body.strip())

        intro = self._extract_intro(self.body)

        overview_text = f"{ctx_header}Endpoint: {method} {path}\n\n"
        if intro:
            overview_text += intro.strip() + "\n"
        for ol in overview_lines:
            overview_text += ol + "\n"

        chunks.append(Chunk(
            text=overview_text.strip(),
            **self._base_meta("overview", 0, method, path),
        ))

        if param_lines:
            param_text = f"{ctx_header}Request parameters untuk endpoint ini:\n\n"
            param_text += "\n\n".join(param_lines)
            chunks.append(Chunk(
                text=param_text.strip(),
                **self._base_meta("request_params", 1, method, path),
            ))

        idx = 2
        for code, bodies in response_sections.items():
            full_body = "\n\n".join(bodies)
            label = "200 OK" if code == "200" else "Error (4xx/5xx)"
            status_code = "200" if code == "200" else "4xx_5xx"
            chunk_type = "response_200" if code == "200" else "response_error"

            nested = self._extract_nested_objects(full_body)

            if nested:
                trimmed_body = self._remove_nested_objects(full_body, nested)
                main_text = (
                    f"{ctx_header}Response {label} — {self.title}\n\n"
                    + trimmed_body.strip()
                )
                main_meta = self._base_meta(chunk_type, idx, method, path)
                main_meta["status_code"] = status_code
                chunks.append(Chunk(text=main_text.strip(), **main_meta))
                idx += 1

                for nested_name, nested_body in nested.items():
                    nested_text = (
                        f"{ctx_header}Response {label} — nested object `{nested_name}` — {self.title}\n\n"
                        + f"Object `{nested_name}` adalah bagian dari response {method} {path}:\n\n"
                        + nested_body.strip()
                    )
                    nested_meta = self._base_meta("response_nested", idx, method, path)
                    nested_meta["status_code"] = status_code
                    nested_meta["parent_chunk_type"] = chunk_type
                    nested_meta["nested_field"] = nested_name
                    chunks.append(Chunk(text=nested_text.strip(), **nested_meta))
                    idx += 1

            else:
                resp_text = (
                    f"{ctx_header}Response {label} — {self.title}\n\n"
                    + full_body.strip()
                )
                resp_meta = self._base_meta(chunk_type, idx, method, path)
                resp_meta["status_code"] = status_code
                chunks.append(Chunk(text=resp_text.strip(), **resp_meta))
                idx += 1

        return chunks

    def _extract_intro(self, body: str) -> str:
        """Ambil teks sebelum heading pertama (##)."""
        m = re.split(r"\n#{2,}\s", body, maxsplit=1)
        if len(m) > 1:
            return m[0].strip()
        return ""

    def _split_into_sections(self, body: str) -> list[tuple[str, str]]:
        """
        Bagi body menjadi list (heading_title, content).
        Heading level ## dan ###.
        """
        parts = re.split(r"\n(#{2,3})\s+(.+)", body)
        sections = []
        i = 1
        while i < len(parts) - 2:
            title = parts[i + 1].strip()
            content = parts[i + 2] if i + 2 < len(parts) else ""
            sections.append((title, content))
            i += 3
        return sections

    def _extract_nested_objects(self, response_body: str) -> dict[str, str]:
        """
        Temukan nested object yang panjang (> threshold baris).
        Heuristik: cari pola "- **field** (object ...)" diikuti sub-fields.
        Return dict {field_name: content_block}.
        """
        nested = {}

        pattern = re.compile(
            r"- \*\*(\w+)\*\*\s*\([^)]*(?:object|array)[^)]*\)[^:]*:(.*?)(?=\n- \*\*|\Z)",
            re.DOTALL
        )

        for m in pattern.finditer(response_body):
            field_name = m.group(1)
            block = m.group(2).strip()
            lines = [l for l in block.splitlines() if l.strip()]
            if len(lines) >= self.NESTED_SPLIT_THRESHOLD:
                nested[field_name] = block

        return nested

    def _remove_nested_objects(self, response_body: str, nested: dict) -> str:
        """Hapus blok nested yang sudah dijadikan sub-chunk dari body utama."""
        result = response_body
        for field_name in nested:
            pattern = re.compile(
                rf"- \*\*{re.escape(field_name)}\*\*\s*\([^)]*(?:object|array)[^)]*\)[^:]*:.*?(?=\n- \*\*|\Z)",
                re.DOTALL
            )
            result = pattern.sub(
                f"- **{field_name}**: *(lihat chunk terpisah untuk detail schema)*",
                result
            )
        return result

class DocsChunker:
    """
    Untuk file docs non-API: chunk per heading ##.
    Setiap chunk mendapat 1-2 kalimat terakhir dari chunk sebelumnya
    sebagai context overlap.
    """

    OVERLAP_SENTENCES = 2

    def __init__(self, meta: dict, body: str, filepath: Path):
        self.meta = meta
        self.body = body
        self.filepath = filepath
        self.title = meta.get("title", filepath.stem)
        self.source_url = meta.get("url", "")
        self.product = meta.get("product", "xendit")
        self.section = detect_section(meta, filepath)

    def chunk(self) -> list[Chunk]:
        chunks: list[Chunk] = []

        parts = re.split(r"\n(#{2})\s+(.+)", self.body)

        intro = parts[0].strip()
        sections = []
        i = 1
        while i < len(parts) - 2:
            heading = parts[i + 1].strip()
            content = parts[i + 2].strip() if i + 2 < len(parts) else ""
            sections.append((heading, content))
            i += 3

        if len(intro) > 100:
            sections.insert(0, (self.title, intro))

        overlap_tail = ""
        for idx, (heading, content) in enumerate(sections):
            ctx_header = f"[{self.title}] — {heading}\n"
            text = ctx_header + overlap_tail + content

            chunks.append(Chunk(
                text=text.strip(),
                source_url=self.source_url,
                product=self.product,
                section=self.section,
                title=self.title,
                endpoint_path=None,
                http_method=None,
                chunk_type="docs_section",
                chunk_index=idx,
                source_file=self.filepath.name,
            ))

            sentences = re.split(r"(?<=[.!?])\s+", content.strip())
            tail_sentences = sentences[-self.OVERLAP_SENTENCES:] if len(sentences) >= self.OVERLAP_SENTENCES else sentences
            overlap_tail = " ".join(tail_sentences) + "\n\n" if tail_sentences else ""

        return chunks

def chunk_file(filepath: Path) -> list[Chunk]:
    """Proses satu file .md dan return list Chunk."""
    content = filepath.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(content)
    section = detect_section(meta, filepath)

    if section == "apidocs":
        return ApiDocsChunker(meta, body, filepath).chunk()
    else:
        return DocsChunker(meta, body, filepath).chunk()


def chunk_directory(docs_dir: Path, output_file: Optional[Path] = None) -> list[dict]:
    """
    Proses semua file .md dalam direktori (rekursif).
    Return list of chunk dicts. Opsional simpan ke JSONL.
    """
    all_chunks = []
    md_files = sorted(docs_dir.rglob("*.md"))

    print(f"Ditemukan {len(md_files)} file .md")

    for fp in md_files:
        try:
            chunks = chunk_file(fp)
            all_chunks.extend(chunks)
            print(f"  ✓ {fp.name}: {len(chunks)} chunks")
        except Exception as e:
            print(f"  ✗ {fp.name}: ERROR — {e}")

    print(f"\nTotal: {len(all_chunks)} chunks dari {len(md_files)} file")

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            for chunk in all_chunks:
                f.write(json.dumps(chunk.to_dict() if isinstance(chunk, Chunk) else chunk, ensure_ascii=False) + "\n")
        print(f"Tersimpan ke: {output_file}")

    return [c.to_dict() if isinstance(c, Chunk) else c for c in all_chunks]


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python xendit_chunker.py path/to/file.md [output.jsonl]")
        print("  python xendit_chunker.py path/to/docs_dir/ [output.jsonl]")
        sys.exit(1)

    target = Path(sys.argv[1])

    if len(sys.argv) > 2:
        output_file = Path(sys.argv[2])
    elif target.is_dir():
        output_file = target.parent / "chunks.jsonl"
    else:
        output_file = target.parent / (target.stem + "_chunks.jsonl")

    if target.is_dir():
        chunk_directory(target, output_file=output_file)
    else:
        chunks = chunk_file(target)
        with open(output_file, "w", encoding="utf-8") as f:
            for c in chunks:
                f.write(json.dumps(c.to_dict(), ensure_ascii=False) + "\n")

        print(f"\nTotal: {len(chunks)} chunks")
        for c in chunks:
            d = c.to_dict()
            print(f"  [{d['chunk_index']}] {d['chunk_type']}"
                  + (f" | status: {d['status_code']}" if d.get("status_code") else "")
                  + (f" | nested: {d['nested_field']}" if d.get("nested_field") else ""))
        print(f"\nTersimpan ke: {output_file.resolve()}")