"""
Task 7: Leveraging Document Loaders for Diverse Sources
"""

from utils.retriever import build_retriever
from utils.summarizer import build_summarization_chain


def summarize_query(retriever, query: str):
    # Retrieve relevant chunks
    results = retriever.invoke(query)

    print("\n--- Retrieved Chunks ---")
    for i, doc in enumerate(results, start=1):
        print(f"\n[Chunk {i}]\n{doc.page_content}\n")

    # Combine into one text
    combined_text = " ".join([r.page_content for r in results])

    # Run summarization chain
    chain = build_summarization_chain(sentences=3)
    return chain.invoke({"text": combined_text}).content 


def main():
    print("\n=== Task 7: Document Loader Summarization ===\n")

    # Build retrievers for PDF and Web
    pdf_retriever = build_retriever("task_7/ai_ethics.pdf", source_type="pdf", chunk_size=150, overlap=30)
    web_retriever = build_retriever("https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence", source_type="web", chunk_size=150, overlap=30)

    query = "AI challenges"

    # Summarize results
    pdf_summary = summarize_query(pdf_retriever, query)
    web_summary = summarize_query(web_retriever, query)

    print("\n--- PDF Summary ---")
    print(pdf_summary)

    print("\n--- Web Summary ---")
    print(web_summary)


if __name__ == "__main__":
    main()
