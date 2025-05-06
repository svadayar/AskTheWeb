import faiss
import numpy as np

index = faiss.IndexFlatL2(1536)  # Embedding dim

documents = []

def add_to_vector_store(text_chunks, embeddings, metadata=None):
    global documents
    vectors = np.array(embeddings).astype("float32")
    index.add(vectors)
    documents.extend([{"text": txt, "metadata": metadata} for txt in text_chunks])

def search_vector_store(query_embedding, k=3):
    D, I = index.search(np.array([query_embedding]).astype("float32"), k)
    return [documents[i] for i in I[0]]
