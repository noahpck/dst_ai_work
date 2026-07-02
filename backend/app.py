import os
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from dotenv import load_dotenv
import ollama
import time

load_dotenv()
vector_database = os.getenv("VECTOR_DB")
embedding_model = os.getenv("EMBEDDING_MODEL")

embeddings = OllamaEmbeddings(model=embedding_model)   
vectordb = Chroma(
    persist_directory=vector_database,
    embedding_function=embeddings,
)    

llm = ChatOllama(model="llama3.1:8b")
def logs_output(query: str):

    results = vectordb.similarity_search(query, k=3) 
    context = "\n".join(doc.page_content for doc in results)
    prompt = f"""You are an expert Incident Response Assistant.
    Use only the provided context to analyze the following log and list containment steps.
    In the prompt they may specify the size of the response they desire, if they do not specify a size, provide a concise response.
    Playbooks: {context}

    Question: {query}
    """
    try:
    
        start_time = time.perf_counter()
        response = llm.invoke(prompt) 
        end_time = time.perf_counter()
        execution_time = end_time - start_time
       
                
    except Exception as e:
        print(e)

    return response.content, f"Time to generate response: {execution_time:.2f} seconds"


