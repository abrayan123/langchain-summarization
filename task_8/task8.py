import os
from utils.env_loader import load_env_vars
from utils.summarizer import build_json_summarization_chain


def main():
    print("\n=== Task 8: Customizing with Output Parsers ===\n")

    # Test text (~150 words)
    test_text = """
    Artificial Intelligence (AI) applications are becoming increasingly widespread across industries. 
    In healthcare, AI systems assist in diagnosing diseases, predicting patient outcomes, and accelerating 
    drug discovery processes. In finance, AI helps detect fraudulent transactions, automate trading strategies, 
    and assess credit risks. The transportation sector uses AI for optimizing traffic flow, managing logistics, 
    and enabling autonomous driving technologies. In education, AI personalizes learning experiences, evaluates 
    student progress, and provides intelligent tutoring support. Retail businesses rely on AI for customer 
    behavior analysis, demand forecasting, and inventory management. Additionally, AI-powered chatbots are 
    transforming customer service by delivering instant, accurate responses. Despite these advances, challenges 
    such as data privacy, algorithmic bias, and ethical concerns remain significant. Effective regulations and 
    responsible development practices will be crucial to ensure AI applications benefit society while minimizing 
    risks. As AI evolves, its impact on daily life is expected to expand even further.
    """

    # Build JSON summarization chain (3 sentences)
    json_chain = build_json_summarization_chain(sentences=3)

    # Run summarization
    result = json_chain.invoke({"text": test_text})

    print("\n--- JSON Summary Output ---")
    print(result)


if __name__ == "__main__":
    main()
