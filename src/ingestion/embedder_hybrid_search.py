from pinecone import Pinecone 
from dotenv import load_dotenv
import os
import json
import hashlib
from pathlib import Path

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_HOST_HYBRID = os.getenv("INDEX_HOST_HYBRID")

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_HOST_HYBRID)

BASE_DIR = Path(__file__).parent.parent.parent
CHUNKS_FILE = BASE_DIR / "data" / "chunks" / "apidocs" / "apidocs_chunks.jsonl"

def generate_id(chunk):
    raw = f"{chunk['source_file']}::{chunk['chunk_index']}"
    return hashlib.md5(raw.encode()).hexdigest()

chunks = []
with open(CHUNKS_FILE, 'r', encoding='utf-8') as file:
    for line in file:
        chunks.append(json.loads(line))

BATCH_SIZE = 50
NAMESPACE = "_default_"

for i in range(0, len(chunks), BATCH_SIZE):
    batch = chunks[i:i+BATCH_SIZE]

    # Embed
    dense_embeddings = pc.inference.embed(
        model="llama-text-embed-v2",
        inputs=[chunk['text'] for chunk in batch],
        parameters={
            "input_type": "passage",
            "dimension": 1024
        }
    )

    sparse_embeddings = pc.inference.embed(
        model="pinecone-sparse-english-v0",
        inputs=[chunk['text'] for chunk in batch],
        parameters={
            "input_type": "passage", 
            "truncate": "END"
        }
    )

    vectors = []
    for chunk, de, se in zip(batch, dense_embeddings, sparse_embeddings):
        vectors.append({
            "id": generate_id(chunk),
            "values": de["values"],
            "sparse_values": {
                "indices": se["sparse_indices"],
                "values": se["sparse_values"]
            },
            "metadata": {
                "text": chunk["text"][:2000],
                "source_url": chunk["source_url"],
                "chunk_type": chunk["chunk_type"],
                "endpoint_path": chunk.get("endpoint_path") or "",
                "http_method": chunk.get("http_method") or "",
                "title": chunk["title"],
                "section": chunk.get("section") or "",
                "source_file": chunk["source_file"],
                "status_code": chunk.get("status_code") or "",
                "nested_field": chunk.get("nested_field") or "",
            }
        })
    
    index.upsert(namespace=NAMESPACE, vectors=vectors)