from app.services.rag_service import ask_rag

query = "What is GraphRAG and how does it improve retrieval?"

result = ask_rag(query)

print("Query:")
print(query)

print("\nRetrieved Chunks:\n")

for i, chunk in enumerate(result["retrieved_chunks"]):
    print(f"Chunk {i+1}:")
    print(chunk)
    print()

print("\nRAG Response:\n")
print(result["response"])