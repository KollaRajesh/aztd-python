"""
Sample: Design patterns
Demonstrates decorator, factory, singleton, and observer patterns.
"""

import time

# Decorator pattern
print("=== Decorator Pattern ===")

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"  {func.__name__} took {elapsed:.3f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "Done"

result = slow_function()
print(f"  Result: {result}")

# Factory pattern
print("\n=== Factory Pattern ===")

class DatabaseConnection:
    def __init__(self, db_type):
        self.connection = self._create_connection(db_type)
    
    def _create_connection(self, db_type):
        if db_type == "postgres":
            return "PostgreSQL connection"
        elif db_type == "sqlite":
            return "SQLite connection"
        elif db_type == "mysql":
            return "MySQL connection"
        else:
            raise ValueError(f"Unknown database type: {db_type}")

for db_type in ["postgres", "sqlite"]:
    db = DatabaseConnection(db_type)
    print(f"  {db_type}: {db.connection}")

# Singleton pattern
print("\n=== Singleton Pattern ===")

class Logger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance
    
    def log(self, message):
        self.logs.append(message)
        print(f"  Logged: {message}")

logger1 = Logger()
logger2 = Logger()

logger1.log("First message")
logger2.log("Second message")

print(f"  logger1 is logger2: {logger1 is logger2}")
print(f"  Total logs: {len(logger1.logs)}")

# Observer pattern
print("\n=== Observer Pattern ===")

class Subject:
    def __init__(self):
        self.observers = []
    
    def attach(self, observer):
        self.observers.append(observer)
    
    def detach(self, observer):
        self.observers.remove(observer)
    
    def notify(self, event):
        for observer in self.observers:
            observer.update(event)

class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, event):
        print(f"  {self.name} received: {event}")

subject = Subject()
observer1 = Observer("Observer1")
observer2 = Observer("Observer2")

subject.attach(observer1)
subject.attach(observer2)

subject.notify("New event occurred")
