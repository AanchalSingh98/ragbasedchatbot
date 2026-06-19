import gradio as gr
import uvicorn

from fastapi import FastAPI
from gradio.routes import mount_gradio_app

from rag.loader import load_documents
from rag.chunker import create_chunks
from rag.embeddings import get_embeddings
from rag.vector_store import (
    create_vector_store,
    load_vector_store
)
from rag.retriever import retrieve
from rag.llm import generate_answer
# Global variables
db = None
embeddings = get_embeddings()


# --------------------
# PDF Processing
# --------------------

def process_pdf(files):

    global db

    if not files:
        return "Please upload PDF(s) first."

    try:

        file_paths = [
            file.name for file in files
        ]

        docs = load_documents(
            file_paths
        )

        chunks = create_chunks(
         docs
        )

        print("\n\n========== FIRST CHUNK ==========\n")
        print(chunks[0].page_content)
        print("\n========== END ==========\n")

        db = create_vector_store(
             chunks,
             embeddings
        )

        return (
            f"✅ PDFs Processed\n"
            f"Documents: {len(file_paths)}\n"
            f"Chunks: {len(chunks)}"
        )

    except Exception as e:

        return f"❌ Error: {e}"


# --------------------
# Chat Function
# --------------------

def chat(message, history):

    global db

    if db is None:

        return (
            "Please upload and process PDF first."
        )

    context, pages = retrieve(
        message,
        db
    )
    print("\n\n========== RETRIEVED CONTEXT ==========\n")
    print(context)
    print("\n========== END CONTEXT ==========\n")

    answer = generate_answer(
        message,
        context,
        history
    )

    if pages:

        answer += (
            f"\n\n📄 Source Pages: "
            f"{', '.join(pages)}"
        )

    return answer


# --------------------
# Load Existing DB
# --------------------

try:

    db = load_vector_store(
        embeddings
    )

    print(
        "Existing vector DB loaded."
    )

except:

    print(
        "No existing vector DB found."
    )

    db = None


# --------------------
# UI
# --------------------

with gr.Blocks() as demo:

    gr.Markdown(
        "# PDF RAG Chatbot"
    )

    pdfs = gr.File(
        file_count="multiple",
        file_types=[".pdf"]
    )

    process_btn = gr.Button(
        "Process PDFs"
    )

    status = gr.Textbox(
        label="Status"
    )

    process_btn.click(
        process_pdf,
        inputs=pdfs,
        outputs=status
    )

    chatbot = gr.ChatInterface(
        fn=chat,
        title="Ask Questions"
    )
# --------------------
# FastAPI + Gradio
# --------------------

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "running"}

app = mount_gradio_app(
    app,
    demo,
    path="/"
)
# --------------------
# Run
# --------------------

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860
    )