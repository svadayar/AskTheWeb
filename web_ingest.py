import requests
from bs4 import BeautifulSoup
import faiss
import numpy as np
from embedder import embed_text_chunks

def extract_text_from_url(url):
    """
    Scrapes and cleans text content from a web page.
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    return [p.get_text().strip() for p in paragraphs if p.get_text().strip()]

def process_web_url(url):
    """
    Takes a web URL, extracts text, creates embeddings, and builds a FAISS index.
    """
    # Step 1: Extract and chunk content
    text_chunks = extract_text_from_url(url)

    if not text_chunks:
        raise ValueError("No content extracted from the URL.")

    # Step 2: Embed text chunks
    embeddings = embed_text_chunks(text_chunks)

    # Step 3: Create FAISS index using correct dimension
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)

    # Step 4: Add embeddings to the index
    index.add(embeddings)

    return index, text_chunks
