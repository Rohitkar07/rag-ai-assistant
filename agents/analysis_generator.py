from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_analysis_answer(query, docs):
    context = "\n".join([d.page_content for d in docs])[:800]

    prompt = f"""
Answer the question in bullet points.

Explain clearly.

Context:
{context}

Question:
{query}

Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(**inputs, max_new_tokens=150)

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer.strip()