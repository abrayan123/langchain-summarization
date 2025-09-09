# utils/tools.py
from langchain.agents import Tool
from utils.summarizer import build_summarization_chain

def build_text_summarizer_tool(
    name: str = "TextSummarizer",
    sentences: int = 3,
    description: str | None = None,
) -> Tool:
    """Return a LangChain Tool that summarizes text via the Task 2 chain."""
    chain = build_summarization_chain(sentences=sentences)

    if description is None:
        description = (
            f"Summarizes input text into exactly {sentences} sentence(s). "
            "Input: plain text. Output: summary as a string."
        )

    def _summarize(text: str) -> str:
        return chain.invoke({"text": text})

    return Tool(name=name, func=_summarize, description=description)