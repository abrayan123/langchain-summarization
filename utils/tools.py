# utils/tools.py
from langchain.agents import Tool
from utils.summarizer import build_summarization_chain
from utils.retriever import build_retriever


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


def build_retriever_tool(
    file_path: str,
    env: dict,
    name: str = "TextRetriever",
    description: str | None = None,
) -> Tool:
    """Wrap Task 3 retriever as a LangChain Tool."""
    retriever = build_retriever(file_path, env)

    if description is None:
        description = (
            "Retrieves relevant chunks from a document based on a query. "
            "Input: a search query string. Output: retrieved text passages."
        )

    def _retrieve(query: str) -> str:
        docs = retriever.invoke(query)
        return "\n\n".join([doc.page_content for doc in docs])

    return Tool(name=name, func=_retrieve, description=description)


def build_word_count_tool(
    name: str = "WordCounter",
    description: str | None = None,
) -> Tool:
    """Simple tool to count words in a given text."""
    if description is None:
        description = "Counts the number of words in the given text string."

    def _count_words(text: str) -> str:
        count = len(text.split())
        return f"Word count: {count}"

    return Tool(name=name, func=_count_words, description=description)
