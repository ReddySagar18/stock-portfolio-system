from flask import Blueprint, request, jsonify
from services.user_service import register_user, login_user

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    response, status = register_user(username, password)

    return jsonify(response), status


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    response, status = login_user(username, password)

    return jsonify(response), status