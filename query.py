from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

VECTOR_DB = "chroma_db"    #this is the actual vector db, i should probably have a env file for this
EMBEDDING_MODEL = "nomic-embed-text"


print("testing1")
embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)   #this is the embedding model
print("testing2")
vectordb = Chroma(
    persist_directory=VECTOR_DB,
    embedding_function=embeddings,
)     #initialise the vector database with the embeddings
print("testing3")


query = "How should I respond to an SSH brute force attack?"    #example query

result = vectordb.similarity_search(query, k=1) #this is the search, k=3 means return the most similar result, if i change k=2 then its the top two results 
print("testing4")


for i, doc in enumerate(result, 1):
    print(f"Result {i}")
    print(f"Source: {doc.metadata.get('source')}")
    print(doc.page_content)
    print("-" * 80)