from retrieval.faiss_store import search_faiss
from retrieval.bm25 import search_bm25
from retrieval.tavily import TavilySearch

tavily = TavilySearch()

def retrieve_docs(query):
    docs1 = search_faiss(query)
    docs2 = search_bm25(query)

    combined_docs = docs1 + docs2

    # 🔥 Fallback to Tavily if weak retrieval
    if len(combined_docs) < 2:
        web_results = tavily.search(query)

        for w in web_results:
            combined_docs.append(type("Doc", (), {
                "page_content": w["content"],
                "metadata": {"source": w["source"]}
            }))

    return combined_docs