import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

from config import (
    OLLAMA_BASE_URL,
    OLLAMA_EMBEDDING_MODEL,
    VECTORSTORE_FOLDER,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


def process_pdf(pdf_path):

    print("Loading PDF...")

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    print(f"Pages loaded: {len(documents)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)

    print(f"Chunks created: {len(chunks)}")

    embeddings = OllamaEmbeddings(
        model=OLLAMA_EMBEDDING_MODEL,
        base_url=OLLAMA_BASE_URL
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTORSTORE_FOLDER,
        collection_name="coding_documents"
    )

    print("Documents stored successfully.")

    return len(documents), len(chunks)


def get_vectorstore():

    embeddings = OllamaEmbeddings(
        model=OLLAMA_EMBEDDING_MODEL,
        base_url=OLLAMA_BASE_URL
    )

    vectorstore = Chroma(
        persist_directory=VECTORSTORE_FOLDER,
        embedding_function=embeddings,
        collection_name="coding_documents"
    )

    return vectorstore