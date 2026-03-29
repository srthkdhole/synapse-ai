import mysql.connector
from mysql.connector import Error


# -------------------------
# DB CONFIG (EDIT THIS)
# -------------------------
DB_CONFIG = {
    "host": "127.0.0.1",   # try "127.0.0.1" if issue
    "user": "root",
    "password": "Srthk123",   # 👈 change this
    "database": "synapse_ai"
}


# -------------------------
# GET DB CONNECTION
# -------------------------
def get_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)

        if conn.is_connected():
            return conn

    except Error as e:
        print("❌ Database Connection Error:", e)

    return None


# -------------------------
# TEST CONNECTION (OPTIONAL)
# -------------------------
def test_connection():
    conn = get_db_connection()

    if conn:
        print("✅ Database connected successfully")
        conn.close()
    else:
        print("❌ Database connection failed")