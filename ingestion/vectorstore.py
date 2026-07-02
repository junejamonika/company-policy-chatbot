from langchain_chroma import Chroma

from config import (
    CHROMA_DB_DIR,
    COLLECTION_NAME,
)


def create_vector_store(chunks, embeddings):

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR,
        collection_name=COLLECTION_NAME,
    )

    print("Vector database created")

    return vector_db