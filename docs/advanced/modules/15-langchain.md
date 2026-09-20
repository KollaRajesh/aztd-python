← [14. Django](./14-django.md) | [Modules](./README.md) | **15. LangChain** | [16. python-dotenv →](./16-python-dotenv.md)

---

# LangChain: LLM Framework

**Purpose:** Build applications with language models, chains, and memory.

## Simple: Basic Chain

```python
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI(api_key="sk-...", temperature=0.7)

template = "What is a good name for a {product}?"
prompt = PromptTemplate(input_variables=["product"], template=template)

chain = LLMChain(llm=llm, prompt=prompt)
result = chain.run(product="coffee shop")
print(result)
```

## Medium: RAG & Memory

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory

# Vector store
embeddings = OpenAIEmbeddings()
docs = ["Python is a programming language", "FastAPI is a web framework"]
vectorstore = FAISS.from_texts(docs, embeddings)

# QA chain with retrieval
llm = ChatOpenAI(temperature=0)
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

answer = qa.run("What is Python?")
print(answer)

# Memory
memory = ConversationBufferMemory()
memory.save_context({"input": "Hi"}, {"output": "Hello!"})
history = memory.load_memory_variables({})
```

## Complex: Agents & Custom Tools

```python
from langchain.agents import Tool, initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

def get_weather(location):
    return f"Weather in {location}: 72F, sunny"

def calculate(expression):
    return eval(expression)

tools = [
    Tool(name="Weather", func=get_weather, description="Get weather for location"),
    Tool(name="Calculator", func=calculate, description="Calculate math expressions")
]

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(memory_key="chat_history")

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

response = agent.run(input="What's the weather in NYC and calculate 2+2")
print(response)
```

**Install:** `pip install langchain openai` | **Use:** LLM applications, chatbots, RAG systems

---

← [14. Django](./14-django.md) | [Modules](./README.md) | **15. LangChain** | [16. python-dotenv →](./16-python-dotenv.md)
