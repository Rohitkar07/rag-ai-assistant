from agents.retriever import retrieve_docs
from agents.generator import generate_answer
from agents.critic import refine_answer
from agents.router import route_query
from agents.analysis_generator import generate_analysis_answer
from agents.validator import validate_answer
from retrieval.tavily import TavilySearch
from memory.chat_memory import ChatMemory

memory = ChatMemory()
tavily = TavilySearch()

def pipeline(query):
    intent = route_query(query)

    docs = []
    sources = []

    # 🔹 STEP 1: GET DOCS
    if intent == "general":
        web_results = tavily.search(query)
        for w in web_results:
            docs.append(type("Doc", (), {
                "page_content": w["content"],
                "metadata": {"source": w["source"]}
            }))
    else:
        docs = retrieve_docs(query)

    # collect sources
    for d in docs:
        if hasattr(d, "metadata") and "source" in d.metadata:
            sources.append(d.metadata["source"])

    # 🔹 STEP 2: GENERATE ANSWER
    if intent == "analysis":
        answer = generate_analysis_answer(query, docs)
    else:
        answer, _ = generate_answer(query, docs)

    # 🔹 STEP 3: REFINE
    final = refine_answer(answer, docs)

    # 🔹 STEP 4: VALIDATE 🔥
    if not validate_answer(query, final):
        # 🔁 fallback: try again with smaller context
        context_docs = docs[:2]

        answer, _ = generate_answer(query, context_docs)
        final = refine_answer(answer, context_docs)

        # 🔁 final fallback
        if not validate_answer(query, final):
            final = "Sorry, I couldn't find a reliable answer. Please try rephrasing."

    # 🔹 STEP 5: CONFIDENCE
    confidence = min(1.0, 0.5 + 0.1 * len(docs))

    memory.store(query, final)

    return final, confidence, list(set(sources))