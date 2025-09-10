import os
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain.chains import LLMChain
from langchain.schema.runnable import RunnableLambda
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from utils.env_loader import load_env_vars


# Load environment variables into memory
load_env_vars()

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


def build_json_summarization_chain(sentences: int = 3):
    """
    Extends the summarization chain to return JSON output
    with 'summary' and 'length' fields.

    Args:
        sentences (int): Number of sentences for the summary.

    Returns:
        Runnable: Summarization chain that outputs JSON.
    """
    # Base summarizer (no memory) → reuse existing function
    base_chain = build_summarization_chain(sentences=sentences)

    # Define JSON response schema
    response_schemas = [
        ResponseSchema(
            name="summary",
            description="The summarized text"
        ),
        ResponseSchema(
            name="length",
            description="Character count of the summary"
        )
    ]
    parser = StructuredOutputParser.from_response_schemas(response_schemas)

    # Add JSON formatting instructions
    format_instructions = parser.get_format_instructions()

    # Wrap existing summarizer with JSON prompt
    json_prompt = PromptTemplate(
        template=f"""
        You are an expert summarizer.

        Task: Summarize the following text into **exactly {sentences} sentence(s)**.
        - Do not write more or fewer sentences.
        - Be concise, factual, and focused.
        - Output must be in valid JSON format.

        Formatting instructions:
        {{format_instructions}}

        Text to summarize:
        {{text}}
        """,
        input_variables=["text"],
        partial_variables={"format_instructions": format_instructions}
    )

    # Reuse LLM from the base chain
    if hasattr(base_chain, "llm"):
        llm = base_chain.llm
    else:
        # Fallback: base_chain is a Runnable (PromptTemplate | LLM)
        llm = AzureChatOpenAI(
            azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
            temperature=0
        )

    # Final chain: json_prompt → llm → parser
    return json_prompt | llm | parser
