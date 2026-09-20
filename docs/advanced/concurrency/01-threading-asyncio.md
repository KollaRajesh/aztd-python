<!-- Navigation -->
**[← Web APIs](../web-apis/01-flask-fastapi-rest.md)** | **[Back to Index](../../../README.md)** | **[Performance →](../performance/01-performance-optimization.md)**

---

# Advanced Python: Concurrency with Threading and Asyncio

## 2.7 Threading Basics

Threading allows multiple tasks to run concurrently in the same process. Each thread shares memory but runs independently.

### Creating Threads

```python
import threading
import time

def task(name, duration):
    print(f"{name} started")
    time.sleep(duration)
    print(f"{name} finished")

# Create threads
thread1 = threading.Thread(target=task, args=("Task 1", 2))
thread2 = threading.Thread(target=task, args=("Task 2", 3))

# Start threads
thread1.start()
thread2.start()

# Wait for completion
thread1.join()
thread2.join()

print("All tasks completed")
```

### Thread Synchronization with Lock

```python
import threading

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    
    def increment(self):
        # Without lock - race condition (inconsistent results)
        # self.value += 1
        
        # With lock - thread-safe
        with self.lock:
            self.value += 1

counter = Counter()

def worker(counter, iterations):
    for _ in range(iterations):
        counter.increment()

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(counter, 1000))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final count: {counter.value}")  # 5000 (guaranteed with lock)
```

### Producer-Consumer with Queue

```python
import threading
import queue
import time
import random

def producer(q):
    for i in range(5):
        item = f"item-{i}"
        q.put(item)
        print(f"Produced: {item}")
        time.sleep(random.uniform(0.1, 0.5))

def consumer(q):
    while True:
        try:
            item = q.get(timeout=2)
            if item is None:
                break
            print(f"Consumed: {item}")
            time.sleep(random.uniform(0.2, 0.8))
            q.task_done()
        except queue.Empty:
            break

q = queue.Queue(maxsize=2)

prod_thread = threading.Thread(target=producer, args=(q,))
cons_thread = threading.Thread(target=consumer, args=(q,))

prod_thread.start()
cons_thread.start()

prod_thread.join()
q.put(None)  # Signal consumer to stop
cons_thread.join()

print("All done")
```

### Thread Pooling

```python
from concurrent.futures import ThreadPoolExecutor
import time

def download_file(url):
    print(f"Downloading {url}")
    time.sleep(2)  # Simulate download
    return f"Downloaded {url}"

urls = [
    "http://example.com/file1.txt",
    "http://example.com/file2.txt",
    "http://example.com/file3.txt"
]

# Use ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit all tasks
    futures = [executor.submit(download_file, url) for url in urls]
    
    # Get results as they complete
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        print(result)
```

---

## 2.8 Asyncio and Async/Await

Asyncio enables asynchronous programming with a single thread. Better for I/O-bound tasks.

### Basic Async Functions

```python
import asyncio

async def say_hello(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

# Run async function
asyncio.run(say_hello("Alice", 1))
```

### Concurrent Tasks

```python
import asyncio

async def fetch_data(url, delay):
    print(f"Fetching {url}")
    await asyncio.sleep(delay)
    return f"Data from {url}"

async def main():
    # Create multiple tasks
    tasks = [
        fetch_data("http://api1.com", 1),
        fetch_data("http://api2.com", 2),
        fetch_data("http://api3.com", 1.5)
    ]
    
    # Run concurrently
    results = await asyncio.gather(*tasks)
    
    for result in results:
        print(result)

asyncio.run(main())
```

### Async with Timeout

```python
import asyncio

async def slow_operation():
    await asyncio.sleep(5)
    return "Done"

async def main():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("Operation timed out!")

asyncio.run(main())
```

### Async with HTTP Requests

```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# Usage
urls = [
    "https://api.example.com/user/1",
    "https://api.example.com/user/2",
    "https://api.example.com/user/3"
]

results = asyncio.run(fetch_multiple_urls(urls))
for result in results:
    print(result[:50] + "...")  # Print first 50 chars
```

### Async Context Manager

```python
import asyncio

class AsyncResource:
    async def __aenter__(self):
        print("Acquiring resource")
        await asyncio.sleep(1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        await asyncio.sleep(1)
    
    async def do_something(self):
        print("Using resource")
        await asyncio.sleep(1)

async def main():
    async with AsyncResource() as resource:
        await resource.do_something()

asyncio.run(main())
```

### Producer-Consumer with AsyncIO

```python
import asyncio

async def producer(queue):
    for i in range(5):
        item = f"item-{i}"
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(0.5)

async def consumer(queue):
    while True:
        try:
            item = await asyncio.wait_for(queue.get(), timeout=2)
            if item is None:
                break
            print(f"Consumed: {item}")
            await asyncio.sleep(1)
        except asyncio.TimeoutError:
            break

async def main():
    q = asyncio.Queue()
    
    # Run producer and consumer concurrently
    await asyncio.gather(
        producer(q),
        consumer(q)
    )

asyncio.run(main())
```

---

## 2.9 Threading vs Asyncio

### When to Use Threading

- CPU-intensive tasks (threading allows OS to schedule threads)
- Blocking I/O operations that don't support async
- Simpler logic for multiple independent tasks

```python
import threading
import time

def cpu_intensive_task(n):
    """Threading works well for CPU tasks"""
    total = 0
    for i in range(n):
        total += i
    return total

def threaded_approach():
    threads = []
    for i in range(4):
        t = threading.Thread(target=cpu_intensive_task, args=(10**7,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

start = time.time()
threaded_approach()
print(f"Threading: {time.time() - start:.2f}s")
```

### When to Use Asyncio

- I/O-bound tasks (network, file operations)
- Many concurrent operations (handles thousands)
- Need responsive applications

```python
import asyncio
import aiohttp
import time

async def fetch_url(session, url):
    async with session.get(url) as response:
        return response.status

async def asyncio_approach(urls):
    """Asyncio excels with many I/O operations"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# Usage
urls = ["https://example.com"] * 100

start = time.time()
# results = asyncio.run(asyncio_approach(urls))
# print(f"Asyncio: {time.time() - start:.2f}s")
```

---

## 2.10 Performance Optimization

### Comparison Example

```python
import time
import threading
import asyncio

# Simulate I/O operations
def blocking_io(n):
    time.sleep(1)
    return f"Task {n}"

async def async_io(n):
    await asyncio.sleep(1)
    return f"Task {n}"

# Sequential (baseline)
start = time.time()
for i in range(5):
    blocking_io(i)
print(f"Sequential: {time.time() - start:.2f}s")  # ~5s

# Threading
start = time.time()
threads = []
for i in range(5):
    t = threading.Thread(target=blocking_io, args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(f"Threading: {time.time() - start:.2f}s")  # ~1s

# Asyncio
async def async_main():
    tasks = [async_io(i) for i in range(5)]
    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(async_main())
print(f"Asyncio: {time.time() - start:.2f}s")  # ~1s
```

---

## 2.11 Real-World Example: Concurrent Web Scraper

```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch_page(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            return await response.text()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

async def parse_page(html):
    # Simulate parsing (would use BeautifulSoup in reality)
    await asyncio.sleep(0.1)
    return {"title": "Article", "links": 5}

async def scrape_website(urls, max_concurrent=5):
    """Scrape multiple URLs concurrently"""
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def limited_fetch(session, url):
        async with semaphore:
            print(f"Fetching {url}")
            html = await fetch_page(session, url)
            if html:
                data = await parse_page(html)
                return data
            return None
    
    async with aiohttp.ClientSession() as session:
        tasks = [limited_fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Usage
urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3",
    # ... more URLs
]

# results = asyncio.run(scrape_website(urls, max_concurrent=5))
# for result in results:
#     print(result)
```

---

## Mini-Exercise: Download Manager

### Using ThreadPoolExecutor

```python
from concurrent.futures import ThreadPoolExecutor
import time
import random

def download_file(filename, size_mb):
    """Simulate file download"""
    print(f"Downloading {filename} ({size_mb}MB)")
    # Simulate download time: ~1s per MB
    time.sleep(size_mb)
    print(f"Completed {filename}")
    return f"{filename}: {size_mb}MB"

def download_manager(files):
    """Manage concurrent downloads"""
    results = []
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {
            executor.submit(download_file, name, size): name 
            for name, size in files
        }
        
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)
            print(f"Progress: {len(results)}/{len(files)}")
    
    return results

# Test
files = [
    ("document.pdf", 2),
    ("image.zip", 3),
    ("video.mp4", 5),
    ("archive.tar.gz", 4)
]

results = download_manager(files)
print("\nAll downloads completed:")
for r in results:
    print(r)
```

### Using Asyncio

```python
import asyncio

async def download_file_async(filename, size_mb):
    """Async file download"""
    print(f"Downloading {filename} ({size_mb}MB)")
    await asyncio.sleep(size_mb)  # Simulate download
    print(f"Completed {filename}")
    return f"{filename}: {size_mb}MB"

async def download_manager_async(files, max_concurrent=3):
    """Manage concurrent downloads with asyncio"""
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def limited_download(name, size):
        async with semaphore:
            return await download_file_async(name, size)
    
    tasks = [limited_download(name, size) for name, size in files]
    results = await asyncio.gather(*tasks)
    return results

# Test
files = [
    ("document.pdf", 2),
    ("image.zip", 3),
    ("video.mp4", 5),
    ("archive.tar.gz", 4)
]

results = asyncio.run(download_manager_async(files))
print("\nAll downloads completed:")
for r in results:
    print(r)
```

---

## Summary Table

| Feature | Threading | Asyncio |
|---------|-----------|---------|
| **Best For** | CPU tasks, blocking I/O | I/O operations, responsiveness |
| **Concurrency** | True parallelism (OS) | Cooperative (single thread) |
| **Overhead** | High (thread creation) | Low (lightweight) |
| **Scalability** | Limited (OS threads) | Excellent (many tasks) |
| **Complexity** | Moderate (locks needed) | Lower (no race conditions) |
| **Debugging** | Harder (race conditions) | Easier (deterministic) |
| **Max Tasks** | Hundreds | Thousands+ |

| Operation | Threading | Asyncio |
|-----------|-----------|---------|
| **Create** | `Thread()` | `asyncio.create_task()` |
| **Wait for completion** | `.join()` | `await asyncio.gather()` |
| **Synchronization** | `Lock()`, `Queue` | `asyncio.Lock()`, `asyncio.Queue` |
| **Timeout** | `timeout` parameter | `asyncio.wait_for()` |

---

<!-- Navigation Footer -->
**[← Web APIs](../web-apis/01-flask-fastapi-rest.md)** | **[Back to Index](../../../README.md)** | **[Performance →](../performance/01-performance-optimization.md)**

**Sections:** 2.7-2.11 | **Time:** 1-2 hours
