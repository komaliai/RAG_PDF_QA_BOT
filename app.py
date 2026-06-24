import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from openai import OpenAI
from dotenv import load_dotenv
import os

# -----------------------
# LOAD ENV
# -----------------------
load_dotenv()

# -----------------------
# OPENAI CLIENT
# -----------------------
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# -----------------------
# LOAD EMBEDDINGS MODEL
# -----------------------
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# -----------------------
# LOAD VECTOR DB
# -----------------------
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# -----------------------
# STREAMLIT UI
# -----------------------
st.title("📄 PDF Q&A Chatbot (RAG)")

query = st.text_input("Ask a question from your PDF:")

if query:

    docs = vectorstore.similarity_search(query, k=3)

    st.subheader("🔎 Top Matching Chunks")

    context = ""

    for i, doc in enumerate(docs):
        st.write(f"Chunk {i+1}")
        st.write(doc.page_content)
        context += doc.page_content + "\n"

    prompt = f"""
You are a PDF Question Answering Assistant.

Answer ONLY from the provided context.

If the answer is not available in the context, reply:
"I could not find the answer in the uploaded PDFs."

Context:
{context}

Question:
{query}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    st.subheader("🤖 Answer")
    st.write(response.output_text)