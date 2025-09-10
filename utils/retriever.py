import os
from utils.env_loader import load_env_vars
from langchain_community.document_loaders import TextLoader, PyPDFLoader, WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import AzureOpenAIEmbeddings

def build_retriever(source: str, source_type: str = "text", chunk_size: int = 200, overlap: int = 20):
    """
    Build retriever for text, pdf, or web documents.

    Args:
        source (str): path to file or URL
        source_type (str): one of {"text", "pdf", "web"}
        chunk_size (int): chunk size for splitting
        overlap (int): chunk overlap

    Returns:
        retriever object
    """
    load_env_vars()

    # Select loader
    if source_type == "text":
        loader = TextLoader(source, encoding="utf-8")
    elif source_type == "pdf":
        loader = PyPDFLoader(source)
    elif source_type == "web":
        loader = WebBaseLoader(source)
    else:
        raise ValueError(f"Unsupported source_type: {source_type}")

    documents = loader.load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )
    chunks = splitter.split_documents(documents)

    # Embeddings from Azure
    deployment_name = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
    
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=deployment_name
    )

    # Vector store
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore.as_retriever()
