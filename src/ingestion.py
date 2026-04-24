import re
import json
from pathlib import Path

INPUT_DIR = Path(r"C:\rag-midtrans-docs\data\raw\docs")
OUTPUT_DIR = Path(r"C:\rag-midtrans-docs\data\chunks")

def split_metadata(text):
    metadata = {}
    if not text.startswith("---"):
        return "Teks ini tidak diawali oleh ---"
    end = text.find("---", 3)
    if end == -1:
        return "Akhir dari --- tidak ditemukan"
    metadata_block = text[3:end].strip()
    content = text[end + 3:].strip()
    for line in metadata_block.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            metadata[key.strip()] = value.strip().strip('"')
 
    return metadata, content

def chunk_method(text):
    return None

def run():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    md_files = list(INPUT_DIR.rglob("*.md"))
    print(f"Ditemukan {len(md_files)} file .md\n")

    for i, filepath in enumerate(md_files):
        text = filepath.read_text(encoding="utf-8")
        metadata, content = split_metadata(text)
        
        chunks = []
        chunks.append({
            "chunk_index": i,
            "text": content,
            "metadata": {
                **metadata,
                "chunk_index": i,
                "source_file": filepath.name
            }
        })
        output_path = OUTPUT_DIR / (filepath.stem + ".json")
        output_path.write_text(json.dumps(chunks, indent=2, ensure_ascii=False), encoding="utf-8")

if __name__ == "__main__":
    run()


        

