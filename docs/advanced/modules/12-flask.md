← [11. Scikit-learn](./11-scikit-learn.md) | [Modules](./README.md) | **12. Flask** | [13. FastAPI →](./13-fastapi.md)

---

# Flask: Web Framework

**Purpose:** Build lightweight web applications and REST APIs.

## Simple: Basic App

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify({"users": ["Alice", "Bob"]})

if __name__ == "__main__":
    app.run(debug=True)
```

## Medium: Routing, Templates & Forms

```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/users/<int:user_id>")
def get_user(user_id):
    return jsonify({"id": user_id, "name": f"User {user_id}"})

@app.route("/create", methods=["POST"])
def create_user():
    data = request.json
    return jsonify({"status": "created", "user": data}), 201

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    app.run()
```

## Complex: Blueprints, Error Handling & Middleware

```python
from flask import Flask, Blueprint, jsonify
from functools import wraps

app = Flask(__name__)

# Blueprint
api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.route("/users", methods=["GET"])
def users():
    return jsonify({"users": []})

app.register_blueprint(api_bp)

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Middleware
def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated

@app.route("/protected")
@require_auth
def protected():
    return jsonify({"data": "secret"})

if __name__ == "__main__":
    app.run()
```

**Install:** `pip install flask` | **Use:** Web applications, REST APIs, microservices

---

← [11. Scikit-learn](./11-scikit-learn.md) | [Modules](./README.md) | **12. Flask** | [13. FastAPI →](./13-fastapi.md)
