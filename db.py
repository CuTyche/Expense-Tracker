import sqlite3
from logger import get_logger

logger = get_logger()

def connect_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        );
    """)
    conn.commit()
    return conn

def add_expense(category, amount, description):
    conn = None
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO expenses (category, amount, description) VALUES (?, ?, ?);",
            (category, amount, description)
        )
        conn.commit()
        logger.info(f"Added expense: Category={category}, Amount={amount}, Desc={description}")
    except Exception as e:
        logger.error(f"Failed to add expense: {e}")
    finally:
        if conn:
            conn.close()

def get_expenses():
    conn = None
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses;")
        return cursor.fetchall()
    except Exception as e:
        logger.error(f"Failed to fetch expenses: {e}")
        return []
    finally:
        if conn:
            conn.close()
