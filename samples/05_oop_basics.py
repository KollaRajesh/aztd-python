"""
Sample: Object-oriented programming basics
Demonstrates classes, inheritance, and polymorphism.
"""

# Basic class
print("=== Basic Class ===")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says: Woof!"

dog = Dog("Rex", 3)
print(f"Name: {dog.name}, Age: {dog.age}")
print(dog.bark())

# Inheritance
print("\n=== Inheritance ===")

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())

# Polymorphism
print("\n=== Polymorphism ===")

animals = [
    Dog("Rex"),
    Cat("Whiskers"),
    Dog("Buddy")
]

for animal in animals:
    print(f"{animal.name}: {animal.speak()}")

# Class with multiple methods
print("\n=== Class Methods ===")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

account = BankAccount("Alice", 100)
print(account.deposit(50))
print(account.withdraw(30))
print(account.withdraw(200))
