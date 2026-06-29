import os
from dotenv import load_dotenv
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


#Setting up variables
load_dotenv()
document_directory = os.getenv("DOCUMENT_DIR")
vector_database = os.getenv("VECTOR_DB")

embedding_model = os.getenv("EMBEDDING_MODEL")

chunk_size = int(os.getenv("CHUNK_SIZE"))
chunk_overlap = int(os.getenv("CHUNK_OVERLAP"))



# Markdown Header Splitter

headers_to_split_on = [
    ("#", "Heading 1"),
    ("##", "Heading 2"),
    ("###", "Heading 3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

character_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
)

# Load the playbooks

documents = []

doc_path = Path(document_directory)

if not doc_path.exists():
    raise FileNotFoundError(f"Directory '{document_directory}' does not exist.")


for file in doc_path.glob("*.md"):   #this checks files with .md extension

    loader = TextLoader(str(file), encoding="utf-8")
    raw_document = loader.load()[0]
    header_docs = markdown_splitter.split_text(raw_document.page_content)
    chunks = character_splitter.split_documents(header_docs)

    # Add source filename metadata
    for chunk in chunks:
        chunk.metadata["source"] = file.name

    documents.extend(chunks)


print(f"\nLoaded {len(documents)} document chunks.")


# Create Embeddings

embeddings = OllamaEmbeddings(
    model=embedding_model
)

# Store in ChromaDB

vectordb = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory=vector_database,
)

print("\nVector database created successfully.")
print(f"Stored at: {vector_database}")
