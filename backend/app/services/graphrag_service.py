import time

from app.services.graph_service import get_graph_context
from app.services.gemini_service import ask_llm


def ask_graph_rag(query: str):

    start_time = time.time()

    graph_context = get_graph_context(query)

    final_prompt = f"""
You are a GraphRAG assistant.

Use the graph knowledge below to answer the question.

GRAPH KNOWLEDGE:
{graph_context}

QUESTION:
{query}
"""

    response = ask_llm(final_prompt)

    latency = round(time.time() - start_time, 2)

    return {
    "pipeline": "GraphRAG",
    "query": query,
    "response": response["response"],
    "latency_seconds": latency,
    "input_tokens_estimate": response["input_tokens_estimate"],
    "output_tokens_estimate": response["output_tokens_estimate"],
    "estimated_cost_usd": response["estimated_cost_usd"]
}