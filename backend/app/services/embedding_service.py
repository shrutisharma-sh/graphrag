from sentence_transformers import SentenceTransformer

# Lightweight embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def generate_embedding(text: str):

    embedding = embedding_model.encode(text)

    return embedding