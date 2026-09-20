"""
Sample: Operators
Demonstrates arithmetic, comparison, logical, and assignment operators.
"""

# Arithmetic operators
print("=== Arithmetic ===")
print(f"10 + 5 = {10 + 5}")
print(f"10 - 3 = {10 - 3}")
print(f"4 * 6 = {4 * 6}")
print(f"20 / 4 = {20 / 4}")
print(f"20 // 3 = {20 // 3}")
print(f"20 % 3 = {20 % 3}")
print(f"2 ** 3 = {2 ** 3}")

# Comparison operators
print("\n=== Comparison ===")
print(f"5 == 5: {5 == 5}")
print(f"5 != 3: {5 != 3}")
print(f"5 > 3: {5 > 3}")
print(f"5 >= 5: {5 >= 5}")
print(f"'apple' < 'banana': {'apple' < 'banana'}")

# Logical operators
print("\n=== Logical ===")
age = 25
is_student = True

result = age > 18 and is_student
print(f"age > 18 and is_student: {result}")

result = age < 18 or is_student
print(f"age < 18 or is_student: {result}")

result = not is_student
print(f"not is_student: {result}")

# Assignment operators
print("\n=== Assignment ===")
x = 10
print(f"x = {x}")

x += 5
print(f"x += 5 → x = {x}")

x -= 3
print(f"x -= 3 → x = {x}")

x *= 2
print(f"x *= 2 → x = {x}")

x /= 4
print(f"x /= 4 → x = {x}")
