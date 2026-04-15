from rank_bm25 import BM25Okapi

bm25 = None
docs_store = []
corpus = []

def build_bm25(docs):
    global bm25, docs_store, corpus
    docs_store = docs
    corpus = [doc.page_content.split() for doc in docs]
    bm25 = BM25Okapi(corpus)

def search_bm25(query):
    if bm25 is None:
        return []
    tokens = query.split()
    scores = bm25.get_scores(tokens)
    top = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:3]
    return [docs_store[i] for i in top]