<!-- Navigation -->
**[← Core Concepts](../core-concepts/01-variables-to-classes.md)** | **[Back to Index](../../../README.md)** | **[Modules & Files →](../modules-files/03-modules-files-advanced.md)**

---

# Python Fundamentals: Object-Oriented Programming

## 1.7 Object-Oriented Programming Principles

### Encapsulation

Bundling data (attributes) and methods (functions) together, hiding internal details from outside.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # Protected
    
    def deposit(self, amount):
        """Public method to modify private data"""
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        """Public method to modify private data"""
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        """Public method to access private data"""
        return self._balance

# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)           # Allowed
account.withdraw(200)          # Allowed
print(account.get_balance())   # 1300
# account._balance = 999999    # Bad practice (direct access)
```

**Benefits**:
- Control how data is accessed and modified
- Prevent invalid states
- Change internal implementation without affecting external code

---

### Abstraction

Hiding complex implementation details, exposing only essential features.

```python
class Car:
    def __init__(self, model):
        self.model = model
        self._fuel = 100
    
    # Abstract high-level operation
    def drive(self, distance):
        """User calls this - details hidden"""
        fuel_needed = distance * 0.05  # Simplified calculation
        
        if self._fuel >= fuel_needed:
            self._fuel -= fuel_needed
            print(f"Drove {distance} km")
        else:
            print("Not enough fuel")
    
    # Internal implementation - not exposed
    def _calculate_fuel_consumption(self, distance, speed):
        """Internal method - hidden from user"""
        return distance * 0.05 * (speed / 100)
    
    def refuel(self):
        self._fuel = 100

# Usage
car = Car("Tesla")
car.drive(100)      # User doesn't care about fuel calculations
car.refuel()

# User doesn't call internal methods
# car._calculate_fuel_consumption(100, 60)  # Should avoid
```

**Benefits**:
- Simplified interface for users
- Implementation can change without breaking code
- Focus on "what" not "how"

---

### Inheritance

Creating new classes based on existing classes, promoting code reuse.

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Child classes inherit from Animal
class Dog(Animal):
    def speak(self):  # Override parent method
        print(f"{self.name} barks: Woof!")

class Cat(Animal):
    def speak(self):  # Override parent method
        print(f"{self.name} meows: Meow!")

class Bird(Animal):
    def speak(self):
        print(f"{self.name} chirps: Tweet!")

# Usage
dog = Dog("Rex")
cat = Cat("Whiskers")
bird = Bird("Tweety")

dog.speak()      # Rex barks: Woof!
cat.speak()      # Whiskers meows: Meow!
bird.speak()     # Tweety chirps: Tweet!

# Inheritance chain
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

tesla = ElectricCar("Tesla", "Model 3", 75)
print(f"{tesla.brand} {tesla.model} with {tesla.battery}kWh battery")
```

**Benefits**:
- Code reuse
- Establish relationships between classes
- Hierarchy and organization

---

### Polymorphism

Objects of different classes respond to the same method call in different ways.

```python
# Same interface, different behavior
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Polymorphic function
def print_area(shape):
    """Works with any Shape subclass"""
    print(f"Area: {shape.area():.2f}")

# Same method, different results
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4)
]

for shape in shapes:
    print_area(shape)
    # Area: 78.50
    # Area: 24.00
    # Area: 6.00
```

**Duck Typing** (Python specific):
```python
# Classes don't need to inherit to be polymorphic
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(thing):
    thing.quack()

duck = Duck()
person = Person()

make_it_quack(duck)     # Quack!
make_it_quack(person)   # I'm quacking like a duck!
```

**Benefits**:
- Write generic code
- Easy to extend with new types
- Flexible and maintainable

---

## Real-World OOP Example: E-Commerce System

```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def reduce_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = []
    
    def add_to_cart(self, product, quantity):
        self.cart.append({"product": product, "quantity": quantity})
    
    def get_total(self):
        total = 0
        for item in self.cart:
            total += item["product"].price * item["quantity"]
        return total

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = customer.cart
        self.total = customer.get_total()
        self.status = "Pending"
    
    def process(self):
        # Reduce stock for each item
        for item in self.items:
            item["product"].reduce_stock(item["quantity"])
        self.status = "Processed"
        print(f"Order for {self.customer.name} processed. Total: ${self.total:.2f}")

# Usage
laptop = Product("Laptop", 999.99, 5)
mouse = Product("Mouse", 29.99, 50)

customer = Customer("Alice", "alice@example.com")
customer.add_to_cart(laptop, 1)
customer.add_to_cart(mouse, 2)

order = Order(customer)
order.process()  # Order for Alice processed. Total: $1059.97
```

---

## Mini-Exercises

### Exercise 1: Library System

```python
# Create a Library system with Book, Library, and Member classes
# Book: title, author, isbn, available (bool)
# Library: name, books (list), add_book(), remove_book(), search_book()
# Member: name, books_borrowed (list), borrow_book(), return_book()

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def get_available_books(self):
        return [b for b in self.books if b.available]

class Member:
    def __init__(self, name):
        self.name = name
        self.books_borrowed = []
    
    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.books_borrowed.append(book)
            return True
        return False
    
    def return_book(self, book):
        if book in self.books_borrowed:
            book.available = True
            self.books_borrowed.remove(book)
            return True
        return False

# Test
lib = Library("City Library")
book1 = Book("Python 101", "John Doe", "123")
book2 = Book("Web Dev", "Jane Smith", "456")

lib.add_book(book1)
lib.add_book(book2)

member = Member("Alice")
member.borrow_book(book1)
print(f"Available books: {len(lib.get_available_books())}")  # 1
member.return_book(book1)
print(f"Available books: {len(lib.get_available_books())}")  # 2
```

### Exercise 2: Employee Management

```python
# Create Employee (base), Manager (subclass), Developer (subclass)
# Calculate salary based on performance rating

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def calculate_salary(self, rating):
        return self.base_salary * (1 + rating * 0.1)

class Manager(Employee):
    def calculate_salary(self, rating):
        # Managers get 20% bonus
        base = super().calculate_salary(rating)
        return base * 1.2

class Developer(Employee):
    def calculate_salary(self, rating):
        # Developers get stock options bonus (15%)
        base = super().calculate_salary(rating)
        return base * 1.15

# Test
manager = Manager("Bob", 5000)
dev = Developer("Alice", 4000)

print(f"Manager salary: ${manager.calculate_salary(4):.2f}")
print(f"Developer salary: ${dev.calculate_salary(4):.2f}")
```

---

## Summary

| Concept | Purpose | Example |
|---------|---------|---------|
| **Encapsulation** | Hide internal details, control access | Private attributes with public methods |
| **Abstraction** | Simplify complex operations | High-level `drive()` method hiding fuel logic |
| **Inheritance** | Reuse code, create hierarchy | `Dog` and `Cat` inherit from `Animal` |
| **Polymorphism** | Different behavior for same method | `Shape.area()` works for `Circle`, `Rectangle` |

---

<!-- Navigation Footer -->
**[← Core Concepts](../core-concepts/01-variables-to-classes.md)** | **[Back to Index](../../../README.md)** | **[Modules & Files →](../modules-files/03-modules-files-advanced.md)**

**Section:** 1.7 | **Time:** 1-2 hours
