# task_11/task11.py
from utils.tools import (
    build_text_summarizer_tool,
    build_date_tool,
    build_mock_web_search_tool,
)
from utils.agents import build_zeroshot_agent


def main():

    # 1) Build tools
    summarizer_tool = build_text_summarizer_tool(
        name="Summarizer",
        sentences=3,
        description="Summarizes provided text into exactly 3 sentences."
    )
    date_tool = build_date_tool(
        name="DateFetcher",
        description="Fetches today’s current date."
    )
    mock_search_tool = build_mock_web_search_tool(
        name="MockWebSearch",
        description="Performs a simulated web search and returns a static response."
    )

    # 2) Build agents with different tool sets
    agent_with_date = build_zeroshot_agent(
        tools=[summarizer_tool, date_tool],
        verbose=True
    )

    agent_with_search = build_zeroshot_agent(
        tools=[summarizer_tool, mock_search_tool],
        verbose=True
    )

    # -------- Test 1: Summarization + Date --------
    ai_text = (
        "Artificial intelligence (AI) is rapidly transforming industries by "
        "enabling automation, personalization, and efficiency. In healthcare, "
        "AI assists with diagnostics and patient care. In finance, it supports "
        "fraud detection and trading. In transportation, self-driving cars are "
        "becoming more reliable. Ethical concerns remain around fairness, bias, "
        "and transparency. Policymakers, researchers, and companies continue to "
        "debate frameworks for safe and responsible AI development worldwide."
    )

    query1 = "Summarize this 100-word text about AI and tell me today’s date."
    result1 = agent_with_date.invoke({"input": f"{query1}\n\n{ai_text}"})
    print("\n=== Test 1: Summarize + Date ===\n")
    print(result1["output"].strip(), "\n")

    # -------- Test 2: Summarization + Mock Search --------
    query2 = "Summarize AI trends and search for recent updates."
    result2 = agent_with_search.invoke({"input": query2})
    print("\n=== Test 2: Summarize + Mock Web Search ===\n")
    print(result2["output"].strip(), "\n")


if __name__ == "__main__":
    main()
