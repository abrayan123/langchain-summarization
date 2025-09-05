# task_4/task4.py
from utils.env_loader import load_env_vars
from utils.tools import build_text_summarizer_tool
from utils.agents import build_zeroshot_agent


def main():
    # 1) Load environment (Azure config) from .env
    load_env_vars()

    # 2) Build summarization tool (reusing Task 2 chain)
    summarizer_tool = build_text_summarizer_tool(
        name="TextSummarizer",
        sentences=3,
        description="Summarizes input text into exactly 3 sentences."
    )

    # 3) Build zero-shot agent with this tool
    agent = build_zeroshot_agent(tools=[summarizer_tool], verbose=False)

    # -------- Test 1: Specific summarization request --------
    healthcare_text = (
        "Artificial Intelligence is transforming healthcare by improving diagnostics, "
        "personalizing treatment, and streamlining hospital operations. AI systems can "
        "analyze medical images more accurately than humans in some cases, leading to "
        "earlier detection of diseases such as cancer. In addition, predictive models "
        "help anticipate patient needs, while chatbots improve patient engagement. "
        "However, challenges remain around data privacy, trust, and ensuring fairness "
        "in AI-driven decision-making."
    )

    prompt1 = (
        "Use the TextSummarizer tool.\n"
        "Summarize the impact of AI on healthcare into exactly 3 sentences.\n\n"
        f"{healthcare_text}"
    )
    result1 = agent.invoke({"input": prompt1})
    print("=== Test 1: Healthcare Summary (3 sentences) ===\n")
    print(result1["output"].strip(), "\n")

    # -------- Test 2: Vague request --------
    prompt2 = "Summarize something interesting."
    # Agent will decide to use TextSummarizer, but there is no content. It may ask for (or invent) content.
    # This is intentional: we want to observe the agent's behavior with a vague request.
    result2 = agent.invoke({"input": prompt2})
    print("=== Test 2: Vague Request Output ===\n")
    print(result2["output"].strip(), "\n")


if __name__ == "__main__":
    main()
