from fastapi import APIRouter
from app.services.rag_service import ask_rag


from app.services.gemini_service import ask_llm
from app.models.llm_models import (
    PromptRequest,
    BenchmarkResponse
)

router = APIRouter()

@router.post("/benchmark/compare")
def compare_pipelines(request: PromptRequest):

    prompt = request.prompt

    #llm 
    llm_result = ask_llm(prompt)

    #rag
    rag_result = ask_rag(prompt)

    return {
        "prompt": prompt,

        "llm": {
            "model": llm_result["model"],
            "response": llm_result["response"],
            "latency_seconds": llm_result["latency_seconds"],
            "input_tokens_estimate": llm_result["input_tokens_estimate"],
            "output_tokens_estimate": llm_result["output_tokens_estimate"],
            "estimated_cost_usd": llm_result["estimated_cost_usd"]
        },

        "rag": {
            "model": rag_result["model"],
            "response": rag_result["response"],
            "latency_seconds": rag_result["latency_seconds"],
            "input_tokens_estimate": rag_result["input_tokens_estimate"],
            "output_tokens_estimate": rag_result["output_tokens_estimate"],
            "estimated_cost_usd": rag_result["estimated_cost_usd"],
            "retrieved_chunks": rag_result["retrieved_chunks"]
        }
    }

@router.post("/benchmark/rag")
def benchmark_rag(request: PromptRequest):

    result = ask_rag(request.prompt)

    return {
        "model": result["model"],
        "prompt": request.prompt,
        "response": result["response"],
        "latency_seconds": result["latency_seconds"],
        "input_tokens_estimate": result["input_tokens_estimate"],
        "output_tokens_estimate": result["output_tokens_estimate"],
        "estimated_cost_usd": result["estimated_cost_usd"],
        "retrieved_chunks": result["retrieved_chunks"]
    }

@router.post(
    "/benchmark/llm",
    response_model=BenchmarkResponse
)
def benchmark_llm(request: PromptRequest):

    result = ask_llm(request.prompt)

    return {
        "model": result["model"],
        "prompt": request.prompt,
        "response": result["response"],
        "latency_seconds": result["latency_seconds"],
        "input_tokens_estimate": result["input_tokens_estimate"],
        "output_tokens_estimate": result["output_tokens_estimate"],
        "estimated_cost_usd": result["estimated_cost_usd"]
    }