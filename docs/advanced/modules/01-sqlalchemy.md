← [Modules](./README.md) | **01. SQLAlchemy** | [02. Pydantic →](./02-pydantic.md)

---

# SQLAlchemy: Database ORM

**Purpose:** Object-relational mapping for database operations.

## Simple: Basic CRUD

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

engine = create_engine("sqlite:///app.db")
Base.metadata.create_all(engine)

# Create
session = Session(engine)
user = User(name="Alice", email="alice@example.com")
session.add(user)
session.commit()

# Read
user = session.query(User).filter(User.name == "Alice").first()
print(user.email)

# Update
user.email = "alice.new@example.com"
session.commit()

# Delete
session.delete(user)
session.commit()
```

## Medium: Relationships & Filtering

```python
from sqlalchemy import ForeignKey, relationship

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

User.posts = relationship("Post")

# Query with relationship
user = session.query(User).filter(User.id == 1).first()
for post in user.posts:
    print(post.title)

# Bulk operations
session.query(User).filter(User.name.like("A%")).update({"name": "Updated"})
session.commit()
```

## Complex: Transactions & Events

```python
from sqlalchemy import event
from sqlalchemy.exc import IntegrityError

def transfer(from_id, to_id, amount):
    try:
        from_user = session.query(User).with_for_update().filter(User.id == from_id).first()
        to_user = session.query(User).with_for_update().filter(User.id == to_id).first()
        
        from_user.balance -= amount
        to_user.balance += amount
        session.commit()
    except IntegrityError:
        session.rollback()

@event.listens_for(Session, "after_insert")
def log_insert(mapper, connection, target):
    print(f"Inserted: {target.id}")
```

**Install:** `pip install sqlalchemy` | **Use:** Web apps, APIs, data pipelines

---

← [Modules](./README.md) | **01. SQLAlchemy** | [02. Pydantic →](./02-pydantic.md)
