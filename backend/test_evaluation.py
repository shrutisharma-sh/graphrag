from app.services.evaluation_service import evaluate_bertscore


reference_answer = """
GraphRAG combines graph databases with retrieval augmented generation.
"""

generated_answer = """
GraphRAG uses graph databases together with retrieval systems.
"""


result = evaluate_bertscore(
    reference_answer,
    generated_answer
)

print("\nBERTScore Evaluation:\n")

print(result)