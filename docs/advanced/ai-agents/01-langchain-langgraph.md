<!-- Navigation -->
**[← Networking](../networking/01-network-programming.md)** | **[Back to Index](../../../README.md)** | **[Data Science →](../data-science/01-numpy-pandas-sklearn.md)**

---

# Advanced Python: LangChain and LangGraph for AI Applications

## 2.27 LangChain Basics

LangChain is a framework for building applications with large language models (LLMs).

### Installation and Setup

```bash
pip install langchain openai python-dotenv
```

### Basic LLM Interaction

```python
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os

# Set API key
os.environ["OPENAI_API_KEY"] = "your-api-key"

# Initialize LLM
llm = OpenAI(temperature=0.7, max_tokens=100)

# Simple prompt
response = llm("What is Python?")
print(response)

# Prompt template
template = "What is the capital of {country}?"
prompt = PromptTemplate(input_variables=["country"], template=template)

# Generate using template
query = prompt.format(country="France")
response = llm(query)
print(response)
```

### Chains

```python
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.7)

# Create prompt template
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in one paragraph"
)

# Create chain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Run chain
result = chain.run(topic="Machine Learning")
print(result)
```

### Sequential Chains

```python
from langchain.chains import SequentialChain

# First chain: Generate idea
first_prompt = PromptTemplate(
    input_variables=["product"],
    template="Generate marketing ideas for {product}"
)
first_chain = LLMChain(llm=llm, prompt=first_prompt, output_key="ideas")

# Second chain: Refine ideas
second_prompt = PromptTemplate(
    input_variables=["ideas"],
    template="Refine these ideas: {ideas}"
)
second_chain = LLMChain(llm=llm, prompt=second_prompt, output_key="refined")

# Sequential chain
overall_chain = SequentialChain(
    chains=[first_chain, second_chain],
    input_variables=["product"],
    output_variables=["ideas", "refined"]
)

result = overall_chain({"product": "AI Assistant"})
print(result)
```

---

## 2.28 LangChain Memory and Context

### Conversation Memory

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.7)

# Create memory
memory = ConversationBufferMemory()

# Create conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# Multiple turns
print(conversation.run(input="Hi, my name is Alice"))
print(conversation.run(input="What's my name?"))
print(conversation.run(input="Tell me a joke"))
```

### Summary Memory

```python
from langchain.memory import ConversationSummaryMemory

memory = ConversationSummaryMemory(llm=llm)

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# Long conversation gets summarized
for i in range(10):
    conversation.run(input=f"Tell me fact {i}")
```

---

## 2.29 LangChain Retrievers and RAG

Retrieval-Augmented Generation (RAG) combines retrieved documents with LLM.

### Document Loading

```python
from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

# Load documents
loader = TextLoader("document.txt")
documents = loader.load()

# Split into chunks
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(documents)

# Or load PDF
pdf_loader = PyPDFLoader("document.pdf")
pdf_documents = pdf_loader.load()
```

### Vector Store and Retrieval

```python
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Create embeddings
embeddings = OpenAIEmbeddings()

# Create vector store
vector_store = FAISS.from_documents(chunks, embeddings)

# Create retriever
retriever = vector_store.as_retriever()

# Create QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)

# Ask questions
result = qa_chain.run("What is discussed in the document?")
print(result)
```

---

## 2.30 LangGraph Introduction

LangGraph is a framework for building stateful, multi-agent systems.

### Basic Graph Structure

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict

# Define state
class AgentState(TypedDict):
    input: str
    output: str
    logs: list

# Create graph
workflow = StateGraph(AgentState)

# Define nodes
def process_input(state):
    state["logs"].append(f"Processing: {state['input']}")
    state["output"] = state["input"].upper()
    return state

def validate_output(state):
    state["logs"].append(f"Validating: {state['output']}")
    return state

# Add nodes
workflow.add_node("process", process_input)
workflow.add_node("validate", validate_output)

# Add edges
workflow.add_edge("process", "validate")
workflow.add_edge("validate", END)

# Set entry point
workflow.set_entry_point("process")

# Compile and run
app = workflow.compile()

initial_state = {"input": "hello", "output": "", "logs": []}
result = app.invoke(initial_state)

print(result["output"])  # HELLO
print(result["logs"])
```

### Conditional Routing

```python
from langgraph.graph import StateGraph, END

class RouterState(TypedDict):
    query: str
    route: str
    result: str

workflow = StateGraph(RouterState)

def route_query(state):
    """Route query to appropriate handler"""
    query = state["query"].lower()
    
    if "weather" in query:
        state["route"] = "weather"
    elif "news" in query:
        state["route"] = "news"
    else:
        state["route"] = "general"
    
    return state

def handle_weather(state):
    state["result"] = "Weather info here"
    return state

def handle_news(state):
    state["result"] = "News info here"
    return state

def handle_general(state):
    state["result"] = "General response here"
    return state

# Add nodes
workflow.add_node("route", route_query)
workflow.add_node("weather", handle_weather)
workflow.add_node("news", handle_news)
workflow.add_node("general", handle_general)

# Add conditional edge
def route_decision(state):
    return state["route"]

workflow.add_conditional_edges("route", route_decision, {
    "weather": "weather",
    "news": "news",
    "general": "general"
})

workflow.add_edge("weather", END)
workflow.add_edge("news", END)
workflow.add_edge("general", END)

workflow.set_entry_point("route")

app = workflow.compile()

result = app.invoke({"query": "What's the weather?", "route": "", "result": ""})
print(result["result"])
```

---

## 2.31 Multi-Agent Systems with LangGraph

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from langchain.llms import OpenAI

llm = OpenAI()

class ResearchState(TypedDict):
    topic: str
    research_notes: List[str]
    draft: str
    review_feedback: str
    final_output: str

# Researcher agent
def researcher(state):
    """Research a topic"""
    topic = state["topic"]
    notes = f"Research on {topic}:\n- Key point 1\n- Key point 2"
    state["research_notes"].append(notes)
    return state

# Writer agent
def writer(state):
    """Write based on research"""
    notes = state["research_notes"]
    draft = f"Draft article based on: {', '.join(notes)}"
    state["draft"] = draft
    return state

# Reviewer agent
def reviewer(state):
    """Review the draft"""
    feedback = "Feedback: Good structure, needs more detail"
    state["review_feedback"] = feedback
    return state

# Editor agent
def editor(state):
    """Create final output"""
    state["final_output"] = f"Final: {state['draft']}\nFeedback applied: {state['review_feedback']}"
    return state

# Build workflow
workflow = StateGraph(ResearchState)

workflow.add_node("research", researcher)
workflow.add_node("write", writer)
workflow.add_node("review", reviewer)
workflow.add_node("edit", editor)

# Chain: Research -> Write -> Review -> Edit
workflow.add_edge("research", "write")
workflow.add_edge("write", "review")
workflow.add_edge("review", "edit")
workflow.add_edge("edit", END)

workflow.set_entry_point("research")

app = workflow.compile()

initial_state = {
    "topic": "Python Best Practices",
    "research_notes": [],
    "draft": "",
    "review_feedback": "",
    "final_output": ""
}

result = app.invoke(initial_state)
print(result["final_output"])
```

---

## 2.32 LangChain Tools and Agents

### Creating Custom Tools

```python
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.7)

# Define custom tools
def calculate(expression: str) -> str:
    """Calculate mathematical expression"""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

def get_time() -> str:
    """Get current time"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create tool objects
tools = [
    Tool(
        name="Calculator",
        func=calculate,
        description="Useful for mathematical calculations"
    ),
    Tool(
        name="GetTime",
        func=get_time,
        description="Returns current date and time"
    )
]

# Create agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Ask agent to use tools
response = agent.run("What is 25 * 4? And what's the current time?")
print(response)
```

---

## 2.33 Real-World Example: Document QA System

```python
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os

class DocumentQASystem:
    def __init__(self, document_path: str):
        self.document_path = document_path
        self.llm = OpenAI(temperature=0)
        self.qa_chain = None
    
    def setup(self):
        """Setup vector store and QA chain"""
        # Load document
        loader = TextLoader(self.document_path)
        documents = loader.load()
        
        # Split into chunks
        text_splitter = CharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_documents(documents)
        
        # Create embeddings
        embeddings = OpenAIEmbeddings()
        
        # Create vector store
        vector_store = FAISS.from_documents(chunks, embeddings)
        
        # Create retriever and QA chain
        retriever = vector_store.as_retriever(search_kwargs={"k": 3})
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True
        )
        
        print("Document QA system ready")
    
    def ask(self, question: str) -> dict:
        """Ask question about document"""
        if not self.qa_chain:
            raise ValueError("System not set up. Call setup() first.")
        
        result = self.qa_chain({"query": question})
        
        return {
            "question": question,
            "answer": result["result"],
            "sources": [doc.metadata for doc in result["source_documents"]]
        }

# Usage
# qa_system = DocumentQASystem("my_document.txt")
# qa_system.setup()
# result = qa_system.ask("What is the main topic?")
# print(result["answer"])
```

---

## 2.34 Real-World Example: Multi-Agent Research Assistant

```python
from langgraph.graph import StateGraph, END
from langchain.llms import OpenAI
from typing import TypedDict, List

class ResearchAssistantState(TypedDict):
    query: str
    research_results: List[str]
    analysis: str
    final_report: str

llm = OpenAI(temperature=0.7)

def search_agent(state):
    """Search for information"""
    query = state["query"]
    # Simulate search results
    results = [
        f"Result 1 for {query}",
        f"Result 2 for {query}",
        f"Result 3 for {query}"
    ]
    state["research_results"].extend(results)
    return state

def analysis_agent(state):
    """Analyze research results"""
    results = state["research_results"]
    analysis_prompt = f"Analyze these results: {', '.join(results)}"
    
    # Simulate analysis
    state["analysis"] = f"Analysis of {len(results)} findings"
    return state

def report_agent(state):
    """Generate final report"""
    state["final_report"] = f"""
    Research Report
    ===============
    Query: {state['query']}
    
    Research Results:
    {chr(10).join(state['research_results'])}
    
    Analysis:
    {state['analysis']}
    """
    return state

# Build workflow
workflow = StateGraph(ResearchAssistantState)

workflow.add_node("search", search_agent)
workflow.add_node("analyze", analysis_agent)
workflow.add_node("report", report_agent)

workflow.add_edge("search", "analyze")
workflow.add_edge("analyze", "report")
workflow.add_edge("report", END)

workflow.set_entry_point("search")

app = workflow.compile()

initial_state = {
    "query": "What are the latest trends in AI?",
    "research_results": [],
    "analysis": "",
    "final_report": ""
}

result = app.invoke(initial_state)
print(result["final_report"])
```

---

## Summary Table

| Concept | Purpose | Use Case |
|---------|---------|----------|
| **Chains** | Connect prompts and LLMs | Sequential operations |
| **Memory** | Track conversation context | Chatbots, dialogue |
| **Retrievers** | Find relevant documents | RAG systems, QA |
| **Tools** | Extend agent capabilities | Tool-using agents |
| **Agents** | Autonomous decision-making | Complex workflows |
| **LangGraph** | Multi-agent systems | Stateful workflows |

| Component | Description | Example |
|-----------|-------------|---------|
| **LLMChain** | Simple LLM + prompt | Translation chain |
| **SequentialChain** | Multiple chains in sequence | Research -> Write -> Review |
| **RetrievalQA** | Question answering with documents | Document QA system |
| **Agent** | Tool-using autonomous system | Calculator + search agent |
| **Graph Workflow** | Stateful multi-step system | Multi-agent research |

---

## Key Patterns

### Pattern 1: RAG (Retrieval-Augmented Generation)
```
Document -> Chunks -> Embeddings -> Vector Store -> Retriever -> LLM
```

### Pattern 2: Agent Loop
```
User Input -> Agent Thinks -> Selects Tool -> Executes -> Observes -> Repeat
```

### Pattern 3: Multi-Agent Workflow
```
Entry -> Agent1 -> Agent2 -> Agent3 -> Exit
```

---

<!-- Navigation Footer -->
**[← Networking](../networking/01-network-programming.md)** | **[Back to Index](../../../README.md)** | **[Data Science →](../data-science/01-numpy-pandas-sklearn.md)**

**Sections:** 2.27-2.34 | **Time:** 1-2 hours
