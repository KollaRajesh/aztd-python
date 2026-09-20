"""
Sample: Data structures
Demonstrates lists, dicts, sets, and tuples.
"""

# Lists
print("=== Lists ===")
fruits = ["apple", "banana", "cherry"]
print(f"List: {fruits}")
print(f"First: {fruits[0]}")

fruits.append("date")
print(f"After append: {fruits}")

fruits.insert(1, "blueberry")
print(f"After insert: {fruits}")

fruits.remove("banana")
print(f"After remove: {fruits}")

# Dictionaries
print("\n=== Dictionaries ===")
user = {"name": "Alice", "age": 30, "city": "NYC"}
print(f"Dict: {user}")
print(f"Name: {user['name']}")

user["email"] = "alice@example.com"
print(f"After adding email: {user}")

for key, value in user.items():
    print(f"  {key}: {value}")

# Sets
print("\n=== Sets ===")
tags = {"python", "coding", "tutorial"}
print(f"Set: {tags}")

tags.add("python")  # No effect, already exists
tags.add("data-science")
print(f"After add: {tags}")

set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(f"\nSet operations:")
print(f"  A & B (intersection): {set_a & set_b}")
print(f"  A | B (union): {set_a | set_b}")
print(f"  A - B (difference): {set_a - set_b}")

# Tuples
print("\n=== Tuples ===")
coordinates = (10, 20)
print(f"Tuple: {coordinates}")
print(f"First: {coordinates[0]}")

x, y = coordinates
print(f"Unpacked: x={x}, y={y}")

def get_user():
    return ("Alice", 30, "NYC")

name, age, city = get_user()
print(f"\nUnpacked from function: {name}, {age}, {city}")
