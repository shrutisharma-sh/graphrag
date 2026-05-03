from fastapi import APIRouter

from app.services.gemini_service import ask_llm
from app.models.llm_models import (
    PromptRequest,
    BenchmarkResponse
)

router = APIRouter()


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