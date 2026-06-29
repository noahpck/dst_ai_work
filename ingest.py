
"""
ingest.py

Ingest Markdown documents into a local ChromaDB vector database.

Requirements:
    pip install langchain langchain-community langchain-ollama chromadb

Run:
    python ingest.py
"""


print("testing starting ingest.py")

from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# ============================================================
# Configuration
# ============================================================

DOCUMENT_DIR = "documents"
VECTOR_DB = "chroma_db"

EMBEDDING_MODEL = "nomic-embed-text"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100



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
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
)



# Load the playbooks

documents = []

doc_path = Path(DOCUMENT_DIR)

if not doc_path.exists():
    raise FileNotFoundError(f"Directory '{DOCUMENT_DIR}' does not exist.")

for file in doc_path.glob("*.md"):   #this checks files with .md extension

    print(f"Loading {file.name}")

    loader = TextLoader(str(file), encoding="utf-8")

    raw_document = loader.load()[0]
    #print("Length:", len(raw_document.page_content))
   # print(repr(raw_document.page_content[:200]))

    # Preserve Markdown structure
    header_docs = markdown_splitter.split_text(raw_document.page_content)
   # print("Header docs:", len(header_docs))
    #print(header_docs)

    # Further split large sections
    chunks = character_splitter.split_documents([raw_document])
    print("Chunks:", len(chunks))
    #if chunks:
      #  print(chunks[0].page_content[:200])

    # Add source filename metadata
    for chunk in chunks:
        chunk.metadata["source"] = file.name

    documents.extend(chunks)


print(f"\nLoaded {len(documents)} document chunks.")


# ============================================================
# Create Embeddings
# ============================================================

embeddings = OllamaEmbeddings(
    model=EMBEDDING_MODEL
)





# Store in ChromaDB
print("Testing embeddings...")

vec = embeddings.embed_query("hello world")

print("Embedding generated!")
print(len(vec))

# vectordb = Chroma.from_documents(
#     documents=documents,
#     embedding=embeddings,
#     persist_directory=VECTOR_DB,
# )

print("Creating database...")
vectordb = Chroma(
    persist_directory=VECTOR_DB,
    embedding_function=embeddings,
)

print("Adding one document...")
print(documents[0])
print(documents[0].metadata)
vectordb.add_documents([documents[0]])  #this currently making the program hang


#vectordb.persist()    #update the database with the new documents

print("\nVector database created successfully.")
print(f"Stored at: {VECTOR_DB}")
