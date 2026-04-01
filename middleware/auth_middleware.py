from functools import wraps
from flask import request, jsonify
import jwt

SECRET_KEY = "your_secret_key"


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Get token from header
        auth_header = request.headers.get('Authorization')

        if auth_header:
            token = auth_header.split(" ")[1]

        if not token:
            return jsonify({"message": "Token is missing"}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user_id = data["user_id"]

        except:
            return jsonify({"message": "Token is invalid or expired"}), 401

        return f(current_user_id, *args, **kwargs)

    return decorated