from flask import Blueprint, jsonify
from middleware.auth_middleware import token_required
from models.transaction_model import get_transactions_by_user

transaction_bp = Blueprint('transactions', __name__)


@transaction_bp.route('/transactions', methods=['GET'])
@token_required
def get_transactions(current_user_id):
    data = get_transactions_by_user(current_user_id)

    return jsonify({
        "message": "Transactions fetched successfully",
        "data": data
    }), 200