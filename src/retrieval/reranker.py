# src/retrieval/reranker.py

from pinecone import Pinecone
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

def rerank(pc, query: str, matches: list, top_n: int = 5) -> list:
    documents = [
        {
            "id": match["id"],
            "text": match["metadata"].get("text", "")
        }
        for match in matches
    ]

    reranked = pc.inference.rerank(
        model="pinecone-rerank-v0",
        query=query,
        documents=documents,
        top_n=top_n,
        rank_fields=["text"],
        return_documents=True,
        parameters={"truncate": "END"}
    )

    id_to_match = {match["id"]: match for match in matches}
    results = []
    for item in reranked.data:
        m = id_to_match[item.document["id"]]
        results.append({
            "id": m["id"],
            "score": m["score"],
            "metadata": m["metadata"],
            "rerank_score": item.score
        })

    return results