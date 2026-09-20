"""
Sample: Flask basics
Run with: pip install flask
         python samples/01_flask_basic.py
Visit: http://localhost:5000/
"""

from flask import Flask, request, render_template_string

app = Flask(__name__)

# In-memory storage
users_db = []

@app.route("/")
def home():
    return "Welcome to Flask!"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.get("/users/")
def list_users():
    return {"users": users_db}

@app.post("/users/")
def create_user():
    data = request.json
    user = {
        "id": len(users_db) + 1,
        "name": data.get("name"),
        "email": data.get("email")
    }
    users_db.append(user)
    return user, 201

@app.get("/users/<int:user_id>")
def get_user(user_id):
    for user in users_db:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}, 404

@app.get("/search")
def search():
    query = request.args.get("q", "")
    return {"query": query, "results": []}

# Template example
@app.route("/template/<name>")
def template_example(name):
    html = "<h1>Hello, {{ name }}!</h1>"
    return render_template_string(html, name=name)

if __name__ == "__main__":
    print("Starting Flask app on http://localhost:5000/")
    print("Try: http://localhost:5000/greet/Alice")
    print("Try: http://localhost:5000/users/")
    app.run(debug=True, port=5000)
