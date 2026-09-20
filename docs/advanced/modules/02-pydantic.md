← [01. SQLAlchemy](./01-sqlalchemy.md) | [Modules](./README.md) | **02. Pydantic** | [03. BeautifulSoup4 →](./03-beautifulsoup4.md)

---

# Pydantic: Data Validation

**Purpose:** Data validation and parsing using Python type hints.

## Simple: Basic Validation

```python
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    age: int

user = User(name="Alice", email="alice@example.com", age=30)
print(user.model_dump())  # {"name": "Alice", "email": "alice@example.com", "age": 30}

# Validation error
try:
    User(name="Bob", email="invalid", age=25)
except ValueError as e:
    print(e)
```

## Medium: Custom Validators & Nested Models

```python
from pydantic import field_validator, Field

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class Person(BaseModel):
    name: str = Field(..., min_length=1)
    age: int = Field(..., ge=0, le=150)
    address: Address

    @field_validator('name')
    def name_alphanumeric(cls, v):
        assert v.isalpha(), "Name must be alphabetic"
        return v

person_data = {
    "name": "Alice",
    "age": 30,
    "address": {"street": "123 Main", "city": "NYC", "zip_code": "10001"}
}
person = Person(**person_data)
print(person.model_dump_json())
```

## Complex: Config, Serialization & Dynamic Models

```python
from pydantic import ConfigDict, field_serializer
from typing import Any

class Config(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        frozen=False,
        str_strip_whitespace=True
    )
    api_key: str
    timeout: int = 30
    debug: bool = False

    @field_serializer('api_key')
    def serialize_api_key(self, value: str) -> str:
        return f"***{value[-4:]}"

config = Config(api_key="secret_12345", timeout=60)
print(config.model_dump())  # api_key masked

# Dynamic model creation
fields = {"id": (int, ...), "name": (str, ...), "active": (bool, True)}
DynamicModel = create_model("DynamicModel", **fields)
obj = DynamicModel(id=1, name="Test")
```

**Install:** `pip install pydantic` | **Use:** FastAPI, data validation, config management

---

← [01. SQLAlchemy](./01-sqlalchemy.md) | [Modules](./README.md) | **02. Pydantic** | [03. BeautifulSoup4 →](./03-beautifulsoup4.md)
