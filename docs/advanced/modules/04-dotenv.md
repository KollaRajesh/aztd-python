← [03. BeautifulSoup4](./03-beautifulsoup4.md) | [Modules](./README.md) | **04. python-dotenv** | [05. Requests →](./05-requests.md)

---

# Python-dotenv: Environment Variables

**Purpose:** Load environment variables from .env files.

## Simple: Load .env

```python
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

print(f"API Key: {API_KEY}")
print(f"Debug: {DEBUG}")
```

## Medium: Type Conversion & Defaults

```python
from dotenv import load_dotenv
import os

load_dotenv("config/.env")

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")
PORT = int(os.getenv("PORT", "8000"))
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost").split(",")

print(f"DB: {DATABASE_URL}, Port: {PORT}, Hosts: {ALLOWED_HOSTS}")
```

## Complex: Config Class with dotenv

```python
from dotenv import load_dotenv
import os
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    api_key: str
    database_url: str
    debug: bool = False
    port: int = 8000
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
print(settings.model_dump())
```

**Install:** `pip install python-dotenv` | **Use:** Configuration management, secrets handling

---

← [03. BeautifulSoup4](./03-beautifulsoup4.md) | [Modules](./README.md) | **04. python-dotenv** | [05. Requests →](./05-requests.md)
