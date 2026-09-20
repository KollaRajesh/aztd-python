"""
Sample: Functions
Demonstrates function definition, parameters, return values, and closures.
"""

# Basic function
def greet(name):
    return f"Hello, {name}!"

print("=== Basic function ===")
print(greet("Alice"))

# Default parameters
def greet_custom(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print("\n=== Default parameters ===")
print(greet_custom("Alice"))
print(greet_custom("Bob", "Hi"))

# Multiple parameters and return
def add(a, b):
    return a + b

def add_and_multiply(a, b, multiplier):
    total = a + b
    return total * multiplier

print("\n=== Multiple parameters ===")
print(f"add(3, 4) = {add(3, 4)}")
print(f"add_and_multiply(3, 4, 2) = {add_and_multiply(3, 4, 2)}")

# *args (variable positional arguments)
def sum_all(*numbers):
    return sum(numbers)

print("\n=== *args ===")
print(f"sum_all(1, 2, 3, 4) = {sum_all(1, 2, 3, 4)}")

# **kwargs (variable keyword arguments)
def print_info(**info):
    for key, value in info.items():
        print(f"  {key}: {value}")

print("\n=== **kwargs ===")
print_info(name="Alice", age=30, city="NYC")

# Scope
print("\n=== Scope ===")
x = "global"

def outer():
    x = "outer"
    
    def inner():
        x = "inner"
        print(f"  inner x: {x}")
    
    inner()
    print(f"  outer x: {x}")

outer()
print(f"global x: {x}")

# Closures
print("\n=== Closures ===")
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

times_3 = make_multiplier(3)
times_5 = make_multiplier(5)

print(f"times_3(10) = {times_3(10)}")
print(f"times_5(10) = {times_5(10)}")
