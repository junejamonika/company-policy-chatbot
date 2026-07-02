from langchain_chroma import Chroma

from config import COLLECTION_NAME
from ingestion.embedder import get_embeddings

def get_vectorstore():
    """Get the vectorstore."""
    embeddings = get_embeddings()
    vectorstore = Chroma(
        persist_directory="db", 
        embedding_function=embeddings, 
        collection_name=COLLECTION_NAME
    )

    print(vectorstore._collection.count())

    return vectorstore

def get_retriever():
    vectorstore = get_vectorstore()

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 4
        }
    )

    return retriever