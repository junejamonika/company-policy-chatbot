from config import PDF_PATH

from ingestion.loader import load_document
from ingestion.splitter import split_documents
from ingestion.embedder import get_embeddings
from ingestion.vectorstore import create_vector_store


def main():
    # Load the document
    print(f"Loading document from {PDF_PATH}...")
    documents = load_document(PDF_PATH)
    # Split the documents into chunks
    print("Splitting documents into chunks...")
    chunks = split_documents(documents)
    # Create embeddings
    print("Creating embeddings for chunks...")
    embeddings = get_embeddings()
    # Create the vector store
    print("Creating vector store...")
    vector_store = create_vector_store(chunks, embeddings)
    print("Ingestion completed successfully.")

if __name__ == "__main__":
    main()
