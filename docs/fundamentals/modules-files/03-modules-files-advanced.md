<!-- Navigation -->
**[← OOP Principles](../oop/02-oop-principles.md)** | **[Back to Index](../../../README.md)** | **[Web APIs →](../../advanced/web-apis/01-flask-fastapi-rest.md)**

---

# Python Fundamentals: Modules, Files & Advanced Features

## 1.8 Importing Modules

### import Statement

```python
# Import entire module
import math
print(math.pi)           # 3.14159...
print(math.sqrt(16))     # 4.0

# Import with alias
import numpy as np
array = np.array([1, 2, 3])

# Import specific items
from math import pi, sqrt
print(pi)                # 3.14159...
result = sqrt(25)        # 5.0

# Import everything (not recommended)
from math import *
print(ceil(4.3))         # 5
```

### Standard Library Modules

#### math - Mathematical functions
```python
import math

# Constants
print(math.pi)           # 3.14159265359
print(math.e)            # 2.71828182846

# Functions
print(math.sqrt(16))     # 4.0
print(math.pow(2, 3))    # 8.0
print(math.ceil(4.3))    # 5
print(math.floor(4.7))   # 4
print(math.factorial(5)) # 120
print(math.gcd(48, 18))  # 6 (greatest common divisor)
```

#### os - Operating System
```python
import os

# Current working directory
print(os.getcwd())       # /Users/username/projects

# List files
files = os.listdir(".")
print(files)

# Create directory
os.mkdir("new_folder")

# Check if exists
if os.path.exists("new_folder"):
    print("Folder exists")

# Remove directory
os.rmdir("new_folder")

# Path operations
path = os.path.join("folder", "file.txt")
print(path)              # folder/file.txt (or folder\file.txt on Windows)
```

#### sys - System-specific parameters
```python
import sys

# Python version
print(sys.version)       # 3.9.x ...

# Command-line arguments
print(sys.argv)          # ['script.py', arg1, arg2]

# Platform
print(sys.platform)      # darwin, linux, win32

# Add to path
sys.path.append("/custom/path")

# Exit program
# sys.exit(0)            # Exit with code 0 (success)
```

#### datetime - Date and time
```python
from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print(now)               # 2026-09-16 10:30:45.123456

# Create specific datetime
d = datetime(2026, 9, 16, 10, 30)
print(d)

# Date arithmetic
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)

# Format date
print(now.strftime("%Y-%m-%d"))      # 2026-09-16
print(now.strftime("%A, %B %d"))     # Wednesday, September 16
```

#### json - JSON handling
```python
import json

# Convert Python to JSON
data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "JavaScript"]
}

json_string = json.dumps(data, indent=2)
print(json_string)

# Parse JSON
parsed = json.loads(json_string)
print(parsed["name"])    # Alice

# Write to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read from file
with open("data.json", "r") as f:
    loaded_data = json.load(f)
```

---

## 1.9 File Handling

### Opening Files

```python
# Read mode (default)
file = open("file.txt", "r")
content = file.read()
file.close()

# Write mode (overwrites)
file = open("file.txt", "w")
file.write("Hello, World!")
file.close()

# Append mode (adds to end)
file = open("file.txt", "a")
file.write("\nNew line")
file.close()

# Binary mode
file = open("image.png", "rb")  # Read binary
# ...
file.close()
```

### Reading Files

```python
# Read entire file
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline

# Read all lines as list
with open("file.txt", "r") as file:
    lines = file.readlines()
    print(lines[0])  # First line

# Read specific number of characters
with open("file.txt", "r") as file:
    chunk = file.read(50)  # First 50 characters
```

### Writing Files

```python
# Write multiple lines
data = [
    "Alice, 25, Engineer\n",
    "Bob, 30, Manager\n",
    "Charlie, 28, Designer\n"
]

with open("output.txt", "w") as file:
    file.writelines(data)

# Write with formatting
with open("report.txt", "w") as file:
    file.write(f"Report generated\n")
    file.write(f"Total records: 100\n")
```

### Exception Handling with Files

```python
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except IOError as e:
    print(f"Error reading file: {e}")
finally:
    print("File operation completed")

# Better: use with statement (auto-closes)
try:
    with open("file.txt", "r") as file:
        for line in file:
            print(line)
except Exception as e:
    print(f"Error: {e}")
```

### CSV File Handling

```python
import csv

# Write CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "NYC"],
    ["Bob", 30, "LA"],
    ["Charlie", 28, "Chicago"]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Read CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Read as dictionaries (with headers)
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old")
```

---

## 1.10 Decorators

### Function Decorators

A decorator is a function that modifies another function or class.

```python
# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
```

### Decorators with Parameters

```python
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

add(5, 3)
```

### Logging Decorator Example

```python
import functools
import time

def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}")
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        elapsed = time.time() - start_time
        print(f"[LOG] {func.__name__} completed in {elapsed:.2f}s")
        return result
    
    return wrapper

@log_execution
def slow_operation():
    time.sleep(2)
    return "Done"

slow_operation()
```

### Stacking Decorators

```python
def decorator_a(func):
    def wrapper():
        print("A-Before")
        func()
        print("A-After")
    return wrapper

def decorator_b(func):
    def wrapper():
        print("B-Before")
        func()
        print("B-After")
    return wrapper

@decorator_a
@decorator_b
def greet():
    print("Hello!")

greet()
# Output:
# A-Before
# B-Before
# Hello!
# B-After
# A-After
```

### Built-in Decorators

```python
class Calculator:
    def __init__(self):
        self._value = 0
    
    # Property decorator - access as attribute
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        if val >= 0:
            self._value = val
        else:
            print("Value must be non-negative")
    
    # Static method - doesn't use self
    @staticmethod
    def add(a, b):
        return a + b
    
    # Class method - uses cls instead of self
    @classmethod
    def create_default(cls):
        return cls()

calc = Calculator()
calc.value = 10          # Uses setter
print(calc.value)        # Uses getter
print(Calculator.add(5, 3))  # 8
```

---

## 1.11 Generators

### yield Keyword

Generators use `yield` to produce values one at a time, saving memory.

```python
# Regular function returns all at once
def get_numbers_list():
    result = []
    for i in range(5):
        result.append(i)
    return result

# Generator yields one at a time
def get_numbers_generator():
    for i in range(5):
        yield i

# Usage
print(get_numbers_list())        # [0, 1, 2, 3, 4]

for num in get_numbers_generator():
    print(num)                   # Prints 0, 1, 2, 3, 4
```

### Fibonacci Generator

```python
def fibonacci(n):
    """Generate Fibonacci sequence up to n terms"""
    a, b = 0, 1
    count = 0
    
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Usage
for fib_num in fibonacci(10):
    print(fib_num, end=" ")
# Output: 0 1 1 2 3 5 8 13 21 34
```

### Memory Efficiency

```python
import sys

# List - stores all values in memory
list_comp = [x**2 for x in range(1000000)]
print(f"List size: {sys.getsizeof(list_comp)} bytes")

# Generator - computes on demand
def gen_squares():
    for x in range(1000000):
        yield x**2

gen = gen_squares()
print(f"Generator size: {sys.getsizeof(gen)} bytes")
# Generator is much smaller!
```

### Generator Expressions

```python
# List comprehension
squares_list = [x**2 for x in range(5)]
print(squares_list)  # [0, 1, 4, 9, 16]

# Generator expression (similar syntax)
squares_gen = (x**2 for x in range(5))
print(squares_gen)   # <generator object at ...>

# Iterate through generator
for sq in squares_gen:
    print(sq, end=" ")  # 0 1 4 9 16
```

---

## 1.12 Iterators

### __iter__ and __next__

```python
class CountUp:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max_value:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Usage
counter = CountUp(3)
for num in counter:
    print(num)  # 1, 2, 3

# Manual iteration
counter2 = CountUp(3)
print(next(counter2))  # 1
print(next(counter2))  # 2
print(next(counter2))  # 3
# print(next(counter2))  # StopIteration exception
```

### Custom Iterator Example

```python
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

# Usage
rev = Reverse("ABC")
for char in rev:
    print(char, end=" ")  # C B A
```

---

## 1.13 Type Hinting

### Basic Hints

```python
# Variables
name: str = "Alice"
age: int = 25
price: float = 19.99
is_active: bool = True

# No runtime enforcement (just hints for tools)
name = 123  # Works, but IDE/checker warns
```

### Function Annotations

```python
def add(a: int, b: int) -> int:
    """Add two integers"""
    return a + b

def greet(name: str) -> None:
    """Greet someone"""
    print(f"Hello, {name}!")

# With default values
def power(base: int, exponent: int = 2) -> int:
    return base ** exponent
```

### Complex Types

```python
from typing import List, Dict, Tuple, Optional

# List of integers
def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

# Dictionary with string keys and integer values
def count_items(items: Dict[str, int]) -> int:
    return sum(items.values())

# Tuple with specific types
def get_coordinates() -> Tuple[float, float]:
    return (10.5, 20.3)

# Optional - value or None
def find_user(user_id: int) -> Optional[Dict]:
    if user_id > 0:
        return {"id": user_id, "name": "Alice"}
    return None

# Union types - value can be multiple types
from typing import Union

def process_data(data: Union[int, str]) -> str:
    return str(data)
```

---

## 1.14 Data Classes

### @dataclass Decorator

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str

# Auto-generates __init__, __repr__, __eq__
person = Person("Alice", 25, "alice@example.com")
print(person)  # Person(name='Alice', age=25, email='alice@example.com')

# Comparison
person2 = Person("Alice", 25, "alice@example.com")
print(person == person2)  # True
```

### Data Classes with Defaults

```python
from dataclasses import dataclass, field

@dataclass
class Config:
    host: str
    port: int = 8080
    debug: bool = False
    tags: list = field(default_factory=list)

config1 = Config("localhost")
config2 = Config("example.com", 3000, True, ["prod"])

print(config1)
# Config(host='localhost', port=8080, debug=False, tags=[])
```

---

## 1.15 Context Managers

### with Statement

```python
# File automatically closes, even if error occurs
with open("file.txt", "r") as file:
    content = file.read()
    print(content)
# file is closed automatically
```

### Custom Context Manager

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Called when entering with block"""
        self.file = open(self.filename, self.mode)
        print(f"File opened: {self.filename}")
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting with block"""
        if self.file:
            self.file.close()
        print(f"File closed: {self.filename}")
        return False  # Don't suppress exceptions

# Usage
with FileManager("output.txt", "w") as f:
    f.write("Hello, World!")
    # File auto-closes here
```

### Context Manager with contextlib

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering context")
    try:
        yield "resource"
    finally:
        print("Exiting context")

with my_context() as resource:
    print(f"Using {resource}")

# Output:
# Entering context
# Using resource
# Exiting context
```

---

## Mini-Exercise: Log File Analyzer

```python
# Create a decorator that logs function calls
# Read a log file and analyze it

import functools
from datetime import datetime

def log_to_file(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with open(filename, "a") as f:
                f.write(f"[{datetime.now()}] Called {func.__name__}\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_to_file("app.log")
def process_data(data):
    return sum(data)

# Usage
result = process_data([1, 2, 3, 4, 5])
print(f"Result: {result}")

# Read and display log
with open("app.log", "r") as f:
    print("Log contents:")
    print(f.read())
```

---

## Summary Table

| Feature | Purpose | Example |
|---------|---------|---------|
| **Modules** | Reuse code | `import math` |
| **File I/O** | Read/write files | `with open()` |
| **Decorators** | Modify functions | `@my_decorator` |
| **Generators** | Memory-efficient iteration | `yield` keyword |
| **Iterators** | Custom iteration | `__iter__`, `__next__` |
| **Type Hints** | Code clarity | `def func(x: int) -> str:` |
| **Data Classes** | Auto-generate methods | `@dataclass` |
| **Context Managers** | Resource management | `with` statement |

---

<!-- Navigation Footer -->
**[← OOP Principles](../oop/02-oop-principles.md)** | **[Back to Index](../../../README.md)** | **[Web APIs →](../../advanced/web-apis/01-flask-fastapi-rest.md)**

**Sections:** 1.8-1.15 | **Time:** 1-2 hours
