# Module Usage Guides

Focused guides for 16 essential Python modules with simple, medium, and complex examples.

## Quick Links

### Data & Databases
- **01-sqlalchemy.md** - ORM for database operations | `pip install sqlalchemy`
- **04-dotenv.md** - Environment variable management | `pip install python-dotenv`

### Data Science & Visualization
- **07-numpy.md** - Numerical computing and arrays | `pip install numpy`
- **08-pandas.md** - Data analysis and manipulation | `pip install pandas`
- **09-matplotlib.md** - Data visualization | `pip install matplotlib`
- **11-scikit-learn.md** - Machine learning models | `pip install scikit-learn`

### Web Scraping & HTTP
- **03-beautifulsoup4.md** - HTML/XML parsing | `pip install beautifulsoup4`
- **05-requests.md** - HTTP client for APIs | `pip install requests`
- **06-aiohttp.md** - Async HTTP requests | `pip install aiohttp`

### Validation & Configuration
- **02-pydantic.md** - Data validation with type hints | `pip install pydantic`

### Web Frameworks
- **12-flask.md** - Lightweight web framework | `pip install flask`
- **13-fastapi.md** - High-performance async API | `pip install fastapi uvicorn`
- **14-django.md** - Full-stack web framework | `pip install django`

### Testing & Quality
- **10-pytest.md** - Unit testing framework | `pip install pytest`

### AI & LLMs
- **15-langchain.md** - LLM application framework | `pip install langchain openai`

## Format

Each guide follows the same structure:
- **Simple** - Basic usage and getting started
- **Medium** - Real-world patterns and intermediate features
- **Complex** - Advanced techniques and production scenarios

All code examples are production-ready and follow PEP 8 conventions.

## Installation

Install all modules at once:
```bash
pip install sqlalchemy pydantic beautifulsoup4 python-dotenv aiohttp requests numpy pandas matplotlib flask fastapi uvicorn django pytest scikit-learn langchain openai
```

Or install by category:
```bash
# Web frameworks
pip install flask fastapi uvicorn django

# Data science
pip install numpy pandas matplotlib scikit-learn

# HTTP & scraping
pip install requests aiohttp beautifulsoup4

# Testing & validation
pip install pytest pydantic

# AI & LLMs
pip install langchain openai
```

## Usage Tips

- Start with the **Simple** example to understand basic concepts
- Move to **Medium** when ready for real-world patterns
- Reference **Complex** for production scenarios and optimization

Each module page includes installation instructions and typical use cases.
