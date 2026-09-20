# Python Quick Reference Card

Quick lookup for common syntax, patterns, and solutions. Keep this handy while coding.

---

## Data Types

### Numbers
```python
# Integers
x = 5
y = -10
z = 0

# Floats
pi = 3.14
temp = -15.5

# Operations
2 + 3          # 5
2 - 3          # -1
2 * 3          # 6
2 / 3          # 0.666...
2 ** 3         # 8 (power)
2 % 3          # 2 (modulo)
2 // 3         # 0 (floor division)
```

### Strings
```python
# Creation
s = "hello"
s = 'hello'
s = """multi
line"""

# Operations
s + " world"              # Concatenation
s * 3                     # Repetition
len(s)                    # Length
s[0]                      # Character access
s[1:4]                    # Slicing
s.upper()                 # Methods
s.lower()
s.split()
s.replace("o", "a")
s.startswith("he")
s.endswith("lo")

# F-strings (formatted)
name = "Alice"
age = 30
f"Name: {name}, Age: {age}"
f"Double: {age * 2}"
```

### Lists
```python
# Creation
lst = [1, 2, 3]
lst = list()              # Empty list
lst = list(range(5))      # [0, 1, 2, 3, 4]

# Operations
lst[0]                    # Access
lst[-1]                   # Last element
lst[1:3]                  # Slice [2, 3]
len(lst)                  # Length
lst.append(4)             # Add element
lst.extend([5, 6])        # Add multiple
lst.insert(0, 0)          # Insert at index
lst.remove(2)             # Remove value
lst.pop()                 # Remove last
lst.pop(0)                # Remove at index
lst.clear()               # Empty list
lst.sort()                # Sort in-place
sorted(lst)               # Sort (new list)
lst.reverse()             # Reverse
lst.index(2)              # Find index
lst.count(2)              # Count occurrences

# Iteration
for item in lst:
    print(item)

# List comprehension
squares = [x**2 for x in lst]
evens = [x for x in lst if x % 2 == 0]
```

### Tuples (Immutable Lists)
```python
# Creation
t = (1, 2, 3)
t = tuple([1, 2, 3])
t = 1, 2, 3               # Parentheses optional

# Operations (same as list, but can't modify)
t[0]                      # Access
len(t)                    # Length
t.count(1)                # Count
t.index(2)                # Find index

# Unpacking
a, b, c = (1, 2, 3)
a, *rest = [1, 2, 3, 4]  # a=1, rest=[2,3,4]
```

### Dictionaries
```python
# Creation
d = {"name": "Alice", "age": 30}
d = dict()                # Empty
d = dict(name="Bob", age=25)

# Operations
d["name"]                 # Access
d.get("name")             # Safe access
d.get("missing", "N/A")   # With default
d["city"] = "NYC"         # Add/update
d.pop("age")              # Remove and return
del d["city"]             # Delete
"name" in d               # Check existence
d.keys()                  # Get keys
d.values()                # Get values
d.items()                 # Get key-value pairs
d.clear()                 # Empty dictionary

# Iteration
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)

# Dict comprehension
squares = {x: x**2 for x in range(5)}
```

### Sets
```python
# Creation
s = {1, 2, 3}
s = set()                 # Empty set
s = set([1, 2, 3])

# Operations
len(s)                    # Size
s.add(4)                  # Add
s.remove(2)               # Remove (error if missing)
s.discard(2)              # Remove (no error)
s.pop()                   # Remove and return
s.clear()                 # Empty

# Set operations
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1 & s2                   # Intersection {2, 3}
s1 | s2                   # Union {1, 2, 3, 4}
s1 - s2                   # Difference {1}
s1 ^ s2                   # Symmetric diff {1, 4}

# Membership
1 in s                    # True
5 not in s                # True

# Iteration
for item in s:
    print(item)
```

---

## Control Flow

### If/Elif/Else
```python
if x > 10:
    print("Large")
elif x > 5:
    print("Medium")
else:
    print("Small")

# One-liner
result = "yes" if x > 5 else "no"
```

### Loops
```python
# For loop
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for item in [1, 2, 3]:
    print(item)

for key, value in {"a": 1, "b": 2}.items():
    print(key, value)

# While loop
while x > 0:
    print(x)
    x -= 1

# Break and continue
for i in range(10):
    if i == 5:
        break             # Exit loop
    if i == 2:
        continue          # Skip iteration
    print(i)

# Else clause
for i in range(5):
    if i == 10:
        break
else:
    print("Completed without break")
```

### Comparisons
```python
x == y                    # Equal
x != y                    # Not equal
x > y                     # Greater than
x < y                     # Less than
x >= y                    # Greater or equal
x <= y                    # Less or equal

# Boolean operators
x > 5 and x < 10          # Both true
x > 5 or x < 2            # At least one true
not x                     # Negation

# Membership
x in [1, 2, 3]            # True if x is 1, 2, or 3
x not in [1, 2, 3]        # Opposite
```

---

## Functions

### Definition
```python
# Basic
def greet():
    print("Hello")

# With parameters
def greet(name):
    print(f"Hello {name}")

# With return
def add(a, b):
    return a + b

# With defaults
def greet(name="Friend"):
    print(f"Hello {name}")

# Multiple returns
def get_min_max(lst):
    return min(lst), max(lst)

# Variable arguments
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)       # 10

# Keyword arguments
def create_user(name, age=18, active=True):
    pass

# Dictionary unpacking
def func(a, b, c):
    pass

params = {"a": 1, "b": 2, "c": 3}
func(**params)

# Type hints
def add(a: int, b: int) -> int:
    return a + b
```

### Lambda Functions
```python
# Simple function
double = lambda x: x * 2
double(5)                 # 10

# With map
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))

# With filter
evens = list(filter(lambda x: x % 2 == 0, numbers))

# With sort
data = [(2, 'b'), (1, 'a'), (3, 'c')]
sorted(data, key=lambda x: x[0])
```

---

## Classes & OOP

### Basic Class
```python
class Dog:
    species = "Canis familiaris"  # Class variable
    
    def __init__(self, name):
        self.name = name           # Instance variable
    
    def bark(self):
        print(f"{self.name} says woof!")
    
    def __str__(self):
        return f"Dog({self.name})"

# Usage
dog = Dog("Buddy")
dog.bark()
print(dog)
```

### Inheritance
```python
class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

### Properties
```python
class User:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if len(value) > 0:
            self._name = value
    
    @name.deleter
    def name(self):
        del self._name

user = User("Alice")
print(user.name)
user.name = "Bob"
```

### Static & Class Methods
```python
class Counter:
    count = 0
    
    @classmethod
    def increment(cls):
        cls.count += 1
    
    @staticmethod
    def is_positive(n):
        return n > 0

Counter.increment()
Counter.is_positive(-5)
```

---

## File Operations

### Reading Files
```python
# Read entire file
with open("file.txt") as f:
    content = f.read()

# Read lines
with open("file.txt") as f:
    lines = f.readlines()

# Read line by line
with open("file.txt") as f:
    for line in f:
        print(line.strip())
```

### Writing Files
```python
# Write (overwrites)
with open("file.txt", "w") as f:
    f.write("Hello")

# Append
with open("file.txt", "a") as f:
    f.write("\nWorld")

# Multiple writes
with open("file.txt", "w") as f:
    f.writelines(["Line 1\n", "Line 2\n"])
```

### Working with JSON
```python
import json

# Read JSON
with open("data.json") as f:
    data = json.load(f)

# Write JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Parse JSON string
data = json.loads('{"name": "Alice"}')

# Convert to JSON string
json_str = json.dumps(data)
```

### CSV Files
```python
import csv

# Read CSV
with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Read as dictionaries
with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# Write CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 30])
```

---

## Error Handling

### Try/Except
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple exceptions
try:
    data = {"key": "value"}
    value = data["missing"]
except KeyError:
    print("Key not found")
except Exception as e:
    print(f"Error: {e}")

# Else clause
try:
    value = int(user_input)
except ValueError:
    print("Invalid input")
else:
    print(f"Got: {value}")

# Finally clause
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    file.close()  # Always runs

# Raise exceptions
if age < 0:
    raise ValueError("Age cannot be negative")
```

---

## Common Patterns

### Checking Existence
```python
# Dictionary
if "key" in d:
    value = d["key"]

# List
if item in lst:
    index = lst.index(item)

# String
if substring in string:
    pass

# Safe dictionary access
value = d.get("key", "default")
```

### Looping with Index
```python
# Old way
for i in range(len(lst)):
    print(i, lst[i])

# Better way
for i, item in enumerate(lst):
    print(i, item)
```

### Zipping Lists
```python
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

### Sorting
```python
# Numbers
numbers = [3, 1, 4, 1, 5, 9]
sorted(numbers)           # [1, 1, 3, 4, 5, 9]

# Reverse
sorted(numbers, reverse=True)

# Custom key
data = [(2, "b"), (1, "a"), (3, "c")]
sorted(data, key=lambda x: x[0])
sorted(data, key=lambda x: x[1])

# Strings
names = ["Charlie", "Alice", "Bob"]
sorted(names)             # Alphabetical

# Case-insensitive
sorted(names, key=str.lower)
```

---

## Useful Functions

### Built-in Functions
```python
# Type conversion
int("42")                 # 42
float("3.14")             # 3.14
str(42)                   # "42"
bool(1)                   # True
list("abc")               # ['a', 'b', 'c']

# Length and size
len([1, 2, 3])            # 3
len("hello")              # 5

# Min and max
min([3, 1, 4, 1, 5])      # 1
max([3, 1, 4, 1, 5])      # 5

# Sum and average
sum([1, 2, 3, 4])         # 10
sum([1, 2, 3, 4]) / 4     # 2.5

# Range
list(range(5))            # [0, 1, 2, 3, 4]
list(range(2, 5))         # [2, 3, 4]
list(range(0, 10, 2))     # [0, 2, 4, 6, 8]

# Any and all
any([False, True, False]) # True
all([True, True, True])   # True

# Sorted
sorted([3, 1, 4, 1, 5])   # [1, 1, 3, 4, 5]

# Reversed
list(reversed([1, 2, 3])) # [3, 2, 1]

# Enumerate
list(enumerate(['a', 'b', 'c']))
# [(0, 'a'), (1, 'b'), (2, 'c')]

# Zip
list(zip([1, 2], ['a', 'b']))
# [(1, 'a'), (2, 'b')]

# Map and filter
list(map(str, [1, 2, 3])) # ['1', '2', '3']
list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
# [2, 4]
```

### String Methods
```python
s = "Hello World"

# Case
s.upper()                 # "HELLO WORLD"
s.lower()                 # "hello world"
s.capitalize()            # "Hello world"
s.title()                 # "Hello World"

# Searching
s.find("World")           # 6 (index)
s.find("xyz")             # -1 (not found)
"World" in s              # True

# Replacing
s.replace("World", "Python")

# Splitting and joining
s.split()                 # ['Hello', 'World']
s.split(" ")              # ['Hello', 'World']
"-".join(['a', 'b', 'c']) # 'a-b-c'

# Stripping whitespace
"  hello  ".strip()       # 'hello'
"  hello  ".lstrip()      # 'hello  '
"  hello  ".rstrip()      # '  hello'

# Checking
s.startswith("Hello")     # True
s.endswith("World")       # True
s.isdigit()               # False
s.isalpha()               # False
s.isalnum()               # False
```

---

## Common Imports

### Collections
```python
from collections import defaultdict, Counter, namedtuple

# defaultdict - default values
d = defaultdict(list)
d['key'].append('value')

# Counter - count occurrences
counts = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
counts['a']               # 3

# namedtuple - named fields
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
p.x                       # 1
```

### Itertools
```python
from itertools import combinations, permutations, product

list(combinations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 3)]

list(permutations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

list(product([1, 2], ['a', 'b']))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

### Functools
```python
from functools import reduce, lru_cache

# Reduce
reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 10

# Cache function results
@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

### DateTime
```python
from datetime import datetime, timedelta, date

# Current time
now = datetime.now()
today = date.today()

# Parsing
dt = datetime.strptime("2024-01-15", "%Y-%m-%d")

# Formatting
now.strftime("%Y-%m-%d %H:%M:%S")

# Arithmetic
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
```

---

## Slicing Cheat Sheet

```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst[2:5]                  # [2, 3, 4]
lst[:3]                   # [0, 1, 2]
lst[5:]                   # [5, 6, 7, 8, 9]
lst[-2:]                  # [8, 9]
lst[:-2]                  # [0, 1, 2, 3, 4, 5, 6, 7]
lst[::2]                  # [0, 2, 4, 6, 8] (every 2nd)
lst[1::2]                 # [1, 3, 5, 7, 9] (every 2nd, start at 1)
lst[::-1]                 # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)
```

---

## Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `NameError` | Variable not defined | Define before use |
| `TypeError` | Wrong data type | Check type, convert if needed |
| `IndexError` | Index out of range | Check list length |
| `KeyError` | Dictionary key missing | Use `.get()` or check with `in` |
| `ValueError` | Invalid value | Validate input |
| `ZeroDivisionError` | Divide by zero | Check for zero |
| `AttributeError` | Object has no attribute | Check object type |
| `FileNotFoundError` | File doesn't exist | Check file path |
| `SyntaxError` | Code syntax wrong | Check for typos, colons, indentation |
| `IndentationError` | Wrong indentation | Use 4 spaces consistently |

---

## Performance Tips

```python
# ✅ Fast: List comprehension
[x**2 for x in range(1000)]

# ❌ Slow: Loop and append
result = []
for x in range(1000):
    result.append(x**2)

# ✅ Fast: Set membership
if x in {1, 2, 3}:
    pass

# ❌ Slow: List membership
if x in [1, 2, 3]:
    pass

# ✅ Fast: Join strings
"-".join(["a", "b", "c"])

# ❌ Slow: Concatenate strings
result = ""
for s in ["a", "b", "c"]:
    result += s
```

---

## Keep This Handy!

Bookmark this file for quick reference while coding. When you forget syntax, come here first!

**Tip:** Copy these patterns and modify them for your needs.

*Last updated: September 16, 2026*
