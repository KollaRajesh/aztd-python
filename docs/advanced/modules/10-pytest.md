← [09. Matplotlib](./09-matplotlib.md) | [Modules](./README.md) | **10. Pytest** | [11. Scikit-learn →](./11-scikit-learn.md)

---

# Pytest: Testing Framework

**Purpose:** Write and run unit tests with fixtures and parametrization.

## Simple: Basic Tests

```python
import pytest

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0

def test_add_floats():
    assert add(1.5, 2.5) == 4.0
```

## Medium: Fixtures & Parametrization

```python
import pytest

@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 30}

@pytest.fixture
def db():
    db = {}
    yield db
    db.clear()

def test_with_fixture(sample_data):
    assert sample_data["name"] == "Alice"

@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16)
])
def test_square(input, expected):
    assert input ** 2 == expected

def test_db_operations(db):
    db["key"] = "value"
    assert db["key"] == "value"
```

## Complex: Mocking & Exception Testing

```python
import pytest
from unittest.mock import Mock, patch

class UserService:
    def __init__(self, api):
        self.api = api
    
    def get_user(self, user_id):
        return self.api.fetch_user(user_id)

@pytest.fixture
def mock_api():
    return Mock()

def test_get_user_success(mock_api):
    mock_api.fetch_user.return_value = {"id": 1, "name": "Alice"}
    service = UserService(mock_api)
    
    result = service.get_user(1)
    assert result["name"] == "Alice"
    mock_api.fetch_user.assert_called_once_with(1)

def test_exception_handling():
    with pytest.raises(ValueError):
        int("invalid")

@patch("requests.get")
def test_with_patch(mock_get):
    mock_get.return_value.json.return_value = {"status": "ok"}
    # Test code here
```

**Install:** `pip install pytest` | **Use:** Unit testing, integration testing, test automation

---

← [09. Matplotlib](./09-matplotlib.md) | [Modules](./README.md) | **10. Pytest** | [11. Scikit-learn →](./11-scikit-learn.md)
