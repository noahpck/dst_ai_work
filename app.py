import os
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from dotenv import load_dotenv




def main(query: str):
    load_dotenv()
    vector_database = os.getenv("VECTOR_DB")
    embedding_model = os.getenv("EMBEDDING_MODEL")

    embeddings = OllamaEmbeddings(model=embedding_model)   
    vectordb = Chroma(
        persist_directory=vector_database,
        embedding_function=embeddings,
    )    

    #query = input("Enter your query: ")    

    results = vectordb.similarity_search(query, k=3) 

    context = "\n".join(doc.page_content for doc in results)
    prompt = f"""You are an expert Incident Response Assistant.
    Use only the provided context to analyze the following log and list containment steps.

    Playbooks: {context}

    Question: {query}

    Answer: 
    """
    print("Prompt sent to LLM:")
    print(prompt)
    llm = ChatOllama(model="llama3.1:8b")
    try:
        response = llm.invoke(prompt)  #currently very slow, but works.
        print(response.content)
    except Exception as e:
        print(e)

    return response.content


