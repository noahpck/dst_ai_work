# Local RAG-Powered Incident Response Assistant


## What is RAG and Vector Databases

RAG, standing for Retrieval Augmented Generation, is the process of optimising the output of a large language model so it references an authoritative knowledge base outside its training data before generating a response.
In order for the LLM to access this authoritative knowledge, it uses a vector database. A vector database is unlike a normal database. It's a specialised type of data storage designed to understand the meaning and context of information, rather than just matching exact keywords.
It does this by storing vector embeddings. Vector embeddings are a way to turn real world information, like words or sentences, into lists of numbers, so that computers can understand what they actually mean.


## Overview and How it Works
This is a RAG-powered incident response assistant. The purpose of this assistant is to respond to cybersecurity-related queries. It works by utilising a vector database that stores vector embeddings generated from various incident response playbooks. These vector embeddings are numerical arrays that capture the semantic meaning of the playbooks' text.

Once the vector database has been initialised, the Ollama large language model (ollama3.1:8b) is set up and ready to receive queries. Before sending the structured prompt to the LLM, the system first retrieves the most semantically relevant chunks of data related to the submitted query using LangChain's `similarity_search()` method. These retrieved chunks are then included in the prompt provided to the LLM. Finally, we `invoke()` the llm to generate a response, which is displayed in the frontend.

## How to Use
You can submit any questions related to potential cyberattacks or provide network logs to determine whether the incident response assistant detects suspicious activity that may indicate a cyberattack. If malicious activity is identified, the assistant will provide guidance on appropriate mitigation and response steps.

In the query text box, you can also specify the desired length of the response (for example, a detailed multi-page response or a shorter, single-page summary). Keep in mind that longer responses generally take more time to generate.


## Installation

1. Clone the repository:

```bash
git clone <insert SSH URL>
```

2. Navigate to the project directory:

```bash
cd dst_ai_work
```

3. Create a Python virtual environment:

```bash
python3 -m venv .venv
```

4. Activate the virtual environment:

```bash
source .venv/bin/activate
```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Setting up the vector database, LLM models and then starting the application:
```bash
python start.py
```