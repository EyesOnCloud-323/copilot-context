from flask import Flask, jsonify, request

from app.auth import create_token, hash_password, require_auth, verify_password
from app.db import add_user, get_user
from app.utils import format_error

app = Flask(__name__)

add_user("asha", hash_password("asha123"), "admin")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username", "")
    password = data.get("password", "")
    if not verify_password(username, password):
        return format_error("invalid credentials", 401)
    return jsonify({"token": create_token(username)})

@app.route("/profile")
@require_auth
def profile(username):
    user = get_user(username)
    return jsonify({"username": username, "role": user["role"]})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})
