<!-- Navigation -->
**[← Concurrency](../concurrency/01-threading-asyncio.md)** | **[Back to Index](../../../README.md)** | **[Networking →](../networking/01-network-programming.md)**

---

# Advanced Python: Performance Optimization

## 2.12 Profiling and Benchmarking

### Using timeit Module

```python
import timeit

# Method 1: String concatenation
code1 = """
result = ""
for i in range(100):
    result += str(i)
"""

# Method 2: List join
code2 = """
result = "".join(str(i) for i in range(100))
"""

time1 = timeit.timeit(code1, number=10000)
time2 = timeit.timeit(code2, number=10000)

print(f"String concatenation: {time1:.4f}s")
print(f"List join: {time2:.4f}s")
print(f"Join is {time1/time2:.1f}x faster")
```

### Using cProfile for Function Profiling

```python
import cProfile
import pstats

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def process_data():
    for i in range(10):
        fibonacci(30)

# Profile the function
profiler = cProfile.Profile()
profiler.enable()

process_data()

profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)

# Or use command line:
# python -m cProfile -s cumulative script.py
```

---

## 2.13 Optimization Techniques

### 1. Use Built-in Functions and Libraries

```python
# Slow: Manual sum
def slow_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

# Fast: Built-in function
def fast_sum(numbers):
    return sum(numbers)

import timeit

nums = list(range(1000))
slow_time = timeit.timeit(lambda: slow_sum(nums), number=10000)
fast_time = timeit.timeit(lambda: fast_sum(nums), number=10000)

print(f"Manual sum: {slow_time:.4f}s")
print(f"Built-in sum: {fast_time:.4f}s")
print(f"Speedup: {slow_time/fast_time:.1f}x")
```

### 2. Use List Comprehensions

```python
# Slow: for loop
def slow_squares():
    result = []
    for i in range(1000):
        result.append(i ** 2)
    return result

# Fast: list comprehension
def fast_squares():
    return [i ** 2 for i in range(1000)]

import timeit

slow_time = timeit.timeit(slow_squares, number=10000)
fast_time = timeit.timeit(fast_squares, number=10000)

print(f"Loop: {slow_time:.4f}s")
print(f"Comprehension: {fast_time:.4f}s")
print(f"Speedup: {slow_time/fast_time:.1f}x")
```

### 3. Avoid Repeated Function Calls

```python
# Slow: Repeated lookup
def slow_approach():
    import math
    result = 0
    for i in range(10000):
        result += math.sqrt(i)
    return result

# Fast: Cache function
def fast_approach():
    import math
    sqrt = math.sqrt  # Local reference
    result = 0
    for i in range(10000):
        result += sqrt(i)
    return result

import timeit

slow_time = timeit.timeit(slow_approach, number=100)
fast_time = timeit.timeit(fast_approach, number=100)

print(f"Repeated lookup: {slow_time:.4f}s")
print(f"Cached function: {fast_time:.4f}s")
print(f"Speedup: {slow_time/fast_time:.1f}x")
```

### 4. Use Generators for Large Datasets

```python
import sys

# List: Stores all in memory
def get_numbers_list(n):
    return [i for i in range(n)]

# Generator: Lazy evaluation
def get_numbers_gen(n):
    for i in range(n):
        yield i

# Memory comparison
list_million = get_numbers_list(1000000)
print(f"List (1M items): {sys.getsizeof(list_million)} bytes")

gen_million = get_numbers_gen(1000000)
print(f"Generator: {sys.getsizeof(gen_million)} bytes")
```

### 5. Use Dictionary for O(1) Lookups

```python
# Slow: Linear search O(n)
def slow_search(items, target):
    for item in items:
        if item["id"] == target:
            return item
    return None

# Fast: Dictionary lookup O(1)
def fast_search(items_dict, target):
    return items_dict.get(target)

# Setup
items_list = [{"id": i, "name": f"Item {i}"} for i in range(10000)]
items_dict = {item["id"]: item for item in items_list}

import timeit

slow_time = timeit.timeit(lambda: slow_search(items_list, 9999), number=1000)
fast_time = timeit.timeit(lambda: fast_search(items_dict, 9999), number=1000)

print(f"Linear search: {slow_time:.4f}s")
print(f"Dictionary lookup: {fast_time:.4f}s")
print(f"Speedup: {slow_time/fast_time:.1f}x")
```

---

## 2.14 Caching and Memoization

### Manual Caching

```python
def expensive_operation(n):
    """Simulate expensive calculation"""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

# With caching
cache = {}

def cached_operation(n):
    if n in cache:
        return cache[n]
    
    result = expensive_operation(n)
    cache[n] = result
    return result

# Usage
print(cached_operation(10000))  # Calculates and caches
print(cached_operation(10000))  # Returns from cache (instant)
```

### Using functools.lru_cache

```python
from functools import lru_cache
import time

# Without cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# With cache
@lru_cache(maxsize=128)
def fibonacci_cached(n):
    if n < 2:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

# Benchmark
import timeit

start = time.time()
result1 = fibonacci(35)
time1 = time.time() - start

start = time.time()
result2 = fibonacci_cached(35)
time2 = time.time() - start

print(f"Without cache: {time1:.4f}s")
print(f"With cache: {time2:.4f}s")
print(f"Speedup: {time1/time2:.0f}x")
```

---

## 2.15 Database Query Optimization

### N+1 Query Problem

```python
# Slow: N+1 queries
def slow_approach(user_ids, db):
    users = []
    for user_id in user_ids:
        user = db.query_user(user_id)  # Query 1
        posts = db.query_posts(user_id)  # Query 2 (repeated)
        users.append({**user, "posts": posts})
    return users  # N queries for users + N queries for posts

# Fast: Join query (SQLAlchemy example)
from sqlalchemy.orm import joinedload

def fast_approach(user_ids, session):
    users = session.query(User).filter(
        User.id.in_(user_ids)
    ).options(joinedload(User.posts)).all()
    return users  # 1 query
```

### Batch Operations

```python
# Slow: Individual inserts
def slow_insert(items, db):
    for item in items:
        db.insert_one(item)

# Fast: Batch insert
def fast_insert(items, db):
    db.insert_many(items)

# SQLAlchemy example
from sqlalchemy import insert

# Slow
for user in users:
    session.add(user)
    session.commit()

# Fast
session.bulk_insert_mappings(User, users)
session.commit()
```

---

## 2.16 String Operations Optimization

### String Concatenation

```python
import timeit

# Slow: String concatenation with +=
def slow_concat(n):
    result = ""
    for i in range(n):
        result += str(i) + ","
    return result

# Fast: List join
def fast_concat(n):
    return ",".join(str(i) for i in range(n))

# Fast: StringBuilder pattern
def faster_concat(n):
    parts = []
    for i in range(n):
        parts.append(str(i))
    return ",".join(parts)

n = 10000
slow_time = timeit.timeit(lambda: slow_concat(n), number=100)
fast_time = timeit.timeit(lambda: fast_concat(n), number=100)
faster_time = timeit.timeit(lambda: faster_concat(n), number=100)

print(f"Concatenation with +=: {slow_time:.4f}s")
print(f"Join with generator: {fast_time:.4f}s")
print(f"Join with list: {faster_time:.4f}s")
```

---

## 2.17 Algorithm Optimization

### Binary Search vs Linear Search

```python
import bisect

# Linear search O(n)
def linear_search(sorted_list, target):
    for i, item in enumerate(sorted_list):
        if item == target:
            return i
    return -1

# Binary search O(log n)
def binary_search(sorted_list, target):
    return bisect.bisect_left(sorted_list, target)

import timeit

sorted_data = list(range(100000))
target = 99999

linear_time = timeit.timeit(
    lambda: linear_search(sorted_data, target), 
    number=1000
)
binary_time = timeit.timeit(
    lambda: binary_search(sorted_data, target), 
    number=1000
)

print(f"Linear search: {linear_time:.4f}s")
print(f"Binary search: {binary_time:.4f}s")
print(f"Speedup: {linear_time/binary_time:.0f}x")
```

### Sorting Optimization

```python
import timeit

# Slow: Bubble sort O(n²)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Fast: Python's sort O(n log n)
def python_sort(arr):
    return sorted(arr)

data = list(range(1000, 0, -1))

bubble_time = timeit.timeit(
    lambda: bubble_sort(data.copy()), 
    number=10
)
python_time = timeit.timeit(
    lambda: python_sort(data), 
    number=1000
)

print(f"Bubble sort (10 runs): {bubble_time:.4f}s")
print(f"Python sort (1000 runs): {python_time:.4f}s")
```

---

## 2.18 Real-World Optimization Example

### Before Optimization

```python
def process_large_file(filename):
    """Process file - slow version"""
    data = []
    
    with open(filename, 'r') as f:
        for line in f:
            # Parse each line
            fields = line.strip().split(',')
            
            if len(fields) < 3:
                continue
            
            record = {
                'id': int(fields[0]),
                'name': fields[1],
                'value': float(fields[2])
            }
            
            # Inefficient: Check existence every time
            if record['id'] not in [d['id'] for d in data]:
                data.append(record)
    
    return data
```

### After Optimization

```python
def process_large_file_optimized(filename):
    """Process file - optimized version"""
    data = []
    seen_ids = set()  # Use set for O(1) lookup
    
    with open(filename, 'r') as f:
        for line in f:
            fields = line.strip().split(',')
            
            if len(fields) < 3:
                continue
            
            try:
                id_val = int(fields[0])
                
                # Efficient: Check set membership
                if id_val not in seen_ids:
                    record = {
                        'id': id_val,
                        'name': fields[1],
                        'value': float(fields[2])
                    }
                    data.append(record)
                    seen_ids.add(id_val)
            except (ValueError, IndexError):
                continue  # Skip invalid records
    
    return data
```

---

## Mini-Exercise: Optimize Data Processing

```python
import timeit
from typing import List, Dict

# Sample data generator
def generate_data(n):
    return [
        {"id": i, "value": i*2, "category": "A" if i % 2 == 0 else "B"}
        for i in range(n)
    ]

# Slow: Multiple passes through data
def slow_process(data: List[Dict]) -> Dict:
    result = {}
    for item in data:
        if item["category"] == "A":
            result[item["id"]] = item["value"]
    
    # Process again
    total = sum(result.get(item["id"], 0) for item in data)
    
    # Process again
    count = len([item for item in data if item["category"] == "A"])
    
    return {"items": result, "total": total, "count": count}

# Fast: Single pass
def fast_process(data: List[Dict]) -> Dict:
    result = {}
    total = 0
    count = 0
    
    for item in data:
        if item["category"] == "A":
            result[item["id"]] = item["value"]
            total += item["value"]
            count += 1
    
    return {"items": result, "total": total, "count": count}

# Benchmark
data = generate_data(10000)

slow_time = timeit.timeit(
    lambda: slow_process(data), 
    number=100
)
fast_time = timeit.timeit(
    lambda: fast_process(data), 
    number=100
)

print(f"Slow approach: {slow_time:.4f}s")
print(f"Fast approach: {fast_time:.4f}s")
print(f"Speedup: {slow_time/fast_time:.1f}x")

# Verify results are identical
assert slow_process(data) == fast_process(data)
```

---

## Summary Table

| Technique | Benefit | Use Case |
|-----------|---------|----------|
| **Built-in functions** | Optimized C code | Frequent operations |
| **List comprehensions** | Faster than loops | Creating lists |
| **Generators** | Memory efficient | Large datasets |
| **Caching** | Avoid recalculation | Repeated calls |
| **Binary search** | O(log n) vs O(n) | Sorted data |
| **Set lookup** | O(1) vs O(n) | Membership check |
| **Batch operations** | Reduce overhead | Database/file I/O |
| **Profiling** | Identify bottlenecks | Any optimization |

| Optimization | Time Saved | Complexity |
|--------------|-----------|-----------|
| String join vs concat | 10-100x | Low |
| Caching with LRU | 100-1000x | Low |
| Binary vs linear search | 100-1000x | Medium |
| Batch operations | 10-100x | Medium |
| Algorithm improvement | 100-10000x | High |

---

<!-- Navigation Footer -->
**[← Concurrency](../concurrency/01-threading-asyncio.md)** | **[Back to Index](../../../README.md)** | **[Networking →](../networking/01-network-programming.md)**

**Sections:** 2.12-2.18 | **Time:** 1-2 hours
