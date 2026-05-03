from app.services.embedding_service import generate_embedding

text = "GraphRAG improves retrieval"

embedding = generate_embedding(text)

print(type(embedding))
print()

print("Embedding dimension:")
print(len(embedding))
print()

print("First 10 values:")
print(embedding[:10])