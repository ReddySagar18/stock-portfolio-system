from models.portfolio_model import get_portfolio_by_user, add_stock, update_stock
from models.portfolio_model import delete_stock
from models.transaction_model import add_transaction

def fetch_portfolio(user_id):
    data = get_portfolio_by_user(user_id)

    return {
        "message": "Portfolio fetched successfully",
        "data": data
    }, 200

def create_stock(user_id, data):
    if isinstance(data, dict):
        data = [data]

    if not isinstance(data, list) or len(data) == 0:
        return {"message": "Invalid data format"}, 400

    for stock in data:
        stock_name = stock.get('stock_name')
        quantity = stock.get('quantity')
        buy_price = stock.get('buy_price')

        if not stock_name or not quantity or not buy_price:
            continue

        add_stock(user_id, stock_name, quantity, buy_price)

        #  ADD TRANSACTION
        add_transaction(user_id, stock_name, "BUY", quantity, buy_price)

    return {"message": "Stocks added successfully"}, 201


def modify_stock(user_id, stock_id, quantity, buy_price):
    if not stock_id or not quantity or not buy_price:
        return {"message": "All fields are required"}, 400

    rows = update_stock(user_id, stock_id, quantity, buy_price)

    if rows == 0:
        return {"message": "Stock not found or unauthorized"}, 404

    #  ADD TRANSACTION (UPDATE treated as BUY/ADJUST)
    add_transaction(user_id, "UPDATED_STOCK", "UPDATE", quantity, buy_price)

    return {"message": "Stock updated successfully"}, 200
def remove_stock(user_id, stock_id):
    if not stock_id:
        return {"message": "Stock ID is required"}, 400

    rows = delete_stock(user_id, stock_id)

    if rows == 0:
        return {"message": "Stock not found or unauthorized"}, 404

    # 🔥 ADD TRANSACTION
    add_transaction(user_id, "DELETED_STOCK", "SELL", 0, 0)

    return {"message": "Stock deleted successfully"}, 200