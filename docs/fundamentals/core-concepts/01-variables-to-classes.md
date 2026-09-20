<!-- Navigation -->
**[← Back to Index](../../../README.md)** | **[Fundamentals Home](#)** | **[Next: OOP Principles →](../oop/02-oop-principles.md)**

---

# Python Fundamentals: Core Concepts

## 1.1 Variables

### Definition
Variables are named storage locations that hold data values. Python uses dynamic typing, meaning you don't declare a variable's type—it's inferred from the value assigned.

### Naming Rules
- Start with letter (a-z, A-Z) or underscore (_)
- Can contain letters, numbers, underscores
- Case-sensitive (age ≠ Age)
- Avoid Python keywords (if, for, while, etc.)
- Follow PEP 8: use lowercase with underscores (snake_case)

### Dynamic Typing Example

```python
# Variable type determined by assigned value
x = 5              # int
x = "hello"        # str (type changed)
x = 3.14           # float

print(type(x))     # <class 'float'>
```

### Best Practices

```python
# Good naming
user_age = 25
is_active = True
total_price = 99.99

# Avoid
x = 25             # Too vague
X = 25             # Confusing with lowercase
userAge = 25       # Use snake_case, not camelCase
```

### Real-World Example

```python
# Banking application
account_holder = "Alice"
balance = 1500.50
is_premium_member = True
transaction_count = 12

print(f"Account: {account_holder}, Balance: ${balance}")
```

---

## 1.2 Data Types

### Basic Types

#### Integer (int)
```python
age = 25
negative = -10
large_number = 1_000_000  # Underscore for readability

print(type(age))  # <class 'int'>
```

#### Float
```python
price = 19.99
temperature = -5.5
scientific = 1.5e-3  # 0.0015

print(price + 1.01)  # 21.0
```

#### String (str)
```python
name = "Alice"
greeting = 'Hello'
multiline = """This is
a multiline
string"""

# String operations
text = "Python"
print(text.upper())      # PYTHON
print(text.lower())      # python
print(len(text))         # 6
print(text[0])           # P
```

#### Boolean (bool)
```python
is_student = True
is_admin = False

# Logical operations
result = is_student and not is_admin  # True
```

### Collections

#### Lists (Ordered, Mutable)
```python
# Create and access
fruits = ["apple", "banana", "orange"]
print(fruits[0])       # apple
print(len(fruits))     # 3

# Modify
fruits.append("grape")
fruits.remove("banana")
fruits[0] = "blueberry"

# Iteration
for fruit in fruits:
    print(fruit)

# List methods
fruits.sort()
fruits.reverse()
```

#### Dictionaries (Key-Value, Mutable)
```python
# Create
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

# Access
print(person["name"])      # Alice
print(person.get("age"))   # 25

# Modify
person["age"] = 26
person["email"] = "alice@example.com"

# Iterate
for key, value in person.items():
    print(f"{key}: {value}")
```

#### Sets (Unique, Unordered, Mutable)
```python
# Create
colors = {"red", "blue", "green"}

# Add/Remove
colors.add("yellow")
colors.remove("red")

# Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a & set_b)     # {3} - intersection
print(set_a | set_b)     # {1,2,3,4,5} - union
print(set_a - set_b)     # {1,2} - difference
```

#### Tuples (Ordered, Immutable)
```python
# Create
coordinates = (10, 20)
person_info = ("Alice", 25, "Engineer")

# Access (like lists)
print(coordinates[0])    # 10
print(len(person_info))  # 3

# Cannot modify
# coordinates[0] = 15    # Error!

# Unpacking
x, y = coordinates
name, age, job = person_info
print(f"{name} is {age} and works as {job}")
```

### Type Conversion

```python
# String to integer
age_str = "25"
age_int = int(age_str)   # 25

# Integer to string
number = 42
text = str(number)       # "42"

# String to float
price_str = "19.99"
price = float(price_str) # 19.99

# List to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)

# To boolean
print(bool(1))           # True
print(bool(0))           # False
print(bool("text"))      # True
print(bool(""))          # False
```

### Mini-Exercise

```python
# Create a student record with name, age, grade, and subjects (list)
# Print the information in a formatted way

student = {
    "name": "Bob",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Physics", "Chemistry"]
}

print(f"Student: {student['name']}")
print(f"Age: {student['age']}")
print(f"Subjects: {', '.join(student['subjects'])}")
```

---

## 1.3 Control Flow

### if, elif, else

```python
age = 25

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")
```

### for Loops

```python
# Iterate over list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Using range
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)

# With enumeration
items = ["a", "b", "c"]
for index, item in enumerate(items):
    print(f"{index}: {item}")
```

### while Loops

```python
count = 0
while count < 5:
    print(count)
    count += 1

# With condition
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")
```

### break and continue

```python
# break - exit loop
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue - skip iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4
```

### Real-World Example

```python
# Grade calculator
scores = [85, 92, 78, 95, 88]
total = 0

for score in scores:
    if score < 70:
        print(f"Score {score} is failing")
        continue
    total += score

average = total / len(scores)
print(f"Average: {average:.2f}")
```

---

## 1.4 Logical Operators

### and, or, not

```python
# and - both must be True
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")

# or - at least one must be True
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today")

# not - negates value
is_raining = False

if not is_raining:
    print("Go outside")
```

### Truth Tables

```python
# and operator
print(True and True)      # True
print(True and False)     # False
print(False and False)    # False

# or operator
print(True or False)      # True
print(False or False)     # False

# not operator
print(not True)           # False
print(not False)          # True
```

### Practical Example

```python
# Login validation
username = "alice"
password = "secret123"
is_admin = True

if (username == "alice" and password == "secret123") or is_admin:
    print("Login successful")
else:
    print("Login failed")

# User permission check
is_owner = True
is_moderator = False

if is_owner or is_moderator:
    print("Can delete post")
```

---

## 1.5 Functions

### Defining Functions

```python
def greet():
    print("Hello!")

greet()  # Call function
```

### Parameters and Return Values

```python
def add(a, b):
    """Add two numbers and return result"""
    result = a + b
    return result

sum_value = add(5, 3)
print(sum_value)  # 8

# Multiple return values
def divide_with_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

q, r = divide_with_remainder(17, 5)
print(f"Quotient: {q}, Remainder: {r}")
```

### Default Parameters

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                # Hello, Alice!
greet("Bob", "Hi")            # Hi, Bob!
```

### *args and **kwargs

```python
# *args for variable number of positional arguments
def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_numbers(1, 2, 3))       # 6
print(sum_numbers(1, 2, 3, 4, 5)) # 15

# **kwargs for variable keyword arguments
def print_config(**options):
    for key, value in options.items():
        print(f"{key}: {value}")

print_config(debug=True, theme="dark", language="en")
```

### Recursive Functions

```python
# Factorial: 5! = 5 * 4 * 3 * 2 * 1 = 120
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

# Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # 8
```

### Lambda Functions

```python
# Anonymous function for simple operations
square = lambda x: x ** 2
print(square(5))  # 25

# With multiple parameters
add = lambda x, y: x + y
print(add(3, 4))  # 7

# Common use: with map, filter, sort
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)  # Sort by grade (highest first)
```

### Best Practices

```python
# Use docstrings
def calculate_area(radius):
    """
    Calculate circle area given radius.
    
    Args:
        radius: Circle radius (float)
    
    Returns:
        Circle area (float)
    """
    import math
    return math.pi * radius ** 2

# Type hints (Python 3.5+)
def add_numbers(a: int, b: int) -> int:
    return a + b

# Handle edge cases
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

---

## 1.6 Classes & Objects

### Class Definition

```python
class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor - initializes object
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age
    
    # Method
    def bark(self):
        print(f"{self.name} says: Woof!")
    
    def get_age(self):
        return self.age

# Create instances
dog1 = Dog("Rex", 3)
dog2 = Dog("Buddy", 5)

# Access attributes
print(dog1.name)       # Rex
print(dog1.species)    # Canis familiaris

# Call methods
dog1.bark()            # Rex says: Woof!
print(dog2.get_age())  # 5
```

### Public, Protected, Private Attributes

```python
class BankAccount:
    def __init__(self, account_number, balance):
        # Public - accessible everywhere
        self.account_number = account_number
        
        # Protected - by convention, prefix with _ (single underscore)
        self._balance = balance
        
        # Private - prefix with __ (double underscore)
        self.__pin = "1234"
    
    def deposit(self, amount):
        self._balance += amount
        return self._balance
    
    def check_balance(self):
        return self._balance
    
    def verify_pin(self, entered_pin):
        return self.__pin == entered_pin

account = BankAccount("123456", 1000)
print(account.account_number)  # Public: works
print(account._balance)        # Protected: works (but don't do this)
# print(account.__pin)         # Private: Error (name mangling)
```

### Methods

```python
class Calculator:
    def __init__(self):
        self.result = 0
    
    # Instance method
    def add(self, x):
        self.result += x
        return self.result
    
    # Class method
    @classmethod
    def from_value(cls, initial_value):
        calc = cls()
        calc.result = initial_value
        return calc
    
    # Static method
    @staticmethod
    def multiply(a, b):
        return a * b
    
    # String representation
    def __str__(self):
        return f"Calculator(result={self.result})"

# Instance method
calc = Calculator()
calc.add(5)

# Class method
calc2 = Calculator.from_value(10)

# Static method
print(Calculator.multiply(3, 4))  # 12
```

---

## Mini-Exercise

```python
# Create a Rectangle class with:
# - width and height attributes
# - area() method
# - perimeter() method
# - __str__() method

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

rect = Rectangle(5, 3)
print(rect)                    # Rectangle(5x3)
print(f"Area: {rect.area()}")  # Area: 15
print(f"Perimeter: {rect.perimeter()}")  # Perimeter: 16
```

---

<!-- Navigation Footer -->
**[← Back to Index](../../../README.md)** | **[Next: OOP Principles →](../oop/02-oop-principles.md)**

**Sections:** 1.1-1.6 | **Time:** 1-2 hours
