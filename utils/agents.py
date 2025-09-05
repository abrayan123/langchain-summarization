import os
from langchain_openai import AzureChatOpenAI
from langchain.agents import initialize_agent
from typing import Sequence

def build_zeroshot_agent(tools: Sequence, verbose: bool = False):
    """
    Build a zero-shot-react-description agent with AzureChatOpenAI and provided tools.
    Env is loaded via utils.env_loader in callers.
    """
    llm = AzureChatOpenAI(
        azure_endpoint=os.getenv("ENDPOINT_URL"),
        deployment_name=os.getenv("DEPLOYMENT_NAME"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("API_VERSION"),  # <-- added fix
    )

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=verbose,
        handle_parsing_errors=True,
    )
    return agent
