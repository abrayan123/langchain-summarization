from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.env_loader import load_env_vars


def build_summarization_chain(sentences: int = 3) -> LLMChain:
    """
    Returns a reusable summarization chain.
    This can be imported and used in later tasks.
    
    Args:
        sentences (int): number of sentences for the summary
    
    Returns:
        LLMChain: A chain ready to summarize text
    """
    creds = load_env_vars()

    llm = AzureChatOpenAI(
        openai_api_key=creds["api_key"],
        azure_endpoint=creds["endpoint"],
        deployment_name=creds["deployment"],
        openai_api_version=creds["api_version"],
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
