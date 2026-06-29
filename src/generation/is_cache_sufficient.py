# src/generation/generate_answer.py

from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

SYSTEM_PROMPT = """Kamu adalah asisten dokumentasi Xendit yang membantu developer memahami produk dan API Xendit.
Tugas anda adalah membuat keputusan untuk menentukan apakah informasi yang diberikan kepada anda apakah dapat menjawab pertanyaan dari user.
Informasi yang anda terima ini berupa retrieved chunks yang di cached di suatu system RAG. Anda hanya dapat menentukan keputusan berdasarkan dari informasi yang diberikan, tidak informasi umum di luar dari informasi yang diberikan kepada anda. 
Jika anda tidak dapat menjawab pertanyaan berdasarkan informasi tersebut, maka lakukan output NO saja. Tetapi, jika anda bisa menjawab pertanyaan tersebut dengan informasi yang diberikan, lakukan output YES saja."""


def build_prompt_decision(query: str, cached_chunks: list[dict]) -> str:
    context_parts = []
    for i, match in enumerate(cached_chunks, 1):
        meta  = match.get("metadata", {})
        title = meta.get("title", "")
        chunk = meta.get("text", "")
        context_parts.append(f"[{i}] {title}\n{chunk}")

    context = "\n\n---\n\n".join(context_parts)

    return f"""{SYSTEM_PROMPT}

Konteks dokumentasi:
{context}

Pertanyaan: {query}

Jawaban:"""


def cache_sufficient_decision(client: genai.Client, prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text