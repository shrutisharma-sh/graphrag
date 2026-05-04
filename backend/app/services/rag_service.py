from app.services.faiss_service import search_similar_chunks
from app.services.gemini_service import ask_llm


def build_rag_prompt(query: str, context_chunks: list):

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are an AI assistant answering based ONLY on the given context.

Context:
{context}

Question:
{query}

Answer clearly and concisely based on the context.
"""

    return prompt


def ask_rag(query: str):

# retrivsal chunk
    chunks = search_similar_chunks(query)

#prompt building
    prompt = build_rag_prompt(query, chunks)

   #ask llm 
    result = ask_llm(prompt)

    return {
        "response": result["response"],
        "retrieved_chunks": chunks,
        "latency_seconds": result["latency_seconds"],
        "input_tokens_estimate": result["input_tokens_estimate"],
        "output_tokens_estimate": result["output_tokens_estimate"],
        "estimated_cost_usd": result["estimated_cost_usd"],
        "model": result["model"]
    }