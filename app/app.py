import streamlit as st
from pinecone import Pinecone
import google.generativeai as genai
from dotenv import load_dotenv
import os
import sys

load_dotenv()

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.retrieval import init_pinecone, retrieve

@st.cache_resource
def init_clients():
    pc, index = init_pinecone()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash")
    return pc, index, model

pc, index, model = init_clients()

def build_prompt(query: str, matches: list[dict]) -> str:
    context_parts = []
    for i, match in enumerate(matches, 1):
        meta  = match.get("metadata", {})
        title = meta.get("title", "")
        chunk = meta.get("text", meta.get("content", ""))
        context_parts.append(f"[{i}] {title}\n{chunk}")

    context = "\n\n---\n\n".join(context_parts)

    return f"""Kamu adalah asisten dokumentasi Xendit yang membantu developer memahami produk dan API Xendit.
Jawab pertanyaan berdasarkan konteks dokumentasi yang diberikan.
Jika jawabannya tidak ada di konteks, katakan bahwa kamu tidak menemukan informasi tersebut di dokumentasi.
Jawab dalam bahasa yang sama dengan pertanyaan user (Indonesia atau Inggris).

Konteks dokumentasi:
{context}

Pertanyaan: {query}

Jawaban:"""

def generate(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text


def rag_answer(query):
    matches = retrieve(pc, index, query)
    if not matches:
        return "Maaf, saya tidak menemukan informasi yang relevan di dokumentasi Xendit.", []
    prompt = build_prompt(query, matches)
    answer = generate(prompt)
    return answer, matches


# Streamlit
st.set_page_config(
    page_title="Xendit Docs Assistant",
    page_icon="💳",
    layout="centered"
)

st.title("💳 Xendit Docs Assistant")
st.caption("Tanyakan apapun tentang dokumentasi Xendit — API, integrasi, dan konsep produk.")

# Init
if "messages" not in st.session_state:
    st.session_state.messages = []

if "sources" not in st.session_state:
    st.session_state.sources = {}

for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "assistant" and i in st.session_state.sources:
            sources = st.session_state.sources[i]
            if sources:
                with st.expander("📄 Sumber dokumentasi", expanded=False):
                    for j, match in enumerate(sources, 1):
                        meta  = match.get("metadata", {})
                        title = meta.get("title", "Unknown")
                        url   = meta.get("source_url", "")
                        ctype = meta.get("chunk_type", "")
                        score = match.get("score", 0)
                        st.markdown(
                            f"**{j}. {title}** `{ctype}` — score: `{score:.3f}`"
                            + (f"\n\n{url}" if url else "")
                        )

if prompt := st.chat_input("Tanya tentang Xendit..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Mencari di dokumentasi..."):
            answer, matches = rag_answer(prompt)
        st.markdown(answer)

        if matches:
            with st.expander("📄 Sumber dokumentasi", expanded=False):
                for j, match in enumerate(matches, 1):
                    meta  = match.get("metadata", {})
                    title = meta.get("title", "Unknown")
                    url   = meta.get("source_url", "")
                    ctype = meta.get("chunk_type", "")
                    score = match.get("score", 0)
                    st.markdown(
                        f"**{j}. {title}** `{ctype}` — score: `{score:.3f}`"
                        + (f"\n\n{url}" if url else "")
                    )

    msg_index = len(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.session_state.sources[msg_index] = matches