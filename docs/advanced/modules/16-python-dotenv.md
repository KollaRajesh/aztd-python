← [15. LangChain](./15-langchain.md) | [Modules](./README.md) | **16. python-dotenv**

---

# python-dotenv: Environment Variables

**Purpose:** Load environment variables from .env files for configuration management.

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
MAX_CONNECTIONS = int(os.getenv("MAX_CONNECTIONS", "10"))

print(f"DB: {DATABASE_URL}")
print(f"Port: {PORT}")
print(f"Hosts: {ALLOWED_HOSTS}")
```

## Complex: Config Class with Pydantic

```python
from dotenv import load_dotenv
import os
from pydantic import BaseSettings, Field

load_dotenv()

class Settings(BaseSettings):
    api_key: str = Field(..., alias="API_KEY")
    database_url: str = Field(default="sqlite:///app.db", alias="DATABASE_URL")
    debug: bool = False
    port: int = 8000
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

settings = Settings()
print(settings.model_dump())

# Usage in app
from fastapi import FastAPI
app = FastAPI(debug=settings.debug)
```

**Install:** `pip install python-dotenv` | **Use:** Configuration, secrets management, environment setup

---

← [15. LangChain](./15-langchain.md) | [Modules](./README.md) | **16. python-dotenv**
