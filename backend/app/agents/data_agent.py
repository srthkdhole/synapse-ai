from backend.app.db.database import get_db_connection


# -------------------------
# BASIC DATA (FOR AI / RAG)
# -------------------------
def fetch_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT city, total_sales FROM sales")
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        # Clean data
        data = [d for d in data if d["total_sales"] and d["total_sales"] > 0]

        return data

    except Exception as e:
        print("❌ fetch_data Error:", e)
        return []


# -------------------------
# TOP CITIES
# -------------------------
def fetch_top_cities():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT city, SUM(total_sales) as total_sales
            FROM sales
            GROUP BY city
            ORDER BY total_sales DESC
            LIMIT 3
        """)

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data

    except Exception as e:
        print("❌ fetch_top_cities Error:", e)
        return []


# -------------------------
# FILTER BY CITY
# -------------------------
def fetch_by_city(city_name):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM sales
            WHERE city = %s
        """, (city_name,))

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data

    except Exception as e:
        print("❌ fetch_by_city Error:", e)
        return []


# -------------------------
# SUMMARY DATA
# -------------------------
def fetch_summary():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT SUM(total_sales) as total_sales FROM sales")
        total = cursor.fetchone()

        cursor.execute("SELECT COUNT(*) as total_orders FROM sales")
        orders = cursor.fetchone()

        cursor.close()
        conn.close()

        return {
            "total_sales": total["total_sales"] if total else 0,
            "total_orders": orders["total_orders"] if orders else 0
        }

    except Exception as e:
        print("❌ fetch_summary Error:", e)
        return {"total_sales": 0, "total_orders": 0}