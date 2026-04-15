import streamlit as st
from main import pipeline
from utils.loader import load_pdf
from utils.chunking import split_docs
from retrieval.faiss_store import build_faiss
from retrieval.bm25 import build_bm25

st.title("🧠 RAG + Web AI Assistant")

file = st.file_uploader("Upload PDF", type="pdf")

if file:
    with open("temp.pdf", "wb") as f:
        f.write(file.read())

    docs = load_pdf("temp.pdf")
    chunks = split_docs(docs)

    build_faiss(chunks)
    build_bm25(chunks)

    st.success("Document ready!")

query = st.text_input("Ask something:")

if query:
    ans, conf, sources = pipeline(query)

    st.write("### Answer")
    st.write(ans)
    st.write(f"Confidence: {conf:.2f}")

    if sources:
        st.write("### Sources")
        for s in sources:
            st.markdown(f"[{s}]({s})")