from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_answer(
    question,
    context,
    history
):
    prompt = f"""
    You are a RAG assistant.

    Rules:

1. Use only provided context.
2. Use previous chat history when the user refers to things using:
- it
- they
- this
- that
- those
3. Never hallucinate.
4. If answer not present say:
"I couldn't find anything about that in the document."

Previous Chat:

{history}

Context:

{context}

Question:

{question}
"""

    response = model.generate_content(
        prompt
    )

    print("\n\n========== PROMPT ==========\n")
    print(prompt)
    print("\n========== END PROMPT ==========\n")
    
    return response.text