"""
Sample: Error handling
Demonstrates try/except/else/finally and custom exceptions.
"""

# Basic try/except
print("=== Basic try/except ===")
try:
    num = int("abc")
except ValueError:
    print("ValueError: Cannot convert 'abc' to int")

# Catching multiple exceptions
print("\n=== Multiple exceptions ===")
try:
    result = 10 / 0
except (ValueError, ZeroDivisionError) as e:
    print(f"Caught {type(e).__name__}: {e}")

# Try/except/else/finally
print("\n=== Try/except/else/finally ===")
try:
    file = open("test_file.txt", "w")
    file.write("test content")
except FileNotFoundError:
    print("File not found")
else:
    print("File written successfully")
finally:
    if 'file' in locals():
        file.close()
    print("Finally block executed (cleanup)")

# Custom exceptions
print("\n=== Custom exceptions ===")

class InvalidAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    if age > 150:
        raise InvalidAgeError("Age seems unrealistic")
    return age

try:
    age = set_age(-5)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")

try:
    age = set_age(200)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")

# Exception hierarchy
print("\n=== Exception hierarchy ===")
try:
    num = int("abc")
except ValueError:
    print("Specific: ValueError caught")
except Exception:
    print("General: Exception caught")

# Context manager for file handling
print("\n=== Context manager ===")
try:
    with open("test_file.txt", "r") as file:
        content = file.read()
        print(f"Read: {content}")
except FileNotFoundError:
    print("FileNotFoundError: File not found")

# Cleanup
import os
if os.path.exists("test_file.txt"):
    os.remove("test_file.txt")
