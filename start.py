#this is to automate setting everything up on a new NUC
from pathlib import Path
from ingest import ingest
import ollama 
import shutil
import subprocess
import sys
import time 

def install_curl():
    if shutil.which("curl"):
        print("curl is already installed.")
        return

    print("Installing curl...")

    try:
        subprocess.run(
            ["sudo", "apt", "update"],
            check=True,
        )

        subprocess.run(
            ["sudo", "apt", "install", "-y", "curl"],
            check=True,
        )

        print("curl installed successfully.")

    except subprocess.CalledProcessError:
        print("Failed to install curl.")
        sys.exit(1)

def install_ollama():
    if shutil.which("ollama"):
        print("Ollama is already installed.")
        return

    print("Installing Ollama...")
    try:
        subprocess.run(
            "curl -fsSL https://ollama.com/install.sh | sh",
            shell=True,
            check=True,
        )
        print("Ollama installed successfully.")

    except subprocess.CalledProcessError:
        print("Failed to install Ollama.")
        sys.exit(1)

def start_ollama():
    try:
        subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print("Started Ollama.")
    except Exception:
        print("Failed to start Ollama.")


def check_ollama_models_installed():
    installed = {m.model for m in ollama.list().models}
    if "llama3.1:8b" not in installed:
        ollama.pull("llama3.1:8b")
        print("Pulled llama3.1:8b model.")
        

    if "nomic-embed-text:latest" not in installed:
        ollama.pull("nomic-embed-text:latest")
        print("Pulled nomic-embed-text:latest model.")
    
    else:
        print("Ollama models are already installed.")

def create_vector_database():
    if not Path("chroma_db").exists():
        ingest()  # Run the ingest.py script to create the vector database

    else:
        print("Vector database already exists.")


def start_streamlit():
    try:
        subprocess.run(
            ["streamlit", "run", "backend/app.py"],
            check=True,
            )
        
    except subprocess.CalledProcessError:
        print("Failed to start Streamlit.")
        sys.exit(1)


install_curl()
install_ollama()
start_ollama()
time.sleep(2)
check_ollama_models_installed()  # Check if Ollama models are installed
create_vector_database()  # Create the vector database if it doesn't exist
start_streamlit()