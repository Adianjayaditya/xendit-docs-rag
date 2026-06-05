import json
import random

apidocs_chunks = []
with open("data/chunks/apidocs/apidocs_chunks.jsonl", encoding="utf-8") as f:
    for line in f:
        apidocs_chunks.append(json.loads(line))

docs_chunks = []
with open("data/chunks/docs/docs_chunks.jsonl", encoding="utf-8") as f:
    for line in f:
        docs_chunks.append(json.loads(line))

def sample_by_type(chunks, n_per_type=15):  # naikkan dari 3 → 15
    by_type = {}
    for c in chunks:
        t = c["chunk_type"]
        by_type.setdefault(t, []).append(c)
    
    result = []
    for t, items in by_type.items():
        result.extend(random.sample(items, min(n_per_type, len(items))))
    return result

sample = sample_by_type(apidocs_chunks, n_per_type=15) + sample_by_type(docs_chunks, n_per_type=15)

output = []
for c in sample:
    output.append({
        "source_file": c["source_file"],
        "chunk_type": c["chunk_type"],
        "section_heading": c.get("section_heading") or c.get("endpoint_path") or "",
        "title": c["title"],
        "text": c["text"][:800]  # naikkan dari 500 → 800 agar konteksnya cukup
    })

with open("chunk_sample.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Total sampel: {len(output)}")
print("Distribusi:")
from collections import Counter
dist = Counter(c["chunk_type"] for c in output)
for t, n in dist.items():
    print(f"  {t}: {n}")