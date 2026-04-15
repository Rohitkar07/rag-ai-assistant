def route_query(query):
    q = query.lower()

    # 🔥 analytical queries
    if any(x in q for x in ["why", "compare", "difference", "benefit"]):
        return "analysis"

    # document queries
    if any(x in q for x in ["pdf", "document", "report"]):
        return "document"

    return "general"