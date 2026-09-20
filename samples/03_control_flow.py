"""
Sample: Control flow
Demonstrates if/elif/else, for loops, while loops, break, and continue.
"""

# If/elif/else
print("=== If/elif/else ===")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# For loop
print("\n=== For loop ===")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  {fruit}")

# For with range
print("\nRange 0-4:")
for i in range(5):
    print(f"  {i}", end=" ")
print()

# For with enumerate
print("\nEnumerate:")
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

# While loop
print("\n=== While loop ===")
count = 0
while count < 3:
    print(f"  count = {count}")
    count += 1

# Break and continue
print("\n=== Break ===")
for i in range(10):
    if i == 5:
        break
    print(f"  {i}", end=" ")
print(" (stopped at 5)")

print("\n=== Continue ===")
for i in range(5):
    if i == 2:
        continue
    print(f"  {i}", end=" ")
print(" (skipped 2)")
