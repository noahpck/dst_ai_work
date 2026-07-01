import os
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv

load_dotenv()
vector_database = os.getenv("VECTOR_DB")
embedding_model = os.getenv("EMBEDDING_MODEL")

embeddings = OllamaEmbeddings(model=embedding_model)   
vectordb = Chroma(
    persist_directory=vector_database,
    embedding_function=embeddings,
)    

query = input("Enter your query: ")    

result = vectordb.similarity_search(query, k=3) 

# Display top 3 results 
for i, doc in enumerate(result, 1):
    print(f"Result {i}")
    print(f"Source: {doc.metadata.get('source')}")
    print(doc.page_content)
    print("-" * 80)