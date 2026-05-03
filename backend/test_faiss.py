from app.services.faiss_service import (
    create_faiss_index,
    search_similar_chunks
)

# Create vector index
create_faiss_index()

print()

query = "How does GraphRAG improve retrieval?"

results = search_similar_chunks(query)

print("Query:")
print(query)

print("\nRetrieved Chunks:\n")

for i, chunk in enumerate(results):

    print(f"Chunk {i+1}:")
    print(chunk)
    print()