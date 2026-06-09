# src/pipeline.py

from dotenv import load_dotenv
from pathlib import Path
from pinecone import Pinecone
import os

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

from src.retrieval.semantic_search import retrieve
from src.retrieval.reranker import rerank
from src.generation.generate_answer import init_gemini, build_prompt, generate


def init_clients() -> tuple:
    """
    Inisialisasi semua client yang dibutuhkan pipeline.
    Return (pc, model)
    Pinecone client di-init sekali dan dipakai oleh retrieve + rerank.
    """
    pc    = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    client = init_gemini()
    return pc, client


def run_pipeline(
    query: str,
    pc: Pinecone,
    client,
    retrieve_top_k: int = 20,
    rerank_top_n: int = 3,
) -> tuple[str, list[dict]]:
    """
    Full RAG pipeline:
      1. Retrieve top_k kandidat dari Pinecone (semantic search)
      2. Rerank kandidat, ambil top_n terbaik
      3. Build prompt dari top_n chunk
      4. Generate jawaban dengan Gemini

    Return:
      answer  : string jawaban dari LLM
      matches : list chunk hasil rerank (untuk ditampilkan sebagai sumber)
    """
    # Step 1 — Retrieve
    candidates = retrieve(pc, query, top_k=retrieve_top_k)
    if not candidates:
        return "Maaf, saya tidak menemukan informasi yang relevan di dokumentasi Xendit.", []

    # Step 2 — Rerank
    reranked = rerank(pc, query, candidates, top_n=rerank_top_n)
    if not reranked:
        return "Maaf, saya tidak menemukan informasi yang relevan di dokumentasi Xendit.", []

    # Step 3 — Build prompt
    prompt = build_prompt(query, reranked)

    # Step 4 — Generate
    answer = generate(client, prompt)

    return answer, reranked