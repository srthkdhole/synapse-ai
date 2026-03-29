import pandas as pd
import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Srthk123",
    "database": "synapse_ai",
}

CSV_PATH = "data/sales_data.csv"


def insert_data():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        df = pd.read_csv(CSV_PATH)

        print("CSV Loaded:", df.shape)

        if df.empty:
            print("❌ CSV is empty")
            return

        for i, row in df.iterrows():
            cursor.execute("""
                INSERT INTO sales (
                    order_id, date, city, product, category,
                    customer_type, payment_mode, quantity, price, total_sales
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                int(row["order_id"]),
                row["date"],
                row["city"],
                row["product"],
                row["category"],
                row["customer_type"],
                row["payment_mode"],
                int(row["quantity"]),
                int(row["price"]),
                int(row["total_sales"])
            ))

            if i % 50 == 0:
                print(f"Inserted {i} rows...")

        conn.commit()
        cursor.close()
        conn.close()

        print("✅ ALL DATA INSERTED SUCCESSFULLY")

    except Exception as e:
        print("❌ ERROR:", e)


if __name__ == "__main__":
    insert_data()