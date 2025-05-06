
# AskTheWeb 🧠🌐

**AskTheWeb** is an intelligent information retrieval system that fetches content from a given weblink, processes it into meaningful vector representations using embeddings, and then generates accurate answers using a Large Language Model (LLM) via the Groq API.

---

## 🚀 Features

- 🔗 Extracts text content from any publicly accessible URL
- ✨ Converts content into vector embeddings using SentenceTransformers
- 🧠 Uses FAISS for fast similarity search and retrieval
- 🤖 Groq LLM integration for intelligent answer generation
- 🎛️ Clean and simple Gradio UI for interaction

---

## 🧱 Tech Stack

- **Python 3.10+**
- **Gradio** – for building the UI
- **BeautifulSoup4** – for parsing webpage content
- **SentenceTransformers** – for generating vector embeddings
- **FAISS** – for storing and retrieving similar chunks
- **Groq API** – to interface with LLM for final answers
- **python-dotenv** – to manage environment variables

---

## 📁 Project Structure

```
AskTheWeb/
├── app.py                   # Main Gradio interface
├── web_ingest.py           # URL scraping and chunking
├── embedder.py             # Embedding logic and FAISS setup
├── llm_interface.py        # Groq LLM query handler
├── .env                    # Environment variables (API keys)
├── requirements.txt        # Dependencies
└── README.md               # Project description
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/AskTheWeb.git
cd AskTheWeb
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables
Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the App
```bash
python app.py
```

---

## ✅ How It Works

1. User inputs a valid URL.
2. Text is extracted, cleaned, and chunked.
3. Each chunk is embedded using `SentenceTransformer`.
4. Chunks are stored in a FAISS index.
5. A question is asked via the UI.
6. The top matching chunks are selected based on cosine similarity.
7. The chunks and question are sent to the Groq LLM for a generated answer.

---

## 📝 Example Use Case

> URL: `https://en.wikipedia.org/wiki/Machine_learning`  
> Question: _"What are some common algorithms in Machine Learning?"_

🧠 Output (from Groq LLM):  
_"Some commonly used machine learning algorithms include decision trees, support vector machines, k-nearest neighbors, and neural networks."_

---

## 🧑‍💻 Author

**Shailaja Vadayar**  
[LinkedIn](https://www.linkedin.com/in/shailajavadayar)

---

## 📄 License

This project is licensed under the MIT License.# AskTheWeb
This project will search the provided weblink and generate answers to your query.
