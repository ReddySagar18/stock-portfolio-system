from database import get_db_connection


def get_portfolio_by_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, stock_name, quantity, buy_price FROM portfolio WHERE user_id = ?",
        (user_id,)
    )

    rows = cursor.fetchall()
    conn.close()

    portfolio = []
    for row in rows:
        portfolio.append({
            "id": row["id"],
            "stock_name": row["stock_name"],
            "quantity": row["quantity"],
            "buy_price": row["buy_price"]
        })

    return portfolio


def add_stock(user_id, stock_name, quantity, buy_price):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO portfolio (user_id, stock_name, quantity, buy_price) VALUES (?, ?, ?, ?)",
        (user_id, stock_name, quantity, buy_price)
    )

    conn.commit()
    conn.close()

    return True


def update_stock(user_id, stock_id, quantity, buy_price):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE portfolio
        SET quantity = ?, buy_price = ?
        WHERE id = ? AND user_id = ?
        """,
        (quantity, buy_price, stock_id, user_id)
    )

    conn.commit()
    conn.close()

    return True


def delete_stock(user_id, stock_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM portfolio WHERE id = ? AND user_id = ?",
        (stock_id, user_id)
    )

    conn.commit()
    conn.close()

    return True