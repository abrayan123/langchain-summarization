import os
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from utils.env_loader import load_env_vars


def build_summarization_chain(sentences: int = 3):
    """
    Returns a reusable summarization chain.
    This can be imported and reused in later tasks.

    Args:
        sentences (int): Number of sentences for the summary

    Returns:
        RunnableSequence: A chain ready to summarize text
    """
    # Load environment variables into memory
    load_env_vars()

    # Pull values from environment (no hardcoding)
    deployment_name = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")

    llm = AzureChatOpenAI(
        azure_deployment=deployment_name,
        temperature=0
    )

    template = f"""
    You are an expert summarizer.

    Task: Summarize the following text into **exactly {sentences} sentence(s)**.
    - Do not write more or fewer sentences.
    - Each sentence should be concise, factual, and focused.
    - Avoid introductions, commentary, or meta text.

    Text to summarize:
    {{text}}
    """

    prompt = PromptTemplate(template=template, input_variables=["text"])

    return prompt | llm
