"""
Sample: Testing with unittest and pytest
Run with: python -m pytest samples/09_testing.py -v
or: python -m unittest samples.09_testing
"""

import unittest

# Functions to test
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Unit tests with unittest
class TestMath(unittest.TestCase):
    
    def test_add_positive(self):
        result = add(2, 3)
        self.assertEqual(result, 5)
    
    def test_add_negative(self):
        result = add(-1, -2)
        self.assertEqual(result, -3)
    
    def test_multiply_positive(self):
        result = multiply(3, 4)
        self.assertEqual(result, 12)
    
    def test_multiply_by_zero(self):
        result = multiply(5, 0)
        self.assertEqual(result, 0)
    
    def test_divide_positive(self):
        result = divide(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

# Test class with setUp
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class TestUser(unittest.TestCase):
    
    def setUp(self):
        """Called before each test"""
        self.user = User("Alice", 30)
    
    def test_user_name(self):
        self.assertEqual(self.user.name, "Alice")
    
    def test_user_age(self):
        self.assertEqual(self.user.age, 30)
    
    def test_user_not_child(self):
        self.assertTrue(self.user.age >= 18)

# Pytest-style tests (can also run with unittest)
def test_add_with_pytest():
    assert add(2, 3) == 5

def test_multiply_with_pytest():
    assert multiply(3, 4) == 12

# Run tests
if __name__ == "__main__":
    unittest.main(verbosity=2)
