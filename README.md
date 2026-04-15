# 🧠 RAG + Web AI Assistant

An advanced **Retrieval-Augmented Generation (RAG)** based AI assistant that can answer questions from uploaded documents and the web using LLMs.

---

## 🚀 Features

- 📄 Upload and query PDFs
- 🌐 Web search integration (Tavily)
- 🔍 Hybrid retrieval (FAISS + BM25)
- 🎯 Re-ranking using Cross-Encoder
- 🧠 Query-type routing (fact / analysis / definition)
- 🔄 Self-correcting pipeline (validation + retry)
- 💬 Context-aware answer generation
- 📊 Confidence score + source tracking

---

## 🏗️ Architecture

User Query
↓
Router (Query Type Detection)
↓
Retriever (FAISS + BM25)
↓
Re-ranker (Cross Encoder)
↓
Generator (LLM)
↓
Critic (Refinement)
↓
Validator (Self-check)
↓
Final Answer



---

## 🛠️ Tech Stack

- Python
- Streamlit
- HuggingFace Transformers
- Sentence Transformers
- FAISS
- BM25
- Tavily API

---

