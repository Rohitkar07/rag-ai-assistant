def validate_answer(query, answer):
    # ❌ bad answers
    if not answer or len(answer.strip()) < 5:
        return False

    # ❌ generic phrases
    bad_phrases = [
        "i don't know",
        "not sure",
        "based on context",
        "area of search"
    ]

    if any(p in answer.lower() for p in bad_phrases):
        return False

    return True