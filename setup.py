#this is to automate setting everything up on a new NUC
from pathlib import Path
from ingest import ingest
import ollama 

def check_ollama_models_installed():
    installed = {m.model for m in ollama.list().models}
    if "llama3.1:8b" not in installed:
        ollama.pull("llama3.1:8b")

    if "nomic-embed-text:latest" not in installed:
        ollama.pull("nomic-embed-text:latest")
    
    else:
        print("Ollama models are already installed.")

def create_vector_database():
    if not Path("chroma_db").exists():
        ingest()  # Run the ingest.py script to create the vector database

# def start_ollama():
#     try:
#         // Start the Ollama server here 
#     except Exception as e:
#         print(f"Error starting Ollama: {e}")


check_ollama_models_installed()  # Check if Ollama models are installed
create_vector_database()  # Create the vector database if it doesn't exist

#need to ask if they expect ollama to already be installed on their NUC's 


