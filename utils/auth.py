from functools import wraps

import jwt
from flask import request, abort

from constants import TOKEN_SECRET, TOKEN_ALGO


def check_token(auth_header):
    if not auth_header or not auth_header.startswith("Bearer "):
        abort(401, "Token is missing or invalid")

    token = auth_header.split("Bearer ")[-1].strip()

    try:
        user = jwt.decode(jwt=token, key=TOKEN_SECRET, algorithms=[TOKEN_ALGO])
        return user
    except Exception as e:
        abort(401, f"{e}")


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        auth_header = request.headers.get("Authorization")
        check_token(auth_header)

        return func(*args, **kwargs)
    return wrapper

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        auth_header = request.headers.get("Authorization")
        user = check_token(auth_header)

        if user.get("role") not in ["admin", "supermegauser"]:
            abort(403, "Admin role required")

        return func(*args, **kwargs)
    return wrapper

