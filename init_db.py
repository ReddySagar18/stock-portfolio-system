from database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

# USERS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

# PORTFOLIO TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS portfolio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    stock_name TEXT,
    quantity INTEGER,
    buy_price REAL,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

# 🔥 NEW: TRANSACTIONS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    stock_name TEXT,
    action TEXT,
    quantity INTEGER,
    price REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

conn.commit()
conn.close()

print("Database initialized successfully")