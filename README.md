RAG PDF Question Answering Chatbot

Project Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask questions in natural language. The system retrieves the most relevant document chunks using FAISS and HuggingFace embeddings, then uses an OpenAI language model to generate accurate answers based on the retrieved context.

Features
-PDF document loading
-Text chunking
-HuggingFace Embeddings (all-MiniLM-L6-v2)
-FAISS vector database
-Semantic similarity search
-OpenAI GPT for answer generation
-Streamlit web interface
🛠️ Tech Stack
-Python
-LangChain
-HuggingFace Embeddings
-FAISS
-OpenAI API
-Streamlit
📂 Project Structure
RAG_PDF_QA_BOT/
│── app.py
│── create_vector_db.py
│── pdf_data/
│── faiss_index/
│── requirements.txt
│── .env
🔄 Workflow
PDF
 ↓
PyPDFLoader
 ↓
Text Chunking
 ↓
HuggingFace Embeddings
 ↓
FAISS
 ↓
Similarity Search
 ↓
OpenAI GPT
 ↓
Answer
▶️ Run the Project
pip install -r requirements.txt
python create_vector_db.py
streamlit run app.py

This kind of README looks much more professional and is great for interviews.

Before we edit the README

Let's finish uploading the project first.
