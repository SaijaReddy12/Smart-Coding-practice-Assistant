# Smart Coding Practice Assistant

A RAG-based coding practice assistant built using:

- Python
- Streamlit
- LangChain
- Ollama
- ChromaDB
- PDF documents

## Project Flow

PDF
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
ChromaDB
↓
Question
↓
Similarity Search
↓
Relevant Context
↓
Ollama
↓
Answer


## Installation

Create a virtual environment:

python -m venv venv


Activate it:

.\venv\Scripts\Activate.ps1


Install requirements:

python -m pip install -r requirements.txt


## Ollama

Install Ollama on your computer.

Pull the language model:

ollama pull llama3.2


Pull the embedding model:

ollama pull nomic-embed-text


Check Ollama:

ollama list


## Run the Application

Start Streamlit:

python -m streamlit run app.py


The application will open in your browser.


## How to Use

1. Start Ollama.
2. Run the Streamlit application.
3. Upload a coding PDF.
4. Click Process PDF.
5. Enter a coding question.
6. Click Ask Assistant.
7. The system retrieves relevant information.
8. Ollama generates the answer.


## Main Components

app.py
---------
Streamlit user interface.


document_processor.py
---------------------
Loads PDFs, splits text into chunks,
creates embeddings and stores them in ChromaDB.


rag_pipeline.py
---------------
Retrieves relevant chunks and sends them
to the Ollama language model.


config.py
---------
Contains project configuration.


.env
----
Contains Ollama configuration.