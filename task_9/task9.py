# task_9/task9.py

import os
from utils.env_loader import load_env_vars
from utils.retriever import build_retriever, build_multiquery_retriever
from utils.summarizer import build_summarization_chain


def main():
    print("\n=== Task 9: Experimenting with Multi-Query Retrieval ===\n")

    # Load environment variables
    load_env_vars()

    # Path to ai_intro.txt (created in Task 3)
    file_path = os.path.join("task_3", "ai_intro.txt")

    # --- Single-query retriever ---
    print("--- Using Single-Query Retriever ---")
    retriever = build_retriever(file_path, source_type="text")
    docs_single = retriever.invoke("AI advancements")

    chain = build_summarization_chain(sentences=3)
    single_summary = chain.invoke({"text": " ".join([doc.page_content for doc in docs_single])}).content

    print("\nSingle-query Summary:\n", single_summary, "\n")

    # --- Multi-query retriever ---
    print("--- Using Multi-Query Retriever ---")
    multi_retriever = build_multiquery_retriever(file_path, source_type="text", num_queries=3)

    # Generate alternate queries (directly from llm_chain)
    queries = multi_retriever.llm_chain.invoke("AI advancements")
    print("\nGenerated Alternate Queries:")
    for i, q in enumerate(queries, 1):
        print(f"Query {i}: {q}")

    # Fetch documents for each query separately (to inspect chunks)
    print("\nRetrieved Chunks Per Query:")
    for i, q in enumerate(queries, 1):
        docs = multi_retriever.retriever.invoke(q) 
        print(f"\n--- Chunks for Query {i}: {q} ---")
        for j, doc in enumerate(docs, 1):
            print(f"Chunk {j}: {doc.page_content[:200]}...\n")

    # Get combined retrieval (default behavior)
    docs_multi = multi_retriever.invoke("AI advancements")
    multi_summary = chain.invoke({"text": " ".join([doc.page_content for doc in docs_multi])}).content

    print("\nMulti-query Summary:\n", multi_summary, "\n")


if __name__ == "__main__":
    main()
