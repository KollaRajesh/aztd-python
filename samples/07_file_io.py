"""
Sample: File I/O
Demonstrates reading and writing files.
"""

# Write to file
print("=== Write to file ===")
with open("sample_data.txt", "w") as file:
    file.write("Line 1: Hello, World!\n")
    file.write("Line 2: Python is great\n")
    file.write("Line 3: File I/O example\n")

print("File written: sample_data.txt")

# Read entire file
print("\n=== Read entire file ===")
with open("sample_data.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
print("=== Read line by line ===")
with open("sample_data.txt", "r") as file:
    for line in file:
        print(f"  {line.strip()}")

# Read all lines into list
print("\n=== Read all lines ===")
with open("sample_data.txt", "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines, 1):
        print(f"  Line {i}: {line.strip()}")

# Append to file
print("\n=== Append to file ===")
with open("sample_data.txt", "a") as file:
    file.write("Line 4: Appended line\n")

print("Appended to file")

# Read after append
with open("sample_data.txt", "r") as file:
    content = file.read()
    print("\nUpdated file content:")
    print(content)

# Working with CSV
print("\n=== CSV Operations ===")
import csv

# Write CSV
rows = [["name", "age", "city"], ["Alice", 30, "NYC"], ["Bob", 25, "LA"]]
with open("sample_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("CSV file created: sample_data.csv")

# Read CSV
print("\nReading CSV:")
with open("sample_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"  {row}")

# Cleanup
import os
os.remove("sample_data.txt")
os.remove("sample_data.csv")
print("\nCleanup: removed sample files")
