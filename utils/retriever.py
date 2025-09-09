from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import AzureOpenAIEmbeddings

def build_retriever(file_path: str, env: dict):
    # Load the text file
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()

    # Split into smaller chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )
    chunks = splitter.split_documents(documents)

    # Use dedicated embedding deployment
    embeddings = AzureOpenAIEmbeddings(
        azure_endpoint=env["endpoint"],
        deployment=env["embedding_deployment"],
        api_version=env["api_version"],
        api_key=env["api_key"],
    )

    # Build FAISS vectorstore
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore.as_retriever()
