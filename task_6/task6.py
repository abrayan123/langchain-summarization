# task_6/task6.py
from utils.summarizer import build_summarization_chain


def run_with_memory(memory_type: str, label: str):
    print(f"\n=== Running with {label} ===\n")

    # Build summarization chain with selected memory type
    chain = build_summarization_chain(sentences=3, memory_type=memory_type)

    # --- First text: Machine Learning (100 words) ---
    ml_text = (
        "Machine learning is a field of artificial intelligence that enables computers "
        "to identify patterns and improve their performance based on data. Instead of "
        "being programmed with explicit instructions, these systems learn from examples "
        "and adapt over time. Machine learning powers applications such as spam "
        "filtering, fraud detection, product recommendations, and predictive analytics. "
        "Its ability to analyze vast amounts of information quickly makes it a valuable "
        "tool in industries ranging from healthcare to finance. However, issues like "
        "bias, transparency, and ethical responsibility remain important challenges to "
        "address as adoption continues."
    )
    result1 = chain.invoke({"text": ml_text})
    print("First Summary (Machine Learning):\n")
    print(result1, "\n")

    # --- Second text: Deep Learning (100 words, related) ---
    dl_text = (
        "Deep learning is a specialized branch of machine learning that focuses on using "
        "neural networks with many layers to model highly complex data. These architectures "
        "enable breakthroughs in computer vision, natural language processing, and speech "
        "recognition. For example, deep learning algorithms power facial recognition "
        "systems, virtual assistants, and real-time language translation tools. The strength "
        "of deep learning lies in its ability to automatically extract features from raw "
        "data, reducing the need for manual engineering. Despite its successes, it requires "
        "large amounts of data and computational resources, raising concerns about fairness, "
        "energy consumption, and accessibility."
    )
    result2 = chain.invoke({"text": dl_text})
    print("Second Summary (Deep Learning, considering prior summary):\n")
    print(result2, "\n")


def main():
    # Run with ConversationBufferMemory (last 3 interactions verbatim)
    run_with_memory("buffer", "ConversationBufferMemory")

    # Run with ConversationSummaryMemory (compressed context)
    run_with_memory("summary", "ConversationSummaryMemory")


if __name__ == "__main__":
    main()