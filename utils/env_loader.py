from dotenv import load_dotenv
import os

def load_env_vars():
    load_dotenv()
    return {
        "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
        "endpoint": os.getenv("ENDPOINT_URL"),
        "deployment": os.getenv("DEPLOYMENT_NAME"),
        "embedding_deployment": os.getenv("DEPLOYMENT_EMBEDDING_NAME"),
        "api_version": os.getenv("API_VERSION")
    }
