from fastapi import FastAPI

# -------------------------
# IMPORT SERVICES
# -------------------------
from backend.app.services.ai_service import (
    ai_full_decision,
    ai_quick_insight_service,
    ai_city_service,
    ai_trend_service,
    ai_anomaly_service,
    ai_summary_service,
    ai_top_city_service
)

from backend.app.services.analytics_service import (
    get_kpi_service,
    get_city_sales_service,
    get_product_sales_service,
    get_category_sales_service,
    get_daily_sales_service,
    get_customer_service,
    get_top_products_service,
    get_date_range_service
)

# -------------------------
# INIT APP
# -------------------------
app = FastAPI(title="Synapse AI API 🚀")


# -------------------------
# HOME
# -------------------------
@app.get("/")
def home():
    return {"message": "Synapse AI Running 🚀"}


# =====================================================
# 🤖 AI ENDPOINTS
# =====================================================

@app.get("/ai-decision")
def ai_decision():
    return ai_full_decision()


@app.get("/ai-quick")
def ai_quick():
    return ai_quick_insight_service()


@app.get("/ai-city/{city}")
def ai_city(city: str):
    return ai_city_service(city)


@app.get("/ai-trend")
def ai_trend():
    return ai_trend_service()


@app.get("/ai-anomaly")
def ai_anomaly():
    return ai_anomaly_service()


@app.get("/ai-summary")
def ai_summary():
    return ai_summary_service()


@app.get("/ai-top-city")
def ai_top_city():
    return ai_top_city_service()


# =====================================================
# 📊 ANALYTICS ENDPOINTS
# =====================================================

@app.get("/analytics/kpi")
def kpi():
    return get_kpi_service()


@app.get("/analytics/city")
def city():
    return get_city_sales_service()


@app.get("/analytics/product")
def product():
    return get_product_sales_service()


@app.get("/analytics/category")
def category():
    return get_category_sales_service()


@app.get("/analytics/daily")
def daily():
    return get_daily_sales_service()


@app.get("/analytics/customer")
def customer():
    return get_customer_service()


@app.get("/analytics/top-products")
def top_products():
    return get_top_products_service()


@app.get("/analytics/date-range")
def date_range(start: str, end: str):
    return get_date_range_service(start, end)