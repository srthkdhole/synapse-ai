from backend.app.db.database import get_db_connection


# -------------------------
# CITY INSIGHTS
# -------------------------
def city_insights():
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

        if not data:
            return {"error": "No data found"}

        return {
            "top_city": data[0],
            "lowest_city": data[-1],
            "all_data": data
        }

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# PRODUCT INSIGHTS
# -------------------------
def product_insights():
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

        if not data:
            return {"error": "No data"}

        return {
            "top_product": data[0],
            "lowest_product": data[-1],
            "all_data": data
        }

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# SALES TREND (TIME SERIES)
# -------------------------
def sales_trend():
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
# CUSTOMER INSIGHTS
# -------------------------
def customer_insights():
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
# KPI SUMMARY
# -------------------------
def kpi_summary():
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
# COMBINED BUSINESS INSIGHT
# -------------------------
def business_insight_summary():
    try:
        city = city_insights()
        product = product_insights()
        kpi = kpi_summary()

        return {
            "kpi": kpi,
            "top_city": city.get("top_city"),
            "top_product": product.get("top_product"),
            "message": "Focus on top-performing city and product to scale business."
        }

    except Exception as e:
        return {"error": str(e)}