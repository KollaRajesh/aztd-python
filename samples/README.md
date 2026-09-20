# Samples

Runnable Python code examples accompanying documentation topics.

## Fundamentals

Learn core Python with executable examples.

| File | Topic | Run |
|------|-------|-----|
| `01_variables_types.py` | Variables and types | `python 01_variables_types.py` |
| `02_operators.py` | Operators | `python 02_operators.py` |
| `03_control_flow.py` | Control flow (if/else, loops) | `python 03_control_flow.py` |
| `04_functions.py` | Functions, scope, closures | `python 04_functions.py` |
| `05_oop_basics.py` | Classes, inheritance, polymorphism | `python 05_oop_basics.py` |
| `06_data_structures.py` | Lists, dicts, sets, tuples | `python 06_data_structures.py` |
| `07_file_io.py` | Reading/writing files | `python 07_file_io.py` |
| `08_error_handling.py` | Try/except, exceptions | `python 08_error_handling.py` |
| `09_testing.py` | Unit tests (unittest, pytest) | `python 09_testing.py` |

## Advanced

Build production systems with proven patterns.

| File | Topic | Run |
|------|-------|-----|
| `01_flask_basic.py` | Flask web app basics | `python 01_flask_basic.py` |
| `02_fastapi_basic.py` | FastAPI REST API | `uvicorn 02_fastapi_basic:app --reload` |
| `02_operators.py` | Design patterns | `python 02_operators.py` |
| `06_design_patterns.py` | Decorator, factory, singleton, observer | `python 06_design_patterns.py` |

## Quick start

Run any example:

```bash
cd samples
python 01_variables_types.py
```

Or with specific topic:

```bash
# Fundamentals
python 04_functions.py

# Advanced
uvicorn 02_fastapi_basic:app --reload
```

## Install dependencies

For advanced samples:

```bash
pip install flask fastapi uvicorn
```

For data science:

```bash
pip install numpy pandas matplotlib
```

For LLM/AI:

```bash
pip install langchain langchain-openai langgraph
```

## Notes

- Each sample is standalone and runs independently.
- Output shows the concept in action.
- Modify examples locally to experiment.
- Check corresponding documentation for explanations.
