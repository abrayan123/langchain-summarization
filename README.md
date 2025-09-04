# langchain-summarization

# LangChain Summarization ProjectA project to master LangChain through structured tasks. Contributor: - Ayan Bin Rizwan


## Completed Tasks

### Task 1: Setup LangChain Environment
- Created and activated Python virtual environment  
- Added `.gitignore` and `.env` for security  
- Implemented reusable `env_loader` for Azure credentials  
- Tested environment variable loading via `task1.py`  

### Task 2: Building a Basic Summarization Chain
- Implemented `utils/summarizer.py` to build a reusable summarization chain.
- Configured Azure OpenAI model with environment variables.
- Tested chain with a 200-word paragraph about AI:
  - 3-sentence summary
  - 1-sentence summary
- Output demonstrates flexible summarization length.
