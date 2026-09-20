← [05. Requests](./05-requests.md) | [Modules](./README.md) | **06. aiohttp** | [07. NumPy →](./07-numpy.md)

---

# aiohttp: Async HTTP Client

**Purpose:** Asynchronous HTTP requests for concurrent operations.

## Simple: Async GET

```python
import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

data = asyncio.run(fetch("https://api.example.com/users"))
print(data)
```

## Medium: Multiple Requests Concurrently

```python
import aiohttp
import asyncio

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return [await r.json() for r in responses]

urls = [
    "https://api.example.com/users",
    "https://api.example.com/posts",
    "https://api.example.com/comments"
]
data = asyncio.run(fetch_all(urls))
```

## Complex: Connection Pool & Timeouts

```python
import aiohttp
import asyncio

async def fetch_with_pool(urls):
    connector = aiohttp.TCPConnector(limit=10, limit_per_host=5)
    timeout = aiohttp.ClientTimeout(total=30)
    
    async with aiohttp.ClientSession(
        connector=connector,
        timeout=timeout
    ) as session:
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        
        results = []
        for i, response in enumerate(responses):
            if isinstance(response, Exception):
                results.append({"url": urls[i], "error": str(response)})
            else:
                try:
                    data = await response.json()
                    results.append({"url": urls[i], "data": data})
                except:
                    results.append({"url": urls[i], "error": "JSON decode failed"})
        
        return results
```

**Install:** `pip install aiohttp` | **Use:** Concurrent requests, high-performance APIs

---

← [05. Requests](./05-requests.md) | [Modules](./README.md) | **06. aiohttp** | [07. NumPy →](./07-numpy.md)
