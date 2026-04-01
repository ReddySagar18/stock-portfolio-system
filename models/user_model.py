from database import get_db_connection


def create_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        return cursor.lastrowid  # return created user id

    except Exception as e:
        return None

    finally:
        conn.close()


def get_user_by_username(username):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    )

    user = cursor.fetchone()
    conn.close()

    return user