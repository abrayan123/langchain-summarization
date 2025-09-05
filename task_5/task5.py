# task_5/task5.py
from utils.env_loader import load_env_vars
from utils.tools import (
    build_text_summarizer_tool,
    build_retriever_tool,
    build_word_count_tool,
)
from utils.agents import build_zeroshot_agent


def main():
    # 1) Load env variables
    env = load_env_vars()

    # 2) Build tools
    retriever_tool = build_retriever_tool(
        file_path="task_3/ai_intro.txt",
        env=env,
        name="Retriever",
        description="Retrieves relevant chunks from ai_intro.txt based on query."
    )
    summarizer_tool = build_text_summarizer_tool(
        name="Summarizer",
        sentences=3,
        description="Summarizes retrieved or provided text into exactly 3 sentences."
    )
    word_count_tool = build_word_count_tool(
        name="WordCounter",
        description="Counts words in the given text summary."
    )

    # 3) Build agent with these tools
    agent = build_zeroshot_agent(
        tools=[retriever_tool, summarizer_tool, word_count_tool],
        verbose=True
    )

    # -------- Test 1: Summarize AI breakthroughs --------
    query1 = "Find and summarize text about AI breakthroughs from the document."
    result1 = agent.invoke({"input": query1})
    print("\n=== Test 1: AI Breakthroughs Summary ===\n")
    print(result1["output"].strip(), "\n")

    # -------- Test 2: Summarize + Word Count --------
    query2 = "Find and summarize text about AI breakthroughs and count words in the summary."
    result2 = agent.invoke({"input": query2})
    print("\n=== Test 2: AI Breakthroughs + Word Count ===\n")
    print(result2["output"].strip(), "\n")


if __name__ == "__main__":
    main()
