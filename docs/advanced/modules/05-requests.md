← [04. python-dotenv](./04-dotenv.md) | [Modules](./README.md) | **05. Requests** | [06. aiohttp →](./06-aiohttp.md)

---

# Requests: HTTP Client

**Purpose:** Make HTTP requests to APIs and web services.

## Simple: GET & POST

```python
import requests

# GET
response = requests.get("https://api.example.com/users")
data = response.json()
print(data)

# POST
payload = {"name": "Alice", "email": "alice@example.com"}
response = requests.post("https://api.example.com/users", json=payload)
print(response.status_code)  # 201
```

## Medium: Headers, Params & Error Handling

```python
import requests

headers = {"Authorization": "Bearer token123", "User-Agent": "MyApp/1.0"}
params = {"page": 1, "limit": 10}

try:
    response = requests.get(
        "https://api.example.com/users",
        headers=headers,
        params=params,
        timeout=5
    )
    response.raise_for_status()
    users = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

## Complex: Sessions & Retries

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def create_session():
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

session = create_session()
response = session.get("https://api.example.com/data")
session.close()
```

**Install:** `pip install requests` | **Use:** API calls, web scraping, integrations

---

← [04. python-dotenv](./04-dotenv.md) | [Modules](./README.md) | **05. Requests** | [06. aiohttp →](./06-aiohttp.md)
