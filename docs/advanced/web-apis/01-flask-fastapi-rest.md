<!-- Navigation -->
**[← Fundamentals](../../fundamentals/modules-files/03-modules-files-advanced.md)** | **[Back to Index](../../../README.md)** | **[Concurrency →](../concurrency/01-threading-asyncio.md)**

---

# Advanced Python: Web APIs with Flask, FastAPI & REST Design

## 2.1 Flask Basics

Flask is a lightweight web framework for building web applications and APIs.

### Setup and Hello World

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

Run with: `python app.py` then visit `http://localhost:5000`

### Routes and Methods

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# GET request
@app.route("/api/users", methods=["GET"])
def get_users():
    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"}
    ]
    return jsonify(users)

# POST request
@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Missing name"}), 400
    
    new_user = {
        "id": 3,
        "name": data["name"],
        "email": data.get("email", "")
    }
    return jsonify(new_user), 201

# GET with ID
@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    users = {1: {"id": 1, "name": "Alice"}, 2: {"id": 2, "name": "Bob"}}
    user = users.get(user_id)
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# PUT request
@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    return jsonify({"id": user_id, **data}), 200

# DELETE request
@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return jsonify({"message": f"User {user_id} deleted"}), 204
```

### Error Handling

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

@app.route("/api/divide/<int:a>/<int:b>")
def divide(a, b):
    try:
        result = a / b
        return jsonify({"result": result})
    except ZeroDivisionError:
        return jsonify({"error": "Cannot divide by zero"}), 400
```

---

## 2.2 FastAPI Basics

FastAPI is a modern, fast framework with automatic API documentation and type hints.

### Setup and Hello World

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(title="My API", version="1.0.0")

@app.get("/")
def hello():
    return {"message": "Hello, World!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Run with: `uvicorn app:app --reload` then visit `http://localhost:8000/docs`

### Request and Response Models

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Define data model
class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None

class UserCreate(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

# In-memory database
users_db = [
    User(id=1, name="Alice", email="alice@example.com", age=25),
    User(id=2, name="Bob", email="bob@example.com", age=30)
]

@app.get("/users", response_model=List[User])
def get_users():
    return users_db

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    return {"error": "User not found"}, 404

@app.post("/users", response_model=User)
def create_user(user_data: UserCreate):
    new_id = max([u.id for u in users_db]) + 1
    new_user = User(
        id=new_id,
        name=user_data.name,
        email=user_data.email,
        age=user_data.age
    )
    users_db.append(new_user)
    return new_user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_data: UserCreate):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            updated_user = User(
                id=user_id,
                name=user_data.name,
                email=user_data.email,
                age=user_data.age
            )
            users_db[i] = updated_user
            return updated_user
    return {"error": "User not found"}, 404

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(i)
            return {"message": f"User {user_id} deleted"}
    return {"error": "User not found"}, 404
```

### Query Parameters and Validation

```python
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/search")
def search(
    query: str = Query(..., min_length=1, max_length=100),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    return {
        "query": query,
        "skip": skip,
        "limit": limit
    }

# Usage: /search?query=python&skip=0&limit=20
```

---

## 2.3 REST API Design Principles

### Endpoint Naming Conventions

```
# Resources use plural nouns
GET    /api/users              # Get all users
POST   /api/users              # Create user
GET    /api/users/1            # Get user by ID
PUT    /api/users/1            # Update user
DELETE /api/users/1            # Delete user

# Sub-resources
GET    /api/users/1/posts      # Get user's posts
POST   /api/users/1/posts      # Create post for user
GET    /api/users/1/posts/5    # Get specific post

# Query parameters for filtering
GET    /api/users?role=admin&active=true
GET    /api/posts?skip=0&limit=20&sort=date
```

### Status Codes

```
200 OK                 - Request successful
201 Created            - Resource created
204 No Content         - Successful, no response body
400 Bad Request        - Invalid input
401 Unauthorized       - Authentication required
403 Forbidden          - Access denied
404 Not Found          - Resource not found
409 Conflict           - Resource conflict
500 Internal Error     - Server error
```

### Complete REST API Example

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Blog API")

# Models
class Post(BaseModel):
    id: int
    title: str
    content: str
    author: str
    created_at: datetime
    updated_at: Optional[datetime] = None

class PostCreate(BaseModel):
    title: str
    content: str
    author: str

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

# Database
posts_db = [
    Post(
        id=1,
        title="Python Basics",
        content="Introduction to Python",
        author="Alice",
        created_at=datetime.now()
    ),
    Post(
        id=2,
        title="Web APIs",
        content="Building REST APIs",
        author="Bob",
        created_at=datetime.now()
    )
]

# CRUD Operations
@app.get("/api/posts", response_model=List[Post])
def list_posts(skip: int = 0, limit: int = 10):
    """Get all posts with pagination"""
    return posts_db[skip:skip+limit]

@app.get("/api/posts/{post_id}", response_model=Post)
def get_post(post_id: int):
    """Get post by ID"""
    for post in posts_db:
        if post.id == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.post("/api/posts", response_model=Post, status_code=status.HTTP_201_CREATED)
def create_post(post_data: PostCreate):
    """Create new post"""
    new_id = max([p.id for p in posts_db]) + 1 if posts_db else 1
    new_post = Post(
        id=new_id,
        title=post_data.title,
        content=post_data.content,
        author=post_data.author,
        created_at=datetime.now()
    )
    posts_db.append(new_post)
    return new_post

@app.put("/api/posts/{post_id}", response_model=Post)
def update_post(post_id: int, post_data: PostUpdate):
    """Update post"""
    for i, post in enumerate(posts_db):
        if post.id == post_id:
            updated = post.copy(update={
                "title": post_data.title or post.title,
                "content": post_data.content or post.content,
                "updated_at": datetime.now()
            })
            posts_db[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/api/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int):
    """Delete post"""
    for i, post in enumerate(posts_db):
        if post.id == post_id:
            posts_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Post not found")

# Additional endpoints
@app.get("/api/posts/author/{author}", response_model=List[Post])
def get_posts_by_author(author: str):
    """Get all posts by author"""
    return [p for p in posts_db if p.author.lower() == author.lower()]
```

---

## 2.4 Request/Response Handling

### Headers and Cookies

```python
from fastapi import FastAPI, Header, Cookie
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/headers")
def read_headers(user_agent: str = Header(None)):
    return {"user-agent": user_agent}

@app.post("/login")
def login(username: str, password: str):
    response = JSONResponse(content={"message": "Login successful"})
    response.set_cookie(key="user", value=username)
    return response

@app.get("/profile")
def get_profile(user: str = Cookie(None)):
    if not user:
        return {"error": "Not logged in"}
    return {"user": user}
```

### File Upload

```python
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents)
    }

@app.post("/upload-multiple")
async def upload_files(files: List[UploadFile] = File(...)):
    return {
        "files": [f.filename for f in files],
        "count": len(files)
    }
```

---

## 2.5 Authentication & Middleware

### Basic Authentication

```python
from fastapi import FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

@app.get("/protected")
def protected_route(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "password123"
    
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    return {"message": f"Hello {credentials.username}"}
```

### Custom Middleware

```python
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
import time

app = FastAPI()

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response

app.add_middleware(LoggingMiddleware)
```

---

## 2.6 Comparison: Flask vs FastAPI

| Feature | Flask | FastAPI |
|---------|-------|---------|
| **Type Hints** | Optional | Built-in, validated |
| **Auto Docs** | No | Yes (Swagger, ReDoc) |
| **Performance** | Good | Excellent (async) |
| **Async Support** | Limited | Full support |
| **Validation** | Manual | Automatic (Pydantic) |
| **Learning Curve** | Gentle | Moderate |
| **Use Case** | Small-medium apps | Modern APIs, microservices |

---

## Mini-Exercise: Todo API

### Using FastAPI

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Todo API")

class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False
    created_at: datetime

class TodoCreate(BaseModel):
    title: str
    description: str

# In-memory database
todos_db = [
    Todo(id=1, title="Learn FastAPI", description="Study FastAPI basics", completed=False, created_at=datetime.now()),
    Todo(id=2, title="Build API", description="Create REST API", completed=False, created_at=datetime.now())
]

@app.get("/todos", response_model=List[Todo])
def get_todos(completed: Optional[bool] = None):
    """Get all todos, optionally filtered by completion status"""
    if completed is None:
        return todos_db
    return [t for t in todos_db if t.completed == completed]

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    """Get specific todo"""
    for todo in todos_db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo_data: TodoCreate):
    """Create new todo"""
    new_id = max([t.id for t in todos_db]) + 1 if todos_db else 1
    new_todo = Todo(
        id=new_id,
        title=todo_data.title,
        description=todo_data.description,
        created_at=datetime.now()
    )
    todos_db.append(new_todo)
    return new_todo

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, completed: bool):
    """Mark todo as completed/incomplete"""
    for i, todo in enumerate(todos_db):
        if todo.id == todo_id:
            todo.completed = completed
            todos_db[i] = todo
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):
    """Delete todo"""
    for i, todo in enumerate(todos_db):
        if todo.id == todo_id:
            todos_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Todo not found")

@app.get("/stats")
def get_stats():
    """Get statistics"""
    total = len(todos_db)
    completed = sum(1 for t in todos_db if t.completed)
    return {
        "total_todos": total,
        "completed": completed,
        "pending": total - completed
    }
```

---

## Summary Table

| Aspect | Flask | FastAPI |
|--------|-------|---------|
| **Setup** | `from flask import Flask` | `from fastapi import FastAPI` |
| **Route Decorator** | `@app.route()` | `@app.get()`, `@app.post()` |
| **Request Data** | `request.get_json()` | Parameter/model-based |
| **Validation** | Manual | Automatic (Pydantic) |
| **Documentation** | Manual | Auto-generated |
| **Best For** | Traditional web apps | Modern APIs |

---

<!-- Navigation Footer -->
**[← Fundamentals](../../fundamentals/modules-files/03-modules-files-advanced.md)** | **[Back to Index](../../../README.md)** | **[Concurrency →](../concurrency/01-threading-asyncio.md)**

**Sections:** 2.1-2.6 | **Time:** 1-2 hours
