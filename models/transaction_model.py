from database import get_db_connection


def add_transaction(user_id, stock_name, action, quantity, price):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO transactions (user_id, stock_name, action, quantity, price)
        VALUES (?, ?, ?, ?, ?)
        """,
        (user_id, stock_name, action, quantity, price)
    )

    conn.commit()
    conn.close()

    return True


def get_transactions_by_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, stock_name, action, quantity, price, created_at
        FROM transactions
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    rows = cursor.fetchall()
    conn.close()

    data = []
    for row in rows:
        data.append({
            "id": row["id"],
            "stock_name": row["stock_name"],
            "action": row["action"],
            "quantity": row["quantity"],
            "price": row["price"],
            "created_at": row["created_at"]
        })

    return data