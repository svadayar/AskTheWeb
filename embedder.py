from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text_chunks(chunks):
    """
    Converts text chunks into float32 embedding vectors.
    """
    embeddings = model.encode(chunks, convert_to_numpy=True)
    return np.array(embeddings).astype("float32")

def embed_query(query):
    """
    Converts a single query to a float32 embedding.
    """
    embedding = model.encode([query], convert_to_numpy=True)
    return np.array(embedding).astype("float32")
