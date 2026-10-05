from langchain_ollama import ChatOllama

from document_processor import get_vectorstore
from config import (
    OLLAMA_MODEL,
    OLLAMA_BASE_URL,
    TOP_K
)


def rag_pipeline(question):

    vectorstore = get_vectorstore()

    # Retrieve relevant coding information
    documents = vectorstore.similarity_search(
        question,
        k=TOP_K
    )

    if not documents:
        return (
            "I could not find relevant information in the uploaded "
            "coding material.",
            []
        )

    # Combine retrieved information
    context = "\n\n".join(
        [
            f"Source {i + 1}:\n{doc.page_content}"
            for i, doc in enumerate(documents)
        ]
    )

    prompt = f"""
You are a Smart Coding Practice Assistant.

Use the retrieved study material below to answer the user's question.

Retrieved study material:
-------------------------
{context}
-------------------------

User question:
{question}

Instructions:

1. Explain the concept clearly.
2. Use simple language suitable for a B.Tech student.
3. If the question asks for code, provide correct code.
4. Explain important parts of the code.
5. If debugging is requested, identify the error and explain the correction.
6. If the retrieved material does not contain enough information, clearly say so.
7. Do not invent information from the retrieved material.
8. Keep the answer organized with headings where useful.
"""

    llm = ChatOllama(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=0.2
    )

    response = llm.invoke(prompt)

    answer = response.content

    return answer, documents