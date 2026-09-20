"""
Sample: Variables and types
Demonstrates basic Python types and type checking.
"""

# Basic variables and types
name = "Alice"
age = 30
height = 5.7
is_active = True
no_value = None

print(f"Name: {name} (type: {type(name).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Height: {height} (type: {type(height).__name__})")
print(f"Active: {is_active} (type: {type(is_active).__name__})")
print(f"None: {no_value} (type: {type(no_value).__name__})")

# Type conversion
num_str = "42"
num = int(num_str)
print(f"\nConverted '{num_str}' to {num} + 8 = {num + 8}")

price = 19.99
price_str = str(price)
print(f"Converted {price} to '{price_str}'")

# Type checking
print(f"\nType checks:")
print(f"isinstance(age, int): {isinstance(age, int)}")
print(f"isinstance(price, float): {isinstance(price, float)}")
print(f"isinstance(name, str): {isinstance(name, str)}")

# Naming conventions (PEP 8)
user_name = "Bob"
MAX_RETRIES = 3
temperature = 98.6

print(f"\nNaming: user_name={user_name}, MAX_RETRIES={MAX_RETRIES}, temperature={temperature}")
