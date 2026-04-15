from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings()
db = None

def build_faiss(docs):
    global db
    db = FAISS.from_documents(docs, embedding)

def search_faiss(query):
    if db is None:
        return []
    return db.similarity_search(query, k=3)