import pickle
import faiss
import numpy as np
import os

from app.services.embedding_service import generate_embedding

INDEX_PATH = "app/rag/vector_store/faiss_index.index"
CHUNKS_PATH = "app/rag/vector_store/chunks.pkl"


def search_similar_chunks(query: str, top_k=2):

    if not os.path.exists(INDEX_PATH):
        raise FileNotFoundError("FAISS index not found")

    if not os.path.exists(CHUNKS_PATH):
        raise FileNotFoundError("chunks.pkl not found")

    
    index = faiss.read_index(INDEX_PATH)

    
    with open(CHUNKS_PATH, "rb") as f:
        document_chunks = pickle.load(f)

    
    query_embedding = generate_embedding(query)
    query_embedding = np.array([query_embedding]).astype("float32")

    
    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        if idx < len(document_chunks):
            results.append(document_chunks[idx])

    return results