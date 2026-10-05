import os
from dotenv import load_dotenv

load_dotenv()

# Ollama configuration
OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2"
)

OLLAMA_EMBEDDING_MODEL = os.getenv(
    "OLLAMA_EMBEDDING_MODEL",
    "nomic-embed-text"
)

# Project folders
DATA_FOLDER = "data"
VECTORSTORE_FOLDER = "vectorstore"

# RAG settings
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

TOP_K = 4