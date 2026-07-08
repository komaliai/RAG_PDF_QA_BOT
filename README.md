# 📄 RAG PDF Question Answering Chatbot

A Retrieval-Augmented Generation (RAG) based chatbot that answers questions from PDF documents using semantic search and a Large Language Model (LLM).

This project extracts text from PDF files, converts the text into vector embeddings using HuggingFace, stores them in a FAISS vector database, retrieves the most relevant document chunks based on the user's query, and generates accurate answers using the OpenAI GPT model.

The application is built with Streamlit, providing an interactive web interface for users to ask questions about uploaded PDF documents.


## Features

- 📄 Load and process PDF documents
- ✂️ Split documents into meaningful text chunks
- 🔍 Generate semantic embeddings using HuggingFace (`all-MiniLM-L6-v2`)
- 🗂️ Store embeddings efficiently using FAISS Vector Database
- 🔎 Retrieve the most relevant document chunks using similarity search
- 🤖 Generate context-aware answers using OpenAI GPT
- 💬 Interactive web interface built with Streamlit
- ⚡ Fast and efficient document retrieval

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| LangChain | RAG pipeline and document processing |
| HuggingFace Embeddings | Convert text into vector embeddings |
| FAISS | Vector database for similarity search |
| OpenAI GPT-4.1-mini | Generate accurate answers from retrieved context |
| Streamlit | Interactive web application |
| PyPDFLoader | Load and extract text from PDF documents |
| RecursiveCharacterTextSplitter | Split documents into smaller chunks |
| python-dotenv | Manage API keys securely |


## 🏗️ Project Architecture


                PDF Documents
                      │
                      ▼
              PyPDFLoader
                      │
                      ▼
      RecursiveCharacterTextSplitter
                      │
                      ▼
     HuggingFace Embeddings
      (all-MiniLM-L6-v2)
                      │
                      ▼
          FAISS Vector Database
                      │
        User Question │
               ───────┘
                      ▼
          Similarity Search (Top-K)
                      │
                      ▼
        Retrieved Context Chunks
                      │
                      ▼
          OpenAI GPT-4.1-mini
                      │
                      ▼
             Final Answer

## 📂 Project Structure

```text
RAG_PDF_QA_BOT/
│
├── app.py                     # Streamlit application
├── create_vector_db.py        # Creates FAISS vector database
├── requirements.txt           # Project dependencies
├── .env                       # API Keys (not uploaded)
├── .gitignore                 # Ignore sensitive files
│
├── pdf_data/                  # Input PDF documents
│
├── faiss_index/               # Generated FAISS vector database
│   ├── index.faiss
│   └── index.pkl
│
├── test_app.py                # Streamlit testing
├── test_openai.py             # OpenAI API testing
└── test_google_embedding.py   # Google Embedding API testing
```

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/komaliai/RAG_PDF_QA_BOT.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd RAG_PDF_QA_BOT
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` File

Add your OpenAI API Key:

```text
OPENAI_API_KEY=your_api_key_here
```

### 5️⃣ Create the Vector Database

```bash
python create_vector_db.py
```

### 6️⃣ Run the Streamlit Application

```bash
streamlit run app.py
```

## 📸 Sample Output

### User Question

```text
What is Battery Management System?
```

### Chatbot Response

```text
A Battery Management System (BMS) is an electronic system that monitors, protects, and manages rechargeable battery packs. It ensures battery safety by monitoring voltage, current, temperature, State of Charge (SOC), and State of Health (SOH), while improving battery performance and lifespan.
```

## 🔮 Future Improvements

- 📂 Upload PDFs directly through the Streamlit interface
- 💬 Support multi-turn conversations with chat history
- 📚 Handle multiple PDF documents simultaneously
- 📄 Display source page numbers for generated answers
- 🌐 Deploy on AWS or Azure
- 🐳 Dockerize the application
- ⚡ Improve retrieval accuracy using hybrid search
- 🔐 Add user authentication

## 👩‍💻 Author

**Komali Devi Puchakayala**

- GitHub: https://github.com/komaliai
- Passionate about Data Science, Machine Learning, NLP, and Generative AI.


  
