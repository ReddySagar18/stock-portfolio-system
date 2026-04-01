from flask import Blueprint, request, jsonify
from services.portfolio_service import (
    fetch_portfolio,
    create_stock,
    modify_stock,
    remove_stock
)
from middleware.auth_middleware import token_required

portfolio_bp = Blueprint('portfolio', __name__)


@portfolio_bp.route('/portfolio', methods=['GET'])
@token_required
def get_portfolio(current_user_id):
    response, status = fetch_portfolio(current_user_id)
    return jsonify(response), status


@portfolio_bp.route('/portfolio', methods=['POST'])
@token_required
def add_portfolio(current_user_id):
    data = request.get_json()

    response, status = create_stock(current_user_id, data)
    return jsonify(response), status


@portfolio_bp.route('/portfolio', methods=['PUT'])
@token_required
def update_portfolio(current_user_id):
    data = request.get_json()

    stock_id = data.get('id')
    quantity = data.get('quantity')
    buy_price = data.get('buy_price')

    response, status = modify_stock(
        current_user_id, stock_id, quantity, buy_price
    )

    return jsonify(response), status


@portfolio_bp.route('/portfolio', methods=['DELETE'])
@token_required
def delete_portfolio(current_user_id):
    data = request.get_json()

    stock_id = data.get('id')

    response, status = remove_stock(current_user_id, stock_id)

    return jsonify(response), status