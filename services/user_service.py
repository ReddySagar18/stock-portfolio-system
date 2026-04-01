from models.user_model import create_user, get_user_by_username
import jwt
import datetime
import bcrypt

SECRET_KEY = "your_secret_key"


def register_user(username, password):
    existing_user = get_user_by_username(username)

    if existing_user:
        return {
            "message": "User already exists"
        }, 400

    # 🔐 HASH PASSWORD
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    user_id = create_user(username, hashed_password)

    if not user_id:
        return {
            "message": "User registration failed"
        }, 500

    return {
        "message": "User registered successfully",
        "user_id": user_id
    }, 201


def login_user(username, password):
    user = get_user_by_username(username)

    if not user:
        return {
            "message": "User not found"
        }, 404

    # 🔐 CHECK HASHED PASSWORD
    if not bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return {
            "message": "Invalid password"
        }, 401

    token = jwt.encode(
        {
            "user_id": user["id"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        },
        SECRET_KEY,
        algorithm="HS256"
    )

    return {
        "message": "Login successful",
        "token": token
    }, 200