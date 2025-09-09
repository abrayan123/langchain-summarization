# langchain-summarization

# LangChain Summarization ProjectA project to master LangChain through structured tasks. Contributor: - Ayan Bin Rizwan


## Completed Tasks


## Task 1: Setup LangChain Environment

- ✅ Created and activated a Python virtual environment  
- ✅ Added `.gitignore` to exclude sensitive files (e.g., `.env`, `__pycache__`, `venv/`)  
- ✅ Configured `.env` to securely store Azure OpenAI credentials  
- ✅ Implemented a reusable `env_loader.py` to manage environment variables  
- ✅ Verified environment setup by printing masked variables in `task1.py`



## Task 2: Building a Basic Summarization Chain

- Implemented `utils/summarizer.py` to build a **reusable summarization chain**.  
- Configured Azure OpenAI model with **environment variables** (API key, endpoint, deployment, version).  
- Designed a flexible prompt template that ensures summaries are generated in the requested number of sentences.  
- Tested the chain with a ~200-word paragraph about Artificial Intelligence.  

---

### 🔹 Original Text

Artificial intelligence (AI) is the simulation of human intelligence in machines that are programmed to think and learn. These systems can perform tasks such as problem-solving, decision-making, language understanding, and pattern recognition.  

Over the years, AI has evolved from simple rule-based systems to complex neural networks capable of deep learning. Today, AI is applied across industries including healthcare, finance, education, and manufacturing.  

In healthcare, AI assists in diagnosing diseases and personalizing treatment plans. In finance, it detects fraud and powers algorithmic trading.  

However, the rapid development of AI also raises concerns regarding ethics, privacy, and potential job displacement. Governments and organizations are working to create regulations and frameworks to ensure AI is developed responsibly.  

Despite the challenges, the future of AI promises significant advancements that could transform daily life, improve efficiency, and unlock new possibilities for innovation.  

---

### 🔹 3-Sentence Summary

Artificial intelligence (AI) simulates human intelligence in machines, enabling them to learn and solve problems.  

It is being applied across various industries, including healthcare, finance, and manufacturing, while also raising ethical and privacy concerns.  

Efforts are underway by governments and organizations to create policies that promote responsible AI development and ensure beneficial collaboration between humans and machines.  

---

### 🔹 1-Sentence Summary

Artificial intelligence (AI) simulates human intelligence in machines, evolving across various industries to enhance capabilities like learning and problem-solving, while also raising ethical concerns that necessitate responsible development frameworks.  

---

✅ **Output demonstrates flexible summarization length** (3 vs 1 sentence) and validates the reusable summarizer design for later tasks.


