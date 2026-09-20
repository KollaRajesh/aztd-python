# aztd-python

Comprehensive Python learning hub covering fundamentals through advanced topics: web applications, REST APIs, concurrency, data science, AI agents, and system design patterns.

## Overview

Structured, example-driven documentation with 43 major topics organized into 6 specializations:

- **Fundamentals** (1.1-1.15) - Variables, functions, OOP, modules, decorators, generators
- **Web APIs** (2.1-2.6) - Flask, FastAPI, REST API design
- **Concurrency** (2.7-2.11) - Threading, asyncio, async patterns
- **Performance** (2.12-2.18) - Profiling, optimization, caching
- **Networking** (2.19-2.26) - Sockets, HTTP, DNS, email, SSL/TLS
- **AI/Agents** (2.27-2.34) - LangChain, LangGraph, multi-agent systems
- **Data Science** (2.35-2.43) - NumPy, Pandas, Scikit-Learn, ML pipelines

## Getting Started

### Install Python

**Windows:**
1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer, check "Add Python to PATH"
3. Verify: `python --version`

**macOS:**
```bash
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Package Managers

#### pip (default Python package manager)
```bash
pip install package_name          # Install
pip install package==1.0.0        # Specific version
pip install -r requirements.txt   # From file
pip list                          # Show installed
pip uninstall package_name        # Remove
pip freeze > requirements.txt     # Export versions
```

#### uv (faster alternative)
```bash
pip install uv                    # Install uv

uv pip install package_name       # Install (faster)
uv pip install -r requirements.txt
uv pip list
uv pip uninstall package_name
uv pip freeze > requirements.txt
```

### pip vs uv Comparison

| Task | pip | uv |
|------|-----|-----|
| **Install package** | `pip install xyz` | `uv pip install xyz` |
| **Install version** | `pip install xyz==1.0` | `uv pip install xyz==1.0` |
| **Install from file** | `pip install -r req.txt` | `uv pip install -r req.txt` |
| **List packages** | `pip list` | `uv pip list` |
| **Remove package** | `pip uninstall xyz` | `uv pip uninstall xyz` |
| **Export versions** | `pip freeze` | `uv pip freeze` |
| **Speed** | Slow | ⚡ Fast (10-100x) |
| **Compatibility** | Wide | pip-compatible |
| **Recommendation** | Use when uv unavailable | **Use for large projects** |

### Virtual Environment

Isolate project dependencies (recommended for every project).

**Create:**
```bash
python -m venv venv
```

**Activate:**
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

**Deactivate:**
```bash
deactivate
```

**Use with pip:**
```bash
# After activation
pip install package_name
```

**Use with uv:**
```bash
# uv auto-creates virtual env in .venv
uv pip install package_name
```

## Setup This Repository

Follow these steps to set up aztd-python locally.

### 1. Clone Repository
```bash
git clone https://github.com/KollaRajesh/aztd-python.git
cd aztd-python
```

### 2. Create Virtual Environment

**Option A: Using Python (traditional)**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

**Option B: Using UV (faster)**
```bash
uv venv
# Activate automatically or use:
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
```

### 3. Install Dependencies
```bash
# After activating venv
pip install -r requirements.txt

# Or with uv
uv pip install -r requirements.txt
```

### 4. Launch Jupyter Notebooks
```bash
jupyter lab

# Or with uv (no activation needed)
uv run jupyter lab
```

Then navigate to `docs/` directory to explore notebooks.

### 5. (Optional) Setup Code Review Graph

For code analysis and architecture visualization:

```bash
pip install code-review-graph

# Generate analysis
crg build

# View architecture
crg view
```

This creates `.code-review-graph/` directory (auto-generated, not committed to git).

### Configuration Files

**What's committed:**
- `requirements.txt` - All dependencies
- `README.md` - This guide
- `CONTRIBUTING.md` - Authoring standards
- `docs/` - 25 notebooks and markdown guides

**What's NOT committed (auto-generated locally):**
- `.venv/` - Your isolated Python environment
- `.code-review-graph/` - Code analysis database
- `__pycache__/` - Python bytecode

See `.gitignore` for complete list.

### Jupyter Environment Setup and Verification

<details>
<summary><strong>Jupyter Environment Setup and Verification</strong></summary>

**Purpose:** Set up and verify Jupyter notebooks with proper kernel and dependencies.

#### Setup Steps

1. **Install Jupyter**
   ```bash
   pip install jupyter jupyterlab ipykernel
   ```

2. **Register Python Kernel**
   ```bash
   python -m ipykernel install --user --name=aztd-python
   ```

3. **Verify Installation**
   ```bash
   jupyter kernelspec list
   ```

#### Verification Commands

**Check Python Environment**
```bash
# Activate virtual environment
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Verify key packages
python -c "import sqlalchemy, pandas, numpy, requests; print('All packages imported successfully')"
```

**Test Jupyter Kernel**
```bash
# Start Jupyter
jupyter notebook

# Or JupyterLab
jupyter lab
```

**Verify Kernel Connection**
```bash
# In Jupyter, create a new notebook with "aztd-python" kernel
# Test basic imports
from sqlalchemy import create_engine
from pandas import DataFrame
import numpy as np

print("SQLAlchemy version:", sqlalchemy.__version__)
print("Pandas version:", pandas.__version__)
print("NumPy version:", np.__version__)
```

#### Troubleshooting

**Common Issues**

- **ModuleNotFoundError**: Install missing packages with `pip install package_name`
- **Kernel not found**: Reinstall kernel with `python -m ipykernel install --user --name=aztd-python`
- **Permission denied**: Use `--user` flag or run as administrator

**Check Environment**
```bash
# List all installed packages
pip list

# Check virtual environment
which python
python -m venv --help
```

</details>

### Most Common Modules

| # | Module | Focus | Examples | Install | Guide |
|---|--------|-------|----------|---------|-------|
| 1 | **SQLAlchemy** | ORM & databases | CRUD, relationships, transactions | `pip install sqlalchemy` | [01-sqlalchemy.md](./docs/advanced/modules/01-sqlalchemy.md) |
| 2 | **Pydantic** | Data validation | Basic validation, custom validators, config | `pip install pydantic` | [02-pydantic.md](./docs/advanced/modules/02-pydantic.md) |
| 3 | **BeautifulSoup4** | Web scraping | HTML parsing, web scraping, navigation | `pip install beautifulsoup4` | [03-beautifulsoup4.md](./docs/advanced/modules/03-beautifulsoup4.md) |
| 4 | **python-dotenv** | Configuration | .env loading, type conversion, Pydantic | `pip install python-dotenv` | [04-dotenv.md](./docs/advanced/modules/04-dotenv.md) |
| 5 | **Requests** | HTTP client | GET/POST, headers, error handling, sessions | `pip install requests` | [05-requests.md](./docs/advanced/modules/05-requests.md) |
| 6 | **aiohttp** | Async HTTP | Async requests, concurrent ops, pools | `pip install aiohttp` | [06-aiohttp.md](./docs/advanced/modules/06-aiohttp.md) |
| 7 | **NumPy** | Numerical computing | Arrays, matrices, broadcasting, vectorization | `pip install numpy` | [07-numpy.md](./docs/advanced/modules/07-numpy.md) |
| 8 | **Pandas** | Data analysis | DataFrames, filtering, grouping, time series | `pip install pandas` | [08-pandas.md](./docs/advanced/modules/08-pandas.md) |
| 9 | **Matplotlib** | Visualization | Line/bar/scatter plots, subplots, annotations | `pip install matplotlib` | [09-matplotlib.md](./docs/advanced/modules/09-matplotlib.md) |
| 10 | **Pytest** | Testing | Basic tests, fixtures, parametrization, mocking | `pip install pytest` | [10-pytest.md](./docs/advanced/modules/10-pytest.md) |
| 11 | **Scikit-learn** | Machine learning | Classification, pipelines, hyperparameter tuning | `pip install scikit-learn` | [11-scikit-learn.md](./docs/advanced/modules/11-scikit-learn.md) |
| 12 | **Flask** | Web framework | Basic app, routing, blueprints, middleware | `pip install flask` | [12-flask.md](./docs/advanced/modules/12-flask.md) |
| 13 | **FastAPI** | Async API | Basic API, validation, dependencies, middleware | `pip install fastapi uvicorn` | [13-fastapi.md](./docs/advanced/modules/13-fastapi.md) |
| 14 | **Django** | Full-stack | Models, views, QuerySets, signals, managers | `pip install django` | [14-django.md](./docs/advanced/modules/14-django.md) |
| 15 | **LangChain** | LLM framework | Chains, RAG, memory, agents, tools | `pip install langchain openai` | [15-langchain.md](./docs/advanced/modules/15-langchain.md) |
| 16 | **python-dotenv** | Environment vars | Configuration management, secrets handling | `pip install python-dotenv` | [16-python-dotenv.md](./docs/advanced/modules/16-python-dotenv.md) |

### Quick start

```bash
# Create virtual environment
python -m venv venv

# Activate
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Install dependencies
pip install requests numpy pandas

# Browse docs
cat docs/fundamentals/core-concepts/01-variables-to-classes.md

# Run examples
python samples/variables_types.py

# Deactivate
deactivate
```

---

## Complete Topic Index

### Fundamentals (1.1 - 1.15)

| # | Topic | File | Key Concepts |
|---|-------|------|--------------|
| 1.1 | Variables & assignment | `core-concepts/01-variables-to-classes.md` | Declaration, scope, naming |
| 1.2 | Data types | `core-concepts/01-variables-to-classes.md` | int, str, float, bool, None |
| 1.3 | Operators | `core-concepts/01-variables-to-classes.md` | Arithmetic, comparison, logical |
| 1.4 | Control flow | `core-concepts/01-variables-to-classes.md` | if/elif/else, loops, break/continue |
| 1.5 | Functions | `core-concepts/01-variables-to-classes.md` | Definition, parameters, return, recursion |
| 1.6 | Classes & objects | `core-concepts/01-variables-to-classes.md` | Definition, instantiation, methods |
| 1.7 | OOP principles | `oop/02-oop-principles.md` | Encapsulation, abstraction, inheritance, polymorphism |
| 1.8 | Modules & imports | `modules-files/03-modules-files-advanced.md` | Module creation, imports, packages |
| 1.9 | File handling | `modules-files/03-modules-files-advanced.md` | Read, write, JSON, CSV |
| 1.10 | Decorators | `modules-files/03-modules-files-advanced.md` | Function/class decorators, parameters |
| 1.11 | Generators | `modules-files/03-modules-files-advanced.md` | yield, generator expressions |
| 1.12 | Iterators | `modules-files/03-modules-files-advanced.md` | __iter__, __next__, custom iterators |
| 1.13 | Type hints | `modules-files/03-modules-files-advanced.md` | Annotations, generics, Optional |
| 1.14 | Dataclasses | `modules-files/03-modules-files-advanced.md` | @dataclass, fields, defaults |
| 1.15 | Context managers | `modules-files/03-modules-files-advanced.md` | with statement, __enter__/__exit__ |

### Web APIs (2.1 - 2.6)

| # | Topic | File | Key Concepts |
|---|-------|------|--------------|
| 2.1 | Flask basics | `web-apis/01-flask-fastapi-rest.md` | Routes, decorators, request/response |
| 2.2 | Flask advanced | `web-apis/01-flask-fastapi-rest.md` | Blueprints, middleware, error handlers |
| 2.3 | FastAPI intro | `web-apis/01-flask-fastapi-rest.md` | Path/query params, type validation |
| 2.4 | FastAPI features | `web-apis/01-flask-fastapi-rest.md` | Pydantic models, async endpoints |
| 2.5 | REST API design | `web-apis/01-flask-fastapi-rest.md` | HTTP methods, status codes, HATEOAS |
| 2.6 | Auth & middleware | `web-apis/01-flask-fastapi-rest.md` | JWT, API keys, CORS |

### Concurrency (2.7 - 2.11)

| # | Topic | File | Key Concepts |
|---|-------|------|--------------|
| 2.7 | Threading basics | `concurrency/01-threading-asyncio.md` | Thread creation, daemon threads |
| 2.8 | Thread synchronization | `concurrency/01-threading-asyncio.md` | Lock, RLock, Event, Condition |
| 2.9 | Asyncio intro | `concurrency/01-threading-asyncio.md` | async/await, event loop |
| 2.10 | Asyncio patterns | `concurrency/01-threading-asyncio.md` | gather, wait, producer-consumer |
| 2.11 | Threading vs asyncio | `concurrency/01-threading-asyncio.md` | Performance, use cases, comparison |

### Performance (2.12 - 2.18)

| # | Topic | File | Key Concepts |
|---|-------|------|--------------|
| 2.12 | Profiling | `performance/01-performance-optimization.md` | cProfile, memory_profiler, timing |
| 2.13 | Benchmarking | `performance/01-performance-optimization.md` | timeit, pytest-benchmark |
| 2.14 | Optimization techniques | `performance/01-performance-optimization.md` | Caching, memoization, algorithms |
| 2.15 | Caching strategies | `performance/01-performance-optimization.md` | @cache, LRU, redis |
| 2.16 | Database optimization | `performance/01-performance-optimization.md` | Indexing, query optimization |
| 2.17 | Algorithm optimization | `performance/01-performance-optimization.md` | Big O, data structures |
| 2.18 | Code optimization | `performance/01-performance-optimization.md` | Comprehensions, vectorization |

### Networking (2.19 - 2.26)

| # | Topic | File | Key Concepts |
|---|-------|------|--------------|
| 2.19 | Socket programming | `networking/01-network-programming.md` | TCP/UDP, client/server |
| 2.20 | HTTP requests | `networking/01-network-programming.md` | requests library, status codes |
| 2.21 | Async HTTP | `networking/01-network-programming.md` | aiohttp, concurrent requests |
| 2.22 | DNS & domains | `networking/01-network-programming.md` | socket.gethostbyname, DNS lookup |
| 2.23 | Port scanning | `networking/01-network-programming.md` | Port detection, vulnerability scanning |
| 2.24 | Email | `networking/01-network-programming.md` | SMTP, POP3, email sending |
| 2.25 | SSL/TLS | `networking/01-network-programming.md` | Certificate validation, secure sockets |
| 2.26 | Chat application | `networking/01-network-programming.md` | Multi-client server, messaging |

### AI/Agents (2.27 - 2.34)

| # | Topic | File | Key Concepts |
|---|-------|------|--------------|
| 2.27 | LangChain basics | `ai-agents/01-langchain-langgraph.md` | LLMs, prompts, chains |
| 2.28 | Memory & chains | `ai-agents/01-langchain-langgraph.md` | ConversationMemory, sequential chains |
| 2.29 | RAG | `ai-agents/01-langchain-langgraph.md` | Retrieval-augmented generation |
| 2.30 | LangGraph intro | `ai-agents/01-langchain-langgraph.md` | State graphs, node functions |
| 2.31 | Multi-agent systems | `ai-agents/01-langchain-langgraph.md` | Coordination, communication |
| 2.32 | Tools & integration | `ai-agents/01-langchain-langgraph.md` | Tool binding, API calls |
| 2.33 | Document QA | `ai-agents/01-langchain-langgraph.md` | Document parsing, similarity search |
| 2.34 | Research assistant | `ai-agents/01-langchain-langgraph.md` | Multi-step reasoning, web search |

### Data Science (2.35 - 2.43)

| # | Topic | File | Key Concepts |
|---|-------|------|--------------|
| 2.35 | NumPy arrays | `data-science/01-numpy-pandas-sklearn.md` | Array creation, operations, broadcasting |
| 2.36 | NumPy advanced | `data-science/01-numpy-pandas-sklearn.md` | Linear algebra, random, aggregation |
| 2.37 | Pandas basics | `data-science/01-numpy-pandas-sklearn.md` | DataFrames, Series, indexing |
| 2.38 | Data cleaning | `data-science/01-numpy-pandas-sklearn.md` | Missing values, type conversion, groupby |
| 2.39 | Data visualization | `data-science/01-numpy-pandas-sklearn.md` | Matplotlib, Seaborn, plotting |
| 2.40 | Scikit-Learn intro | `data-science/01-numpy-pandas-sklearn.md` | Estimators, pipeline, model selection |
| 2.41 | Classification | `data-science/01-numpy-pandas-sklearn.md` | Iris dataset, cross-validation |
| 2.42 | Regression | `data-science/01-numpy-pandas-sklearn.md` | Linear/polynomial regression, evaluation |
| 2.43 | Time series | `data-science/01-numpy-pandas-sklearn.md` | ARIMA, forecasting, seasonal data |

---

## File Organization

```
aztd-python/
├── README.md                           # This file (complete index + structure)
├── CONTRIBUTING.md                     # Writing standards & guidelines
├── QUICK_START.md                      # 5-minute quick start guide
├── QUICK_REFERENCE.md                  # Python syntax quick reference card
├── TROUBLESHOOTING_AND_FAQ.md          # Common issues & solutions
├── RESOURCES_AND_BEST_PRACTICES.md     # Tools, patterns, external links
│
├── docs/
│   ├── fundamentals/
│   │   ├── core-concepts/
│   │   │   └── 01-variables-to-classes.md         # Sections 1.1-1.6
│   │   ├── oop/
│   │   │   └── 02-oop-principles.md               # Section 1.7
│   │   └── modules-files/
│   │       └── 03-modules-files-advanced.md       # Sections 1.8-1.15
│   │
│   └── advanced/
│       ├── web-apis/
│       │   └── 01-flask-fastapi-rest.md           # Sections 2.1-2.6
│       ├── concurrency/
│       │   └── 01-threading-asyncio.md            # Sections 2.7-2.11
│       ├── performance/
│       │   └── 01-performance-optimization.md     # Sections 2.12-2.18
│       ├── networking/
│       │   └── 01-network-programming.md          # Sections 2.19-2.26
│       ├── ai-agents/
│       │   └── 01-langchain-langgraph.md          # Sections 2.27-2.34
│       └── data-science/
│           └── 01-numpy-pandas-sklearn.md         # Sections 2.35-2.43
│
├── samples/                            # Runnable .py files paired with docs
│   ├── variables_types.py
│   ├── control_flow.py
│   ├── functions.py
│   ├── classes_oop.py
│   ├── decorators.py
│   ├── generators.py
│   ├── flask_app.py
│   ├── fastapi_app.py
│   ├── threading_example.py
│   ├── asyncio_example.py
│   ├── rest_api.py
│   ├── langchain_basic.py
│   ├── numpy_pandas.py
│   ├── ml_classification.py
│   └── [more examples...]
│
├── .github/
│   └── copilot-instructions.md         # AI contribution guidelines
│
├── LICENSE
└── .gitignore
```

---

## FAQ

**Q: Start with?**  
A: Section 1.1 if new to Python.

**Q: Skip fundamentals?**  
A: No, they're prerequisites.

**Q: How long per section?**  
A: 1-2 hours average.

**Q: Examples production-ready?**  
A: Educational only; add error handling.

**Q: Run samples?**  
A: `python samples/topic_name.py`

**Q: Contribute?**  
A: See CONTRIBUTING.md.

---

## Quick Tips

- Use comprehensions, not loops
- Cache with `@cache`
- Profile with `cProfile`
- Use generators for large data
- Vectorize with NumPy
- Type hints for clarity
- PEP 8 compliant code

---

## Development Tools

### IDE & Editors

| Tool | VS Code | PyCharm | JupyterLab |
|------|---------|---------|-----------|
| **Free** | Yes | Community edition | Yes |
| **Python support** | Excellent | Built-in | Notebooks |
| **Debugger** | Yes | Yes | Limited |
| **Linting** | Yes (via extension) | Built-in | Extensions |
| **Best for** | Light/web dev | Large projects | Data science |

#### VS Code Python Extensions

| Extension | Purpose | Install |
|-----------|---------|---------|
| Python | Official Python support | Built-in |
| Pylance | Type checking, IntelliSense | Marketplace |
| Pylint | Linting | Marketplace |
| Black Formatter | Code formatting | Marketplace |
| Pytest | Testing | Marketplace |
| Jupyter | Notebook support | Marketplace |

### Install IDEs

**Windows (using Chocolatey):**
```bash
# Install Chocolatey first (if needed)
# https://chocolatey.org/install

choco install pycharm-community
choco install jupyterlab
```

**Windows (using winget):**
```bash
winget install JetBrains.PyCharm.Community
winget install Jupyter.JupyterLab
```

**macOS:**
```bash
brew install pycharm-ce
brew install jupyterlab
```

**Linux:**
```bash
sudo apt install pycharm-community
sudo apt install jupyterlab
```

### Code Quality Tools

#### Pylint (Find errors and style issues)
```bash
pip install pylint

pylint file.py                    # Check file
pylint --generate-rcfile > .pylintrc  # Generate config
```

#### Flake8 (Style guide enforcement)
```bash
pip install flake8

flake8 file.py                    # Check file
flake8 . --count --show-source    # Show detailed errors
```

#### Black (Auto-format code)
```bash
pip install black

black file.py                     # Format file
black . --line-length 88          # Format all files
```

#### mypy (Type checking)
```bash
pip install mypy

mypy file.py                      # Type check file
mypy . --strict                   # Strict checking
```

### Full Setup Example

```bash
# Create virtual environment
python -m venv venv

# Activate
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Install development tools
pip install pylint flake8 black mypy pytest

# Check code quality
pylint src/
flake8 src/
mypy src/

# Format code
black src/

# Run tests
pytest tests/
```

### Quick Quality Check Workflow

```bash
# 1. Format code automatically
black .

# 2. Check for style issues
flake8 .

# 3. Type check
mypy .

# 4. Detailed analysis
pylint src/

# 5. Run tests
pytest
```

---

## Best Practices

### Code Standards
- **Style:** PEP 8, 4 spaces, <88 chars per line
- **Type Hints:** Always use for clarity
- **Error Handling:** Catch specific exceptions
- **Functions:** Single responsibility
- **Files:** Use context managers (`with` statement)

### Performance
- Profile with `cProfile` before optimizing
- List comprehensions over loops
- Cache with `@cache`
- Generators for large datasets
- NumPy vectorization
- `set` for membership checks (O(1))

### Security
- No hardcoded secrets
- Use environment variables
- Validate user input
- Use parameterized queries
- Hash passwords (bcrypt)
- HTTPS for APIs
- Keep dependencies updated

### Common Patterns

**Singleton:**
```python
class Config:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

**Factory:**
```python
class DBFactory:
    @staticmethod
    def create(db_type):
        return PostgresDB() if db_type == "postgres" else MysqlDB()
```

**Decorator:**
```python
def timing(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time: {time.time() - start}s")
        return result
    return wrapper
```

---

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| ImportError | Missing package | `pip install xyz` |
| IndentationError | Tabs vs spaces | Use 4 spaces consistently |
| TypeError | Wrong data type | Check with `type(variable)` |
| AttributeError | Variable is None | Add null checks |
| RecursionError | Infinite recursion | Add base case |
| FastAPI won't start | Port in use | `uvicorn app:app --port 8001` |
| Async not awaited | Missing `await` | Use `await` on async calls |

---

## External Resources

- [Python docs](https://docs.python.org/3/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Flask](https://flask.palletsprojects.com/)
- [LangChain](https://python.langchain.com/)
- [Scikit-Learn](https://scikit-learn.org/)
- [NumPy](https://numpy.org/doc/)
- [Pandas](https://pandas.pydata.org/docs/)

### Start learning

1. Read `QUICK_START.md` (5 min overview)
2. Pick a topic from the index above
3. Read the documentation with examples
4. Run code from `samples/`

### Find a specific topic

Use the index tables above. Each topic maps to:
- File location
- Key concepts covered
- Related sections

### Quick reference

- **Syntax help:** `QUICK_REFERENCE.md`
- **Common issues:** `TROUBLESHOOTING_AND_FAQ.md`
- **Best practices:** `RESOURCES_AND_BEST_PRACTICES.md`

### Contribute

See `CONTRIBUTING.md` for structure, tone, and quality standards.

---

## Key principles

- **Clear** - Concise explanations; no jargon or verbosity
- **Practical** - Every concept has a working example
- **Focused** - One idea per section; minimal content
- **Progressive** - Fundamentals first, then advanced
- **Standards** - PEP 8, type hints, error handling

## Example

### Fundamentals (1.1)

```python
# Variables and strings
name = "Alice"
age = 30
print(f"{name} is {age} years old")
```

### Advanced (2.3 - FastAPI)

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "name": "Alice"}
```

---

## Resources

- [Python docs](https://docs.python.org/3/)
- [FastAPI docs](https://fastapi.tiangolo.com/)
- [LangChain docs](https://python.langchain.com/)
- [Scikit-Learn docs](https://scikit-learn.org/)

## License

See `LICENSE` file.

## Contributing

Contributions welcome. Follow `CONTRIBUTING.md`.

- Add docs to appropriate folder
- Add samples to `samples/`
- Keep explanations clear, examples minimal
- Update README index if adding new topics

---

**Start here:** Open `QUICK_START.md` or pick a topic from the index above.
