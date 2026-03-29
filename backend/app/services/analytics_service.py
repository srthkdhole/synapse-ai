# -------------------------
# IMPORTS
# -------------------------
from backend.app.db.database import get_db_connection


# -------------------------
# KPI SERVICE
# -------------------------
def get_kpi_service():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT SUM(total_sales) as total_sales FROM sales")
        total = cursor.fetchone()

        cursor.execute("SELECT COUNT(*) as total_orders FROM sales")
        orders = cursor.fetchone()

        cursor.execute("SELECT AVG(total_sales) as avg_sales FROM sales")
        avg = cursor.fetchone()

        cursor.close()
        conn.close()

        return {
            "total_sales": total["total_sales"] or 0,
            "total_orders": orders["total_orders"] or 0,
            "avg_sales": avg["avg_sales"] or 0
        }

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# CITY SALES
# -------------------------
def get_city_sales_service():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT city, SUM(total_sales) as total_sales
            FROM sales
            GROUP BY city
            ORDER BY total_sales DESC
        """)

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# PRODUCT SALES
# -------------------------
def get_product_sales_service():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT product, SUM(total_sales) as total_sales
            FROM sales
            GROUP BY product
            ORDER BY total_sales DESC
        """)

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# CATEGORY SALES
# -------------------------
def get_category_sales_service():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT category, SUM(total_sales) as total_sales
            FROM sales
            GROUP BY category
            ORDER BY total_sales DESC
        """)

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# DAILY SALES (TREND)
# -------------------------
def get_daily_sales_service():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT date, SUM(total_sales) as daily_sales
            FROM sales
            GROUP BY date
            ORDER BY date
        """)

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# CUSTOMER ANALYSIS
# -------------------------
def get_customer_service():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT customer_type, COUNT(*) as count
            FROM sales
            GROUP BY customer_type
        """)

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# TOP PRODUCTS
# -------------------------
def get_top_products_service():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT product, SUM(total_sales) as total_sales
            FROM sales
            GROUP BY product
            ORDER BY total_sales DESC
            LIMIT 3
        """)

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# DATE RANGE FILTER
# -------------------------
def get_date_range_service(start, end):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM sales
            WHERE date BETWEEN %s AND %s
        """, (start, end))

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data

    except Exception as e:
        return {"error": str(e)}