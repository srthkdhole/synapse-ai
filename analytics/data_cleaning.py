import pandas as pd
import random
from datetime import datetime, timedelta

# -------------------------
# MASTER DATA
# -------------------------
cities = ["Mumbai", "Pune", "Delhi", "Bangalore", "Hyderabad"]
products = ["Laptop", "Phone", "Tablet", "Headphones"]
categories = {
    "Laptop": "Electronics",
    "Phone": "Electronics",
    "Tablet": "Electronics",
    "Headphones": "Electronics"
}
customers = ["New", "Returning"]
payments = ["UPI", "Card", "Cash"]

# -------------------------
# GENERATE DATA
# -------------------------
rows = []
start_date = datetime(2024, 1, 1)

for i in range(1, 301):  # 300 rows

    product = random.choice(products)
    price = random.randint(5000, 80000)
    quantity = random.randint(1, 5)

    rows.append({
        "order_id": i,
        "date": (start_date + timedelta(days=random.randint(0, 60))).strftime("%Y-%m-%d"),
        "city": random.choice(cities),
        "product": product,
        "category": categories[product],
        "customer_type": random.choice(customers),
        "payment_mode": random.choice(payments),
        "quantity": quantity,
        "price": price,
        "total_sales": price * quantity
    })

# -------------------------
# CREATE DATAFRAME
# -------------------------
df = pd.DataFrame(rows)

# -------------------------
# SAVE CSV
# -------------------------
df.to_csv("data/sales_data.csv", index=False)

print("✅ Dataset generated successfully (300 rows)")
