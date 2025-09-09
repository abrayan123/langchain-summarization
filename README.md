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



## Task 3: Exploring Retrievers with Summarization

For this task, we created a 500-word sample text file (`ai_intro.txt`) and used LangChain’s `TextLoader` to load the file. The text was then split into smaller chunks using `RecursiveCharacterTextSplitter`. We stored the embeddings in an in-memory FAISS vector store using `AzureOpenAIEmbeddings`, built a retriever, and queried it with the term **"AI milestones"**. The retrieved text was then passed to our summarization chain from Task 2 to generate a summary.

#### Output

$ python -m task_3.task3

📌 **Retrieved Chunks:**

--- **Chunk 1** ---  
From its early theoretical roots to its modern-day applications, the history of AI is a story of cycles of optimism, setbacks, and breakthroughs. Each era has contributed key milestones that have  

--- **Chunk 2** ---  
AI quickly spread across industries, revolutionizing healthcare, finance, transportation, and entertainment. Virtual assistants like Siri, Alexa, and Google Assistant became household names, while  

--- **Chunk 3** ---  
that have brought us closer to machines capable of augmenting human intelligence. As AI continues to advance, its history reminds us that progress often comes in waves, shaped by innovation,  

--- **Chunk 4** ---  
names, while self-driving car research advanced rapidly. In healthcare, AI-assisted diagnostics began improving accuracy in detecting diseases like cancer from medical images. In business, AI tools  

📌 **Complete Retrieved Text:**  

From its early theoretical roots to its modern-day applications, the history of AI is a story of cycles of optimism, setbacks, and breakthroughs. Each era has contributed key milestones that have.  

AI quickly spread across industries, revolutionizing healthcare, finance, transportation, and entertainment. Virtual assistants like Siri, Alexa, and Google Assistant became household names, while.  

That have brought us closer to machines capable of augmenting human intelligence. As AI continues to advance, its history reminds us that progress often comes in waves, shaped by innovation.  

Names, while self-driving car research advanced rapidly. In healthcare, AI-assisted diagnostics began improving accuracy in detecting diseases like cancer from medical images. In business, AI tools.  

📌 **Summary:**  

The history of AI is marked by cycles of optimism, setbacks, and breakthroughs, leading to significant advancements across various industries.  

Key milestones include the rise of virtual assistants and improvements in healthcare diagnostics, particularly in detecting diseases like cancer.  

As AI technology continues to evolve, it highlights the ongoing interplay between innovation and practical applications.


