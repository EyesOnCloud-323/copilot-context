import os

SECRET_KEY = os.getenv("APP_SECRET_KEY", "dev-secret")
TOKEN_TTL_SECONDS = 3600
