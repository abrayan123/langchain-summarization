# task_10/task10.py

import os
from langchain_community.document_loaders import TextLoader
from langchain.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI

from utils.env_loader import load_env_vars
from utils.summarizer import build_summarization_chain


def build_qa_chain():
    """
    Build a question-answering chain that answers based only on the provided text.
    Returns a runnable chain using LCEL (| operator).
    """
    deployment_name = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")

    llm = AzureChatOpenAI(
        azure_deployment=deployment_name,
        temperature=0
    )

    template = """
    You are an AI assistant. Answer the user's question using ONLY the provided text.

    Text:
    {context}

    Question: {question}

    Answer:
    """
    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )

    # Return LCEL chain: prompt → llm
    return prompt | llm


def main():
    print("\n=== Task 10: Building a Question-Answering Chain on Summaries ===\n")

    # Load environment
    load_env_vars()

    # Load full document (ai_intro.txt)
    loader = TextLoader("task_3/ai_intro.txt", encoding="utf-8")
    docs = loader.load()
    full_text = docs[0].page_content

    # Summarize the document
    summarizer = build_summarization_chain(sentences=5)
    summary_text = summarizer.invoke({"text": full_text})

    # Handle LCEL vs LLMChain return formats
    if isinstance(summary_text, dict) and "text" in summary_text:
        summary_text = summary_text["text"]
    elif hasattr(summary_text, "content"):  # AIMessage
        summary_text = summary_text.content

    print("--- Document Summary ---")
    print(summary_text, "\n")

    # Build QA chain
    qa_chain = build_qa_chain()

    question = "What’s the key event mentioned?"

    # QA on summary
    summary_answer = qa_chain.invoke({
        "context": summary_text,
        "question": question
    })
    if hasattr(summary_answer, "content"):
        summary_answer = summary_answer.content

    # QA on full document
    full_answer = qa_chain.invoke({
        "context": full_text,
        "question": question
    })
    if hasattr(full_answer, "content"):
        full_answer = full_answer.content

    print("--- Q&A on Summary ---")
    print(summary_answer, "\n")

    print("--- Q&A on Full Document ---")
    print(full_answer, "\n")

    print("=== Comparison ===")
    print("- Summary-based QA → usually more concise but may miss details.")
    print("- Full-text QA → more accurate, but may include unnecessary context.")


if __name__ == "__main__":
    main()
