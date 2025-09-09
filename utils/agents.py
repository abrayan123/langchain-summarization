import os
from utils.env_loader import load_env_vars
from langchain_openai import AzureChatOpenAI
from langchain.agents import initialize_agent
from typing import Sequence

def build_zeroshot_agent(tools: Sequence, verbose: bool = False):
    """
    Build a zero-shot-react-description agent with AzureChatOpenAI and provided tools.
    Env is loaded via utils.env_loader.
    """
    load_env_vars()
    
    deployment_name = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")

    llm = AzureChatOpenAI(
        azure_deployment=deployment_name,
        temperature=0
    )
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=verbose,
        handle_parsing_errors=True,
    )
    return agent