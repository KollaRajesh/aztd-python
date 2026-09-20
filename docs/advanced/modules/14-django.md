← [13. FastAPI](./13-fastapi.md) | [Modules](./README.md) | **14. Django** | [15. LangChain →](./15-langchain.md)

---

# Django: Full-Stack Framework

**Purpose:** Build complete web applications with built-in ORM, admin, and authentication.

## Simple: Models & Views

```python
from django.db import models
from django.http import JsonResponse
from django.views import View

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserListView(View):
    def get(self, request):
        users = User.objects.all().values("id", "name", "email")
        return JsonResponse(list(users), safe=False)

    def post(self, request):
        user = User.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email")
        )
        return JsonResponse({"id": user.id, "name": user.name})
```

## Medium: QuerySets & Relationships

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)

# Queries
posts = Post.objects.filter(published=True).order_by("-id")
author_posts = Post.objects.filter(author__name="Alice")
post_count = Post.objects.filter(author__name="Bob").count()

# Aggregation
from django.db.models import Count
authors = Author.objects.annotate(post_count=Count("post"))

# Update
Post.objects.filter(published=False).update(published=True)
```

## Complex: Signals, Managers & Serializers

```python
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.serializers import serialize
import json

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

class PostManager(models.Manager):
    def published(self):
        return self.filter(status="published")
    
    def by_author(self, author_id):
        return self.filter(author_id=author_id)

Post.objects = PostManager()

@receiver(post_save, sender=Post)
def post_saved(sender, instance, created, **kwargs):
    if created:
        print(f"Post '{instance.title}' created by {instance.author}")

# Serialization
def serialize_post(post):
    return {
        "id": post.id,
        "title": post.title,
        "author": post.author.username,
        "content": post.content
    }

posts = Post.objects.all()
serialized = [serialize_post(p) for p in posts]
json_data = json.dumps(serialized)
```

**Install:** `pip install django` | **Use:** Full-stack web applications, enterprise projects

---

← [13. FastAPI](./13-fastapi.md) | [Modules](./README.md) | **14. Django** | [15. LangChain →](./15-langchain.md)
