# src/pipeline.py

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pathlib import Path
from pinecone import Pinecone
import os

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

from src.retrieval.semantic_search import retrieve
from src.retrieval.reranker import rerank
from src.generation.generate_answer import build_prompt, generate
from src.generation.is_cache_sufficient import build_prompt_decision, cache_sufficient_decision


def init_clients() -> tuple:
    """
    Inisialisasi semua client yang dibutuhkan pipeline.
    Return (pc, model)
    Pinecone client di-init sekali dan dipakai oleh retrieve + rerank.
    """
    pc    = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    return pc, client


def run_pipeline(
    query: str,
    pc: Pinecone,
    client,
    cached_chunks: list,
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
    if len(cached_chunks) == 0:
        candidates = retrieve(pc, query, top_k=retrieve_top_k)
        if not candidates:
            return "Maaf, saya tidak menemukan informasi yang relevan di dokumentasi Xendit.", []
        reranked = rerank(pc, query, candidates, top_n=rerank_top_n)
        prompt = build_prompt(query, reranked)
        answer = generate(client, prompt)
        return answer, reranked
    else:
        prompt_decision = build_prompt_decision(query, cached_chunks)
        is_cache_sufficient = cache_sufficient_decision(client, prompt_decision)
        if is_cache_sufficient == 'NO':
            candidates = retrieve(pc, query, top_k=retrieve_top_k)
            if not candidates:
                return "Maaf, saya tidak menemukan informasi yang relevan di dokumentasi Xendit.", []
            reranked = rerank(pc, query, candidates, top_n=rerank_top_n)
            prompt = build_prompt(query, reranked)
            answer = generate(client, prompt)
            return answer, reranked
        else:
            prompt = build_prompt(query, cached_chunks)
            answer = generate(client, prompt)
            return answer, cached_chunks


