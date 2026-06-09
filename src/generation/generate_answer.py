# src/generation/generate_answer.py

from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

SYSTEM_PROMPT = """Kamu adalah asisten dokumentasi Xendit yang membantu developer memahami produk dan API Xendit.
Jawab pertanyaan berdasarkan konteks dokumentasi yang diberikan.
Jika jawabannya tidak ada di konteks, katakan bahwa kamu tidak menemukan informasi tersebut di dokumentasi.
Jawab dalam bahasa yang sama dengan pertanyaan user (Indonesia atau Inggris)."""


def init_gemini() -> genai.Client:
    return genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def build_prompt(query: str, matches: list[dict]) -> str:
    context_parts = []
    for i, match in enumerate(matches, 1):
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


def generate(client: genai.Client, prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text