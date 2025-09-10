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



## Task 4 – Creating an Agent for Summarization

In this task, we introduced the **concept of tools and agents** in LangChain.  
Unlike Task 3, where we explicitly combined a retriever with the summarizer, Task 4 demonstrates how an **agent can autonomously decide which tools to use** based on the user’s request.  

We first defined a custom tool called **“TextSummarizer”**, which wrapped around our summarization chain from Task 2. This tool was given a clear description that explained its purpose — to summarize input text into exactly three sentences.  

Next, we initialized a **zero-shot-react-description agent** using `AzureChatOpenAI`. The agent was provided with the summarizer tool and could decide on its own when to call it. This setup showed how LangChain’s agent framework can make interactions more flexible, since the agent interprets user intent and dynamically selects the right tool to respond.

This task demonstrated the advantage of using agents:  
- Instead of chaining tools manually, the agent is empowered to reason about vague or broad instructions.  
- It can still rely on the summarizer tool when summarization is explicitly or implicitly required.  
- This makes the system more **generalizable and adaptable to future use cases**.  

**Example Output:**  

Test 1 – Healthcare Summary (3 sentences):  
Artificial Intelligence is enhancing healthcare through improved diagnostics, personalized treatment, and efficient hospital operations. AI can analyze medical images with greater accuracy than humans, facilitating earlier disease detection, while predictive models and chatbots enhance patient engagement and anticipate needs. Despite these advancements, challenges related to data privacy, trust, and fairness in AI decision-making persist.  

Test 2 – Vague Request:  
Recent discoveries in the Amazon rainforest have uncovered many new species of plants and animals, emphasizing its rich biodiversity. These findings underscore the necessity of conserving the ecosystem, which is essential for regulating the Earth's climate. Additionally, evidence of ancient human settlements reveals that the region has been inhabited for thousands of years, reflecting the enduring connection between humans and nature in the Amazon.  

---



## Task 5: Building and Testing Agents with Tools

In this task, the retriever, summarizer, and word counter were integrated into a single agent workflow. The purpose was to demonstrate how the agent could retrieve relevant information from a document, generate a concise summary, and optionally perform additional analysis such as counting the words in the generated output.  

The retriever tool fetched relevant chunks of information from the source text. These chunks were then passed to the summarizer, which condensed the content into a short summary. Finally, the word counter tool was used in the second test to verify the length of the generated summary. Together, these tools highlight how agents can coordinate multiple steps in a pipeline to perform more advanced tasks.  

During the first test, the agent was only asked to provide a summary of AI breakthroughs. The final result was:  

**Test 1 Summary:**  
"AI breakthroughs have significantly improved diagnostics in healthcare and accelerated self-driving car research in transportation. The adoption of AI tools has transformed business practices and integrated virtual assistants like Siri and Alexa into daily life. These developments highlight AI's ongoing role in enhancing human intelligence and transforming multiple industries."  

In the second test, the agent was required to both summarize and count the words in the summary. The retrieved information was condensed into three sentences, followed by word count verification. The final result was:  

**Test 2 Summary + Word Count:**  
"AI-assisted diagnostics improved disease detection accuracy in healthcare, particularly for cancer. The technology rapidly spread across various industries, transforming sectors such as finance, transportation, and entertainment. Virtual assistants like Siri, Alexa, and Google Assistant gained widespread recognition as AI tools advanced toward augmenting human intelligence. The word count of this summary is 45."  

The word count of this summary was confirmed to be **45 words**.  

This demonstrates how the same agent can perform different levels of analysis depending on the requirements — in one case producing only a summary, and in another extending the process to include validation through word counting. 



## Task 6: Using Memory to Improve Summarization

In this task, the goal was to enhance our summarization chain from Task 2 by integrating memory. Memory enables the system to recall prior interactions and use that context to influence future outputs. This is particularly useful when working with related pieces of text where continuity and awareness of past summaries matter.

Two types of memory were implemented using LangChain: **ConversationBufferMemory** and **ConversationSummaryMemory**. The buffer memory stores past interactions verbatim, while the summary memory compresses them into shorter summaries. Both were tested by first summarizing a 100-word text about *machine learning* and then a related 100-word text about *deep learning*, explicitly instructing the model to consider prior conversation in its response.

The results show how memory influences the second summary differently depending on the type of memory used.

---

### 🔹 Results with ConversationBufferMemory

**First Summary (Machine Learning):**

Machine learning is a branch of artificial intelligence that allows computers to learn from data and improve their performance without explicit programming.  
It is utilized in various applications, including spam filtering, fraud detection, and predictive analytics, across multiple industries.  
Despite its advantages, challenges such as bias, transparency, and ethical responsibility need to be addressed as the technology becomes more widely adopted.  

**Second Summary (Deep Learning, considering prior summary):**

Deep learning is a branch of machine learning that utilizes multi-layered neural networks to analyze complex data.  
It has led to advancements in areas such as computer vision, natural language processing, and speech recognition, powering applications like facial recognition and virtual assistants.  
However, deep learning demands significant data and computational power, which raises issues related to fairness, energy use, and accessibility.  

---

### 🔹 Results with ConversationSummaryMemory

**First Summary (Machine Learning):**

Machine learning is a branch of artificial intelligence that allows computers to learn from data and improve their performance without explicit programming.  
It is utilized in various applications, including spam filtering, fraud detection, and predictive analytics, across multiple industries.  
Despite its advantages, challenges such as bias, transparency, and ethical responsibility need to be addressed as the technology becomes more widely adopted.  

**Second Summary (Deep Learning, considering prior summary):**

Deep learning is a branch of machine learning that utilizes multi-layered neural networks to analyze complex data.  
It has led to advancements in areas such as computer vision, natural language processing, and speech recognition, powering applications like facial recognition and virtual assistants.  
However, deep learning demands significant data and computational power, which raises issues related to fairness, energy use, and accessibility.  

---

### 🔹 Comparison and Insights

With **ConversationBufferMemory**, the system recalls the previous machine learning summary verbatim, ensuring accuracy and explicit continuity. This makes it well-suited for short sessions where exact details are important.  

With **ConversationSummaryMemory**, the system relies on compressed summaries, which capture the gist of prior interactions but sometimes introduce verbosity or redundancy. While this reduces accuracy slightly, it scales better for longer sessions by keeping memory compact.  



## Task 7: Leveraging Document Loaders for Diverse Sources

This task demonstrates how to use LangChain’s document loaders to process information from two different sources — a **PDF** and a **live Wikipedia page** — and compare the quality of AI-generated summaries.

---

## 🔧 Implementation Steps

1. **Load Sources**  
   - **PDF**: Used `PyPDFLoader` to load the IFPMA *AI Ethics Principles (July 2022)* PDF.  
   - **Webpage**: Used `WebBaseLoader` to scrape content from Wikipedia’s  
     [Ethics of Artificial Intelligence page](https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence).

2. **Chunking**  
   Used `RecursiveCharacterTextSplitter` with a **200** character chunk size and **20** overlap.  
   Multiple relevant chunks were retrieved for each query, then combined before summarization.

3. **Retriever & Vector Store**  
   Instead of building FAISS stores manually, the centralized **`build_retriever`** utility from Task 3 was reused.  
   Chunks were embedded with `AzureOpenAIEmbeddings`.

4. **Summarization**  
   Both sources were queried with:  
        "AI challenges"


The retrieved content was summarized using the reusable summarization chain from Task 2.

5. **Debugging Aid**  
Retrieved chunks were printed before summarization to observe the raw context provided to the model.

---

## 📄 Summaries

### PDF Summary (Source: IFPMA AI Ethics Principles, July 2022)

AI systems can produce outputs like content, predictions, and recommendations that impact various environments and opportunities.  

However, the emerging technology raises concerns about potential misuse, inadequate accountability, and varying risk levels in different applications, particularly in healthcare.  

A risk-based approach is essential, especially in areas like early research versus late clinical development, where the implications of AI use can differ significantly.  

**Accuracy Check**  
- ✅ Closely reflects the official IFPMA text.  
- ✅ Captures **misuse**, **accountability**, and **risk-based application** concerns.  
- ➡️ **Conclusion**: Accurate and faithful to the PDF.

---

### Web Summary (Source: Wikipedia – Ethics of AI)

Algorithmic biases present significant challenges in the responsible development and use of AI.  

These biases include language bias and gender bias, which can affect the fairness and effectiveness of AI systems.  

Addressing these issues is crucial for ensuring ethical AI practices.  

**Accuracy Check**  
- ✅ Correctly identifies **algorithmic bias**, **language bias**, and **gender bias** from Wikipedia.  
- ✅ Concise and thematically aligned with the source.  
- ➡️ **Conclusion**: Accurate, well-grounded, and free of fabricated details.

---

## 🔍 Comparison

The **PDF summary** is broader in scope, covering issues of **risk, accountability, and misuse**, with a strong emphasis on the healthcare context.  

The **Web summary** is more focused, centering specifically on **algorithmic bias** issues.  
While narrower, it is precise and well aligned with the Wikipedia text.  

---

## 🏆 Final Conclusion

The **PDF summary** highlights overarching governance, accountability, and healthcare-specific risks.  

The **Web summary** zeroes in on technical bias issues like language and gender.  

Together, these results demonstrate how **different document structures yield different emphases**: structured policy documents (PDFs) capture broader frameworks, while encyclopedic sources (Wikipedia) highlight detailed, categorized issues.  




# Task 9: Experimenting with Multi-Query Retrieval

## Overview
In this task, we extended our retriever pipeline to support **Multi-Query Retrieval**.  
Unlike the standard single-query retriever, the multi-query version reformulates the user query into multiple alternate queries.  
This helps retrieve a **wider range of relevant chunks**, often producing **richer and more balanced summaries**.

---

## Experiment

**Original Input Text (excerpt):**  
A long passage covering the history of Artificial Intelligence — from Turing and the Dartmouth Conference to AI winters, the rise of Deep Learning, AlphaGo, modern applications (healthcare, self-driving cars, assistants), and today’s focus on ethics and governance.

---

### 🔹 Single-query Summary

AI research progressed rapidly, leading to significant advancements in self-driving cars, healthcare diagnostics, and business tools that enhance human intelligence. Virtual assistants such as Siri, Alexa, and Google Assistant gained widespread recognition, while improvements in natural language processing and speech recognition set the stage for future developments. The evolution of AI has transformed various industries, including healthcare, finance, transportation, and entertainment, highlighting the cyclical nature of technological progress.

---

### 🔹 Multi-query Summary

The 2000s and 2010s saw significant advancements in AI, particularly through deep learning, leading to breakthroughs in image recognition and speech processing. This progress has prompted global efforts to establish frameworks for trustworthy AI development, as its applications have transformed various industries, including healthcare and finance. The history of AI reflects a cycle of optimism and setbacks, with each era contributing to its evolution as a field.

---

## Comparison
- **Single-query Retriever**: Narrower focus, emphasizing **modern applications** (self-driving cars, healthcare, assistants).  
- **Multi-query Retriever**: Broader coverage, highlighting **historical cycles and governance**, but less detail on applications.  

Together, both approaches complement each other — one captures **applications and industry impact**, while the other emphasizes **historical progression and ethics**.

---

## Key Takeaway
- Single-query retrieval works well for **direct, focused summaries**.  
- Multi-query retrieval is better at **broad, balanced coverage** of complex topics.  



## Task 10: Building a Question-Answering Chain on Summaries


### Objective

- Summarize the `ai_intro.txt` document.  

- Build a Question-Answering (QA) chain that can answer based on either:  
  - The **summary** of the document.  
  - The **full document text**.  

- Compare the responses for conciseness and accuracy.  


### Implementation

- A summarization chain (`build_summarization_chain`) was used to condense the entire document into 5 sentences.  

- A QA chain was created using a `PromptTemplate` and the LCEL `|` operator (`prompt | llm`).  

- The question asked was:  

  **“What’s the key event mentioned?”**  


### Results


**Document Summary (5 sentences):**

> The history of artificial intelligence (AI) began in the 1940s and 1950s with foundational work by pioneers like Alan Turing and John von Neumann, who developed key concepts in computation and algorithms.  

> The term "artificial intelligence" was coined in 1956 at the Dartmouth Conference, marking the start of AI as an academic discipline, with early successes in problem-solving programs.  

> However, the field faced an "AI winter" in the 1970s and 1980s due to limited computational power and funding, despite ongoing developments in expert systems.  

> The resurgence of AI in the 1990s was fueled by advancements in computing and machine learning, highlighted by IBM's Deep Blue defeating chess champion Garry Kasparov.  

> Today, AI is rapidly evolving with large language models and deep learning, impacting various industries while raising important ethical and societal concerns.  



**Q&A on Summary:**

> The key event mentioned is the coining of the term "artificial intelligence" in 1956 at the Dartmouth Conference.  



**Q&A on Full Document:**

> The key event mentioned is the Dartmouth Conference in 1956, where the term "artificial intelligence" was coined and is recognized as the birth of AI as an academic discipline.  



### Comparison

- **Summary-based QA** → More concise and direct.  

- **Full-text QA** → Slightly more detailed, includes the context that the event is considered the “birth of AI as an academic discipline.”  

- Both answers are correct, but the full-text QA provides richer context, while the summary QA is more efficient.  
