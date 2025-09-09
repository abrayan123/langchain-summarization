from utils.summarizer import build_summarization_chain
from utils.retriever import build_retriever

def main():
    retriever = build_retriever("task_3/ai_intro.txt")

    query = "AI milestones"
    retrieved_docs = retriever.invoke(query)

    print("\n📌 Retrieved Chunks:")
    for i, doc in enumerate(retrieved_docs, 1):
        print(f"\n--- Chunk {i} ---")
        print(doc.page_content)

    combined_text = " ".join([doc.page_content for doc in retrieved_docs])
    print("\n📌 Complete Retrieved Text:")
    print(combined_text)

    summarizer = build_summarization_chain(sentences=3)
    summary = summarizer.invoke({"text": combined_text}).content

    print("\n📌 Summary:")
    print(summary)

if __name__ == "__main__":
    main()
