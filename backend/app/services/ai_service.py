# -------------------------
# IMPORTS
# -------------------------
from backend.app.agents.data_agent import (
    fetch_data,
    fetch_summary,
    fetch_top_cities
)

from backend.app.rag_service import (
    get_rag_response,
    get_quick_insight,
    get_city_insight,
    get_trend_insight,
    detect_anomalies,
    get_summary_insight
)


# -------------------------
# FULL AI DECISION
# -------------------------
def ai_full_decision():
    try:
        data = fetch_data()
        summary = fetch_summary()

        if not data:
            return {"error": "No data available"}

        query = f"""
        Total Sales: {summary['total_sales']}
        Total Orders: {summary['total_orders']}

        Analyze business and give actionable decision.
        """

        decision = get_rag_response(data, query)

        return {
            "summary": summary,
            "decision": decision
        }

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# QUICK AI
# -------------------------
def ai_quick_insight_service():
    try:
        data = fetch_data()
        return {"decision": get_quick_insight(data)}
    except Exception as e:
        return {"error": str(e)}


# -------------------------
# CITY AI
# -------------------------
def ai_city_service(city_name):
    try:
        data = fetch_data()
        decision = get_city_insight(data, city_name)

        return {
            "city": city_name,
            "decision": decision
        }

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# TREND AI
# -------------------------
def ai_trend_service():
    try:
        data = fetch_data()
        return {"trend": get_trend_insight(data)}
    except Exception as e:
        return {"error": str(e)}


# -------------------------
# ANOMALY DETECTION
# -------------------------
def ai_anomaly_service():
    try:
        data = fetch_data()
        return {"anomaly": detect_anomalies(data)}
    except Exception as e:
        return {"error": str(e)}


# -------------------------
# SUMMARY AI
# -------------------------
def ai_summary_service():
    try:
        data = fetch_data()
        return {"summary": get_summary_insight(data)}
    except Exception as e:
        return {"error": str(e)}


# -------------------------
# TOP CITY AI (HYBRID)
# -------------------------
def ai_top_city_service():
    try:
        top_cities = fetch_top_cities()

        if not top_cities:
            return {"error": "No data"}

        top_city = top_cities[0]["city"]

        decision = get_city_insight(fetch_data(), top_city)

        return {
            "top_city": top_city,
            "decision": decision
        }

    except Exception as e:
        return {"error": str(e)}