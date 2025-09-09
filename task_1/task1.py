from utils.env_loader import load_env_vars
import os

def main():
    # Load variables into memory
    load_env_vars()

    print("Environment Variables Loaded:")

    keys = [
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_API_VERSION",
        "AZURE_OPENAI_CHAT_DEPLOYMENT",
        "AZURE_OPENAI_EMBEDDING_DEPLOYMENT",
    ]

    for key in keys:
        value = os.getenv(key)
        masked = value[:6] + "..." if value else "Not Found"
        print(f"{key}: {masked}")

if __name__ == "__main__":
    main()
