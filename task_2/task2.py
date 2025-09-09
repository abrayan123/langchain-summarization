from utils.summarizer import build_summarization_chain


def main():
    test_text = (
        "Artificial intelligence (AI) refers to the simulation of human intelligence in machines "
        "that are programmed to think like humans and mimic their actions. The term may also be "
        "applied to any machine that exhibits traits associated with a human mind such as learning "
        "and problem-solving. AI is continuously evolving to benefit many different industries. "
        "Machines are wired using a cross-disciplinary approach based on mathematics, computer science, "
        "linguistics, psychology, and more. Advances in machine learning and deep learning are creating "
        "a paradigm shift in virtually every sector of the tech industry. AI applications include "
        "expert systems, natural language processing, speech recognition, and machine vision. "
        "Healthcare uses AI to analyze complex medical data, finance uses AI to detect fraud, "
        "and manufacturing uses AI to optimize production lines. Despite these benefits, AI also raises "
        "concerns about ethics, privacy, and the potential loss of jobs. Governments and organizations "
        "are now working on policies and frameworks to ensure responsible AI development. "
        "The goal is to harness AI’s potential while addressing its risks, shaping a future where humans "
        "and intelligent machines collaborate for positive outcomes."
    )

    # 3-sentence summary
    summarizer_3 = build_summarization_chain(sentences=3)
    summary_3 = summarizer_3.invoke({"text": test_text}).content
    print("3-Sentence Summary:\n", summary_3, "\n")

    # 1-sentence summary
    summarizer_1 = build_summarization_chain(sentences=1)
    summary_1 = summarizer_1.invoke({"text": test_text}).content
    print("1-Sentence Summary:\n", summary_1)


if __name__ == "__main__":
    main()