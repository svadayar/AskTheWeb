import gradio as gr
import os
from web_ingest import process_web_url
from embedder import embed_query
from groq import Groq
from dotenv import load_dotenv

# Load GROQ API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

client = Groq(api_key=GROQ_API_KEY)

MODEL = "llama3-70b-8192"  # ✅ Confirmed model available in Groq


def ask_the_web(url, question):
    try:
        # Step 1: Process the web page and build FAISS index
        index, chunks = process_web_url(url)

        # Step 2: Embed the query
        query_vector = embed_query(question)

        # Step 3: Search FAISS for top matches
        k = 3
        distances, indices = index.search(query_vector, k)
        retrieved_chunks = [chunks[i] for i in indices[0] if i < len(chunks)]

        # Step 4: Construct prompt for Groq model
        context = "\n".join(retrieved_chunks)
        prompt = f"""Use the following information to answer the user's question:\n\n{context}\n\nQuestion: {question}\nAnswer:"""

        # Step 5: Generate response using Groq
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error: {str(e)}"


# Gradio UI
demo = gr.Interface(
    fn=ask_the_web,
    inputs=[
        gr.Textbox(label="Enter a Web URL"),
        gr.Textbox(label="What do you want to know?")
    ],
    outputs=gr.Textbox(label="Answer from Web"),
    title="Ask the Web",
    description="Retrieves and analyzes content from a given webpage to answer your question using Groq's LLM."
)

if __name__ == "__main__":
    demo.launch()
