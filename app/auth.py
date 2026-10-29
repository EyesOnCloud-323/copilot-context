import base64
import hashlib
import hmac
import time
from functools import wraps

from flask import jsonify, request

from app import config
from app.db import get_user

def hash_password(password):
    return hashlib.pbkdf2_hmac(
        "sha256", password.encode(), config.SECRET_KEY.encode(), 100_000
    ).hex()

def verify_password(username, password):
    user = get_user(username)
    if not user:
        return False
    return hmac.compare_digest(user["password_hash"], hash_password(password))

def _sign(payload):
    return hmac.new(config.SECRET_KEY.encode(), payload.encode(), "sha256").hexdigest()

def create_token(username):
    expires = int(time.time()) + config.TOKEN_TTL_SECONDS
    payload = f"{username}:{expires}"
    raw = f"{payload}:{_sign(payload)}"
    return base64.urlsafe_b64encode(raw.encode()).decode()

def decode_token(token):
    try:
        raw = base64.urlsafe_b64decode(token.encode()).decode()
        username, expires, signature = raw.split(":")
    except Exception:
        return None
    if not hmac.compare_digest(signature, _sign(f"{username}:{expires}")):
        return None
    if int(expires) < time.time():
        return None
    return username


def require_auth(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization", "")
        username = decode_token(header.removeprefix("Bearer "))
        if not username:
            return jsonify({"error": "unauthorized"}), 401
        return view(username, *args, **kwargs)

    return wrapper
