from utils.env_loader import load_env_vars
from utils.summarizer import build_summarization_chain
from utils.retriever import build_retriever

def main():
    # Load environment variables
    env = load_env_vars()

    # Build retriever on ai_intro.txt
    retriever = build_retriever("task_3/ai_intro.txt", env)

    # Query retriever
    query = "AI milestones"
    retrieved_docs = retriever.invoke(query)

    # Show each retrieved chunk separately
    print("\n📌 Retrieved Chunks:")
    for i, doc in enumerate(retrieved_docs, 1):
        print(f"\n--- Chunk {i} ---")
        print(doc.page_content)

    # Combine retrieved text
    combined_text = " ".join([doc.page_content for doc in retrieved_docs])

    # Show complete retrieved text
    print("\n📌 Complete Retrieved Text:")
    print(combined_text)

    # Summarize retrieved text
    summarizer = build_summarization_chain(sentences=3)
    summary = summarizer.invoke({"text": combined_text}).content

    print("\n📌 Summary:")
    print(summary)

if __name__ == "__main__":
    main()
