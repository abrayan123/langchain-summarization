import os
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain.chains import LLMChain  # still useful for memory
from utils.env_loader import load_env_vars


def build_summarization_chain(sentences: int = 3, memory_type: str | None = None):
    """
    Returns a reusable summarization chain, optionally with memory.
    This can be imported and reused in later tasks.

    Args:
        sentences (int): Number of sentences for the summary.
        memory_type (str | None): Type of memory to use. Options:
            - "buffer": ConversationBufferMemory
            - "summary": ConversationSummaryMemory
            - None: No memory

    Returns:
        Chain: A chain ready to summarize text.
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
    - If prior conversation exists, consider it while generating the new summary.

    Text to summarize:
    {{text}}
    """

    prompt = PromptTemplate(template=template, input_variables=["text"])

    # Optional memory integration (requires LLMChain wrapper)
    if memory_type == "buffer":
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            input_key="text",
            k=3,  # last 3 interactions
            return_messages=True
        )
        return LLMChain(llm=llm, prompt=prompt, memory=memory, verbose=True)

    elif memory_type == "summary":
        memory = ConversationSummaryMemory(
            memory_key="chat_history",
            input_key="text",
            llm=llm,
            return_messages=True
        )
        return LLMChain(llm=llm, prompt=prompt, memory=memory, verbose=True)

    # No memory → use LCEL chaining with "|"
    return prompt | llm
