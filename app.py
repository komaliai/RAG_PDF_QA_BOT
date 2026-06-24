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

# -----------------------
# CHAT MEMORY (IMPORTANT)
# -----------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# show chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

query = st.chat_input("Ask a question from your PDF...")

if query:

    # store user message
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").write(query)

    with st.spinner("Thinking... 🤔"):

        # -----------------------
        # RETRIEVE DOCS
        # -----------------------
        docs = vectorstore.similarity_search(query, k=4)

        # -----------------------
        # SAFE CHECK FIRST
        # -----------------------
        if not docs:
            answer = "I could not find the answer in the uploaded PDFs."
        else:
            # build context safely
            context = "\n".join([doc.page_content for doc in docs])

            prompt = f"""
You are a PDF Question Answering Assistant.

Rules:
- Use ONLY the context below
- Be accurate and concise
- If answer not found, say: "I could not find the answer in the uploaded PDFs."

Context:
{context}

Question:
{query}

Answer:
"""

            response = client.responses.create(
                model="gpt-4.1-mini",
                input=prompt
            )

            answer = response.output_text

    # store assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)