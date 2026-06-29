# app/app.py

import streamlit as st
import os
import sys

# sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.pipeline import init_clients, run_pipeline


@st.cache_resource
def load_clients():
    return init_clients()

pc, client = load_clients()


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Xendit Docs Assistant",
    page_icon="💳",
    layout="centered"
)

st.title("💳 Xendit Docs Assistant")
st.caption("Tanyakan apapun tentang dokumentasi Xendit — API, integrasi, dan konsep produk.")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "sources" not in st.session_state:
    st.session_state.sources = {}

if "cached_chunks" not in st.session_state:
    st.session_state.cached_chunks = []

# Tampilkan chat history
for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

        if msg["role"] == "assistant" and i in st.session_state.sources:
            sources = st.session_state.sources[i]
            if sources:
                with st.expander("📄 Sumber dokumentasi", expanded=False):
                    for j, match in enumerate(sources, 1):
                        meta         = match.get("metadata", {})
                        title        = meta.get("title", "Unknown")
                        url          = meta.get("source_url", "")
                        chunk_type   = meta.get("chunk_type", "")
                        rerank_score = match.get("rerank_score", match.get("score", 0))
                        st.markdown(
                            f"**{j}. {title}** `{chunk_type}` — rerank score: `{rerank_score:.3f}`"
                            + (f"\n\n{url}" if url else "")
                        )

# Chat input
if prompt := st.chat_input("Tanya tentang Xendit..."):

    # Tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate jawaban
    with st.chat_message("assistant"):
        with st.spinner("Mencari di dokumentasi..."):
            answer, matches = run_pipeline(
                query=prompt,
                pc=pc,
                client=client,
                cached_chunks=st.session_state.cached_chunks,
                retrieve_top_k=20,
                rerank_top_n=3,
            )
            if matches:
                st.session_state.cached_chunks = matches
        st.markdown(answer)

        if matches:
            with st.expander("📄 Sumber dokumentasi", expanded=False):
                for j, match in enumerate(matches, 1):
                    meta         = match.get("metadata", {})
                    title        = meta.get("title", "Unknown")
                    url          = meta.get("source_url", "")
                    chunk_type   = meta.get("chunk_type", "")
                    rerank_score = match.get("rerank_score", match.get("score", 0))
                    st.markdown(
                        f"**{j}. {title}** `{chunk_type}` — rerank score: `{rerank_score:.3f}`"
                        + (f"\n\n{url}" if url else "")
                    )

    # Simpan ke history
    msg_index = len(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.session_state.sources[msg_index] = matches