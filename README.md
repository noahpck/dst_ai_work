# Local RAG-Powered Incident Response Assistant

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

6. Set up the vector database and LLM models:

```bash
python setup.py
```

## Running the Application

After the setup script has finished, start the application:

```bash
python backend/app.py
```

Or, if using the Streamlit interface:

```bash
streamlit run frontend/app_ui.py
```