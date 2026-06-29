import os
import chromadb
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

PERSIST_DIR = "./db"
COLLECTION_NAME = "langchain"

# --- 1. Set up embeddings (local, free, no API key) ---
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# --- 2. Sample documents to add ---
docs = [
    Document(page_content="Hello world", metadata={"source": "test"}),
    Document(page_content="ChromaDB is a vector database", metadata={"source": "test"}),
]

# --- 3. Build and persist the vectorstore via LangChain ---
print("Building and persisting vectorstore...")
vectordb = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    collection_name=COLLECTION_NAME,
    persist_directory=PERSIST_DIR,
)
print(f"Persisted {len(docs)} documents to '{PERSIST_DIR}'.")

# --- 4. Read it back directly via chromadb (the method you found) ---
print("\nReloading via chromadb.PersistentClient...")
client = chromadb.PersistentClient(path=PERSIST_DIR)

print("Collections found:", client.list_collections())

collection = client.get_collection(name=COLLECTION_NAME)
print(f"Collection '{COLLECTION_NAME}' contains {collection.count()} items.")

# Peek at what's stored
result = collection.get(limit=5, include=["documents", "metadatas"])
for doc_id, text, meta in zip(result["ids"], result["documents"], result["metadatas"]):
    print(f"- id={doc_id} | text={text!r} | metadata={meta}")