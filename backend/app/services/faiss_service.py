import os
import faiss
import numpy as np

from app.services.embedding_service import generate_embedding


DOCUMENT_PATH = "app/rag/documents/graphrag.txt"

INDEX_PATH = "app/rag/vector_store/faiss_index.index"


document_chunks = []


def load_document():

    with open(DOCUMENT_PATH, "r", encoding="utf-8") as file:

        text = file.read()

    return text


def chunk_text(text: str):

    """
    Simple chunking by paragraph.
    """

    chunks = text.split("\n\n")

    return [chunk.strip() for chunk in chunks if chunk.strip()]


def create_faiss_index():

    global document_chunks

    text = load_document()

    document_chunks = chunk_text(text)

    embeddings = []

    for chunk in document_chunks:

        embedding = generate_embedding(chunk)

        embeddings.append(embedding)

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

   
    index.add(embeddings)

    
    faiss.write_index(index, INDEX_PATH)

    print("FAISS index created successfully.")

    print(f"Total chunks indexed: {len(document_chunks)}")


def search_similar_chunks(query: str, top_k=2):

    global document_chunks

    
    text = load_document()
    document_chunks = chunk_text(text)

    
    if not os.path.exists(INDEX_PATH):
        create_faiss_index()

    index = faiss.read_index(INDEX_PATH)

    query_embedding = generate_embedding(query)
    query_embedding = np.array([query_embedding]).astype("float32")

    
    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        if idx < len(document_chunks):  # safety check
            results.append(document_chunks[idx])

    return results