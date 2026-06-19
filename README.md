 # 🧠 RAG Chatbot - PDF Question Answering System

A Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask natural language questions about their content.

The system retrieves relevant document chunks using semantic search and generates context-aware answers using Google's Gemini AI.

---

# 🚀 Features

* 📄  Upload one or multiple PDF documents
* ✂️ Automatic document chunking
* 🧠 Semantic search using vector embeddings
* 🔍 Context-aware retrieval with FAISS
* 🤖 AI-powered answers using Gemini
* 📚 Source page tracking
* ⚡ Fast document processing and querying
* ☁️ Deployed on Microsoft Azure

---

# 🏗️ How It Works

```text
PDF Upload
    ↓
Document Loader
    ↓
Text Chunking
    ↓
Embeddings Generation
    ↓
FAISS Vector Database
    ↓
Retriever
    ↓
Gemini AI
    ↓
Final Answer + Source Pages
```

---

# 🛠️ Tech Stack

## Frontend

* Gradio

## Backend

* FastAPI
* Python

## AI / RAG

* LangChain
* Google Gemini API
* FAISS
* Sentence Transformers

## Deployment

* Microsoft Azure App Service
* GitHub Actions

---

# 📂 Project Structure

```text
RagChatBot101/
│
├── app.py
├── requirements.txt
├── .gitignore
│
└── rag/
    ├── loader.py
    ├── chunker.py
    ├── embeddings.py
    ├── vector_store.py
    ├── retriever.py
    └── llm.py
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/AanchalSingh98/RagChatBot101.git
cd RagChatBot101
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# ▶️ Run Locally

```bash
python app.py
```

Open:

```text
http://localhost:7860
```

---

# ☁️ Azure Deployment

This project is deployed on Microsoft Azure App Service using:

* Python 3.11
* FastAPI
* Gunicorn
* GitHub Actions CI/CD

Startup Command:

```bash
gunicorn -w 1 -k uvicorn.workers.UvicornWorker app:app
```

---

# 📈 Key Highlights

* Built a complete Retrieval-Augmented Generation (RAG) pipeline
* Implemented PDF-based semantic search
* Used FAISS for efficient vector similarity search
* Integrated Google Gemini AI for document-grounded responses
* Deployed on Microsoft Azure
* Supports source-aware question answering

---

# 🔮 Future Improvements

* Multi-user document sessions
* Hybrid Retrieval (FAISS + BM25)
* OCR support for scanned PDFs
* Conversation memory
* User authentication
* Cloud vector storage

---

# 👨‍💻 Author

**Aanchal singh**

B.Tech Computer Science (AI & ML)

* GitHub: https://github.com/AanchalSingh98

---

# ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub.
