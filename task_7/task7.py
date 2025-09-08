"""
Task 7: Leveraging Document Loaders for Diverse Sources
"""

from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS  
from langchain_openai import AzureOpenAIEmbeddings
from utils.summarizer import build_summarization_chain
from utils.env_loader import load_env_vars


def load_pdf(path: str):
    loader = PyPDFLoader(path)
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=150, chunk_overlap=30)
    return splitter.split_documents(docs)


def load_web(url: str):
    loader = WebBaseLoader(url)
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=150, chunk_overlap=30)
    return splitter.split_documents(docs)


def build_vector_store(chunks):
    """Create a FAISS vector store with Azure OpenAI embeddings."""
    creds = load_env_vars()

    embeddings = AzureOpenAIEmbeddings(
        api_key=creds["api_key"],
        azure_endpoint=creds["endpoint"],
        deployment=creds["embedding_deployment"],   # ✅ DEPLOYMENT_EMBEDDING_NAME from .env
        openai_api_version=creds["api_version"]
    )

    return FAISS.from_documents(chunks, embeddings)


def summarize_query(store, query: str):
    results = store.similarity_search(query, k=3)
    combined_text = " ".join([r.page_content for r in results])
    chain = build_summarization_chain(sentences=3)
    return chain.invoke(combined_text).content


def main():
    print("\n=== Task 7: Document Loader Summarization ===\n")

    pdf_chunks = load_pdf("task_7/ai_ethics.pdf")
    pdf_store = build_vector_store(pdf_chunks)
    
    web_chunks = load_web("https://www.ibm.com/think/topics/ai-ethics")
    web_store = build_vector_store(web_chunks)

    query = "AI challenges"
    pdf_summary = summarize_query(pdf_store, query)
    web_summary = summarize_query(web_store, query)

    print("\n--- PDF Summary ---")
    print(pdf_summary)

    print("\n--- Web Summary ---")
    print(web_summary)


if __name__ == "__main__":
    main()
