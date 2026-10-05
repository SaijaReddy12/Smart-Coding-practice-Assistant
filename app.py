import os
import shutil
import streamlit as st

from document_processor import process_pdf
from rag_pipeline import rag_pipeline
from config import DATA_FOLDER, VECTORSTORE_FOLDER


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="Smart Coding Practice Assistant",
    page_icon="💻",
    layout="wide"
)


# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title("💻 Smart Coding Practice Assistant")

st.write(
    "Practice programming concepts and coding problems "
    "using your own study material with RAG and Ollama."
)


# -------------------------------------------------
# CREATE REQUIRED FOLDERS
# -------------------------------------------------

os.makedirs(DATA_FOLDER, exist_ok=True)
os.makedirs(VECTORSTORE_FOLDER, exist_ok=True)


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:

    st.header("📚 Study Material")

    uploaded_file = st.file_uploader(
        "Upload a coding PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        if st.button("📥 Process PDF"):

            pdf_path = os.path.join(
                DATA_FOLDER,
                uploaded_file.name
            )

            with open(pdf_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            with st.spinner("Processing PDF..."):

                try:

                    pages, chunks = process_pdf(pdf_path)

                    st.success(
                        "Document processed successfully!"
                    )

                    st.info(
                        f"Pages: {pages}\n\n"
                        f"Chunks: {chunks}"
                    )

                except Exception as e:

                    st.error(
                        f"Error while processing PDF:\n{e}"
                    )


    st.divider()

    st.header("⚙️ Project")

    if st.button("🗑️ Reset Knowledge Base"):

        try:

            if os.path.exists(VECTORSTORE_FOLDER):
                shutil.rmtree(VECTORSTORE_FOLDER)

            os.makedirs(
                VECTORSTORE_FOLDER,
                exist_ok=True
            )

            st.success(
                "Knowledge base reset successfully."
            )

        except Exception as e:

            st.error(
                f"Reset error: {e}"
            )


# -------------------------------------------------
# MAIN CHAT AREA
# -------------------------------------------------

st.subheader("🤖 Ask the Coding Assistant")

question = st.text_area(
    "Enter your coding question:",
    placeholder=(
        "Example: Explain inheritance in Java "
        "or help me understand this Python concept."
    ),
    height=120
)


# -------------------------------------------------
# ASK BUTTON
# -------------------------------------------------

if st.button("🚀 Ask Assistant"):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Searching study material and generating answer..."
        ):

            try:

                answer, documents = rag_pipeline(
                    question
                )

                st.markdown("## 💡 Answer")

                st.markdown(answer)

                # ----------------------------------
                # RETRIEVED INFORMATION
                # ----------------------------------

                with st.expander(
                    "🔎 View Retrieved Sources"
                ):

                    if documents:

                        for i, doc in enumerate(
                            documents,
                            start=1
                        ):

                            st.markdown(
                                f"### Source {i}"
                            )

                            page_number = doc.metadata.get(
                                "page",
                                "Unknown"
                            )

                            st.caption(
                                f"Page: {page_number}"
                            )

                            st.write(
                                doc.page_content
                            )

                            st.divider()

                    else:

                        st.write(
                            "No sources were retrieved."
                        )

            except Exception as e:

                st.error(
                    "Unable to generate an answer."
                )

                st.exception(e)


# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.divider()

st.caption(
    "Smart Coding Practice Assistant | "
    "RAG + LangChain + Ollama + ChromaDB"
)