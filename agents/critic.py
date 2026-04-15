from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def refine_answer(answer, docs):
    context = " ".join([d.page_content for d in docs])[:1000]

    prompt = f"""
Refine the answer in 1-2 sentences.

Context:
{context}

Answer:
{answer}
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(
        **inputs,
        max_new_tokens=100
    )

    refined = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # fallback
    if not refined or len(refined) < 5:
        return answer

    return refined