from fastapi import APIRouter
from app.services.gemini_service import ask_gemini

router = APIRouter()


@router.get("/test-llm")
def test_llm():

    prompt = "Explain GraphRAG in simple words."

    response = ask_gemini(prompt)

    return {
        "prompt": prompt,
        "response": response
    }