from pinecone import Pinecone
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

def hybrid_score_norm(dense, sparse, alpha: float):
    if alpha < 0 or alpha > 1:
        raise ValueError("Alpha must be between 0 and 1")
    scaled_sparse = {
        "indices": sparse["indices"],
        "values": [v * (1 - alpha) for v in sparse["values"]]
    }
    scaled_dense = [v * alpha for v in dense]
    return scaled_dense, scaled_sparse

def retrieve(query, top_k=5, alpha=0.75):
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index = pc.Index(os.getenv("INDEX_HOST_HYBRID"))
    dense_query_embedding = pc.inference.embed(
        model="llama-text-embed-v2",
        inputs=[
            query
        ],
        parameters={
            "input_type": "query",
            "truncate": "END"
        }
    )

    sparse_query_embedding = pc.inference.embed(
        model="pinecone-sparse-english-v0",
        inputs=[
            query
        ],
        parameters={
            "input_type": "query",
            "truncate": "END"
        }
    )

    for d, s in zip(dense_query_embedding, sparse_query_embedding):
        hdense, hsparse = hybrid_score_norm(
            dense=d["values"],
            sparse={"indices": s["sparse_indices"], "values": s["sparse_values"]},
            alpha=alpha
        )
        query_response = index.query(
            namespace="_default_",
            top_k=top_k,
            vector=hdense,
            sparse_vector=hsparse,
            include_metadata=True
        )
    return query_response.get("matches", [])