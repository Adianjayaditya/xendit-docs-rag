from pinecone import Pinecone
import os

def retrieve(query, top_k=5):
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index = pc.Index(os.getenv("INDEX_HOST"))
    embedding = pc.inference.embed(
        model="llama-text-embed-v2",
        inputs=[
            query
        ],
        parameters={
            "input_type": "query",
            "dimension": 1024
        }
    )

    results = index.query(
        namespace="_default_",
        vector=embedding[0]["values"],
        top_k=top_k,
        include_metadata=True
    )
    return results.get("matches", [])