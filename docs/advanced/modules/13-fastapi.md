← [12. Flask](./12-flask.md) | [Modules](./README.md) | **13. FastAPI** | [14. Django →](./14-django.md)

---

# FastAPI: Modern Web Framework

**Purpose:** Build fast, modern REST APIs with automatic documentation.

## Simple: Basic API

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "name": f"User {user_id}"}

@app.post("/users")
def create_user(user: User):
    return {"status": "created", "user": user}
```

## Medium: Query Parameters & Validation

```python
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/items")
def list_items(skip: int = Query(0, ge=0), limit: int = Query(10, le=100)):
    return {"skip": skip, "limit": limit}

@app.get("/search")
def search(q: str = Query(..., min_length=1, max_length=50)):
    return {"query": q}

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    if post_id < 1:
        raise HTTPException(status_code=400, detail="Invalid ID")
    return {"id": post_id, "title": f"Post {post_id}"}
```

## Complex: Dependencies, Middleware & Exception Handling

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_token_header(x_token: str = Header(...)):
    if x_token != "secret-token":
        raise HTTPException(status_code=403, detail="Invalid token")
    return x_token

@app.get("/protected")
def protected_route(token: str = Depends(get_token_header)):
    return {"message": "Access granted"}

# Exception handler
@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return {"error": str(exc)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**Install:** `pip install fastapi uvicorn` | **Use:** High-performance REST APIs, async applications

---

← [12. Flask](./12-flask.md) | [Modules](./README.md) | **13. FastAPI** | [14. Django →](./14-django.md)
