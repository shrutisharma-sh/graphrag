from fastapi import APIRouter

from app.services.gemini_service import ask_llm
from app.services.rag_service import ask_rag
from app.services.graphrag_service import ask_graph_rag
from app.services.evaluation_service import evaluate_bertscore

router = APIRouter()


@router.get("/compare")
def compare_pipelines(query: str):

    # Reference answer
    reference_answer = """
    GraphRAG combines graph databases with retrieval augmented generation
    to improve reasoning and connected knowledge retrieval.
    """


    #piplines 

    llm_result = ask_llm(query)

    rag_result = ask_rag(query)

    graph_result = ask_graph_rag(query)


    #evaluations

    llm_eval = evaluate_bertscore(
        reference_answer,
        llm_result["response"]
    )

    rag_eval = evaluate_bertscore(
        reference_answer,
        rag_result["response"]
    )

    graph_eval = evaluate_bertscore(
        reference_answer,
        graph_result["response"]
    )


    #ataching 

    llm_result["evaluation"] = llm_eval

    rag_result["evaluation"] = rag_eval

    graph_result["evaluation"] = graph_eval


    return {
        "query": query,

        "llm_only": llm_result,

        "basic_rag": rag_result,

        "graph_rag": graph_result
    }