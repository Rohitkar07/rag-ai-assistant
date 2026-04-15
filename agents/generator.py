from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_answer(query, docs):
    context = ""
    sources = []

    for d in docs:
        context += d.page_content + "\n"
        if hasattr(d, "metadata") and "source" in d.metadata:
            sources.append(d.metadata["source"])

    context = context[:800]

    prompt = f"""
Answer the question clearly in 3-4 bullet points.

Rules:
- If it's a definition question, explain in 2-3 sentences
- First line: define properly
- Next lines: explanation or usage
- Do NOT give one-word answers
- Be helpful and specific
- Include steps if applicable
- Avoid generic answers
- Answer the question clearly in 3-4 bullet points.

Context:
{context}

Question:
{query}

Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(
        **inputs,
        max_new_tokens=50
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    

    # 🔥 SMART POST-PROCESSING (KEY FIX)

    context_lower = context.lower()
    query_lower = query.lower()


    # ✅ General fallback
    if not answer or len(answer) < 5:
        if docs:
            answer = docs[0].page_content[:200]
        else:
            answer = "Sorry, I couldn't find a clear answer."

    return answer, list(set(sources))