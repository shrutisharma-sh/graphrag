from app.services.graphrag_service import ask_graph_rag

query = "How does GraphRAG improve retrieval?"

result = ask_graph_rag(query)

print(result)