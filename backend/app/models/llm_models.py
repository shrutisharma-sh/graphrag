from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str


class BenchmarkResponse(BaseModel):
    model: str
    prompt: str
    response: str
    latency_seconds: float
    input_tokens_estimate: int
    output_tokens_estimate: int
    estimated_cost_usd: float