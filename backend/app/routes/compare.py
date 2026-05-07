from fastapi import APIRouter

from app.services.gemini_service import ask_llm
from app.services.rag_service import ask_rag
from app.services.graphrag_service import ask_graph_rag

router = APIRouter()


@router.get("/compare")
def compare_pipelines(query: str):

    llm_response = ask_llm(query)

    rag_response = ask_rag(query)

    graph_response = ask_graph_rag(query)

    return {
        "query": query,

        "llm_only": llm_response,

        "basic_rag": rag_response,

        "graph_rag": graph_response
    }