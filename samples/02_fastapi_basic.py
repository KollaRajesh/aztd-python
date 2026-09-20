"""
Sample: FastAPI basics
Run with: pip install fastapi uvicorn
         uvicorn samples.02_fastapi_basic:app --reload
Visit: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Request/Response models
class User(BaseModel):
    name: str
    email: str
    age: int

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int

# In-memory storage
users_db = []

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"greeting": f"Hello, {name}"}

# CRUD operations
@app.get("/users/", response_model=List[UserResponse])
def list_users():
    return users_db

@app.post("/users/", status_code=201, response_model=UserResponse)
def create_user(user: User):
    new_user = {
        "id": len(users_db) + 1,
        **user.dict()
    }
    users_db.append(new_user)
    return new_user

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: User):
    for existing_user in users_db:
        if existing_user["id"] == user_id:
            existing_user.update(user.dict())
            return existing_user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users_db):
        if user["id"] == user_id:
            users_db.pop(i)
            return {"status": "deleted"}
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/search/")
def search(q: str, skip: int = 0, limit: int = 10):
    return {"query": q, "skip": skip, "limit": limit, "results": []}

# Run with: uvicorn samples.02_fastapi_basic:app --reload
# Then visit: http://localhost:8000/docs
