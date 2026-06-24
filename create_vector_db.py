"""mport os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

pdf_folder = "pdf_data"

documents = []

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        path = os.path.join(pdf_folder, file)
        loader = PyPDFLoader(path)
        docs = loader.load()

        print(f"\n📄 FILE: {file}")
        print(docs[0].page_content[:500])  # clean text preview

        documents.extend(docs)


from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print(len(chunks))
print(chunks[0])
print(chunks[0].page_content)


api_key = os.getenv("GOOGLE_API_KEY")

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    model="text-embedding-004",
    google_api_key=api_key
)

print("Embeddings model loaded successfully")

from langchain_community.vectorstores import FAISS

# create FAISS vector database
vectorstore = FAISS.from_documents(chunks, embeddings)

# save it locally
vectorstore.save_local("faiss_index")

print("FAISS vector database created successfully")"""

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# STEP 1: Load PDFs
pdf_folder = "pdf_data"
documents = []

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(pdf_folder, file))
        documents.extend(loader.load())

print("PDF loaded:", len(documents))

# STEP 2: Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print("Chunks created:", len(chunks))
print("Sample chunk:\n", chunks[0].page_content)

# STEP 3: Embeddings (NO API KEY)
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

print("Embedding model loaded")

# STEP 4: FAISS Vector DB
vectorstore = FAISS.from_documents(chunks, embeddings)

vectorstore.save_local("faiss_index")

print("Vector DB created successfully 🚀")