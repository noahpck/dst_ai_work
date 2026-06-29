from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

VECTOR_DB = "chroma_db"    
EMBEDDING_MODEL = "nomic-embed-text" 


embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)   #this is the embedding model
vectordb = Chroma(
    persist_directory=VECTOR_DB,
    embedding_function=embeddings,
)    

query = input("Enter your query: ")    

result = vectordb.similarity_search(query, k=3) 


for i, doc in enumerate(result, 1):
    print(f"Result {i}")
    print(f"Source: {doc.metadata.get('source')}")
    print(doc.page_content)
    print("-" * 80)