from langchain_community.document_loaders import PyMuPDFLoader


def load_document(file_path: str):
    """
    Load a document using PyMuPDFLoader.

    Args:
        file_path (str): The path to the document file.

    Returns:
        list: A list of documents loaded from the file.
    """
    loader = PyMuPDFLoader(file_path)
    documents = loader.load()

    print(f"Loaded {len(documents)} documents from {file_path}.")

    return documents