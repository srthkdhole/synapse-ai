import streamlit as st
import requests
import pandas as pd

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(page_title="Synapse AI", layout="wide")

API_BASE = "http://127.0.0.1:8000"

# -------------------------
# STYLE
# -------------------------
st.markdown("""
<style>
.main-title {
    font-size: 32px;
    font-weight: bold;
    color: #4CAF50;
}
.card {
    padding: 15px;
    border-radius: 10px;
    background-color: #f5f5f5;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("🚀 Synapse AI")

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Analytics", "AI Insights"]
)

# =====================================================
# 🏠 DASHBOARD
# =====================================================
if page == "Dashboard":

    st.markdown('<p class="main-title">📊 Business Dashboard</p>', unsafe_allow_html=True)

    # KPI
    kpi = requests.get(f"{API_BASE}/analytics/kpi").json()

    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Total Sales", kpi.get("total_sales", 0))
    col2.metric("📦 Orders", kpi.get("total_orders", 0))
    col3.metric("📊 Avg Sales", round(kpi.get("avg_sales", 0), 2))

    st.divider()

    # Charts row
    col1, col2 = st.columns(2)

    # City Sales
    with col1:
        st.subheader("🏙️ City Sales")
        city_data = requests.get(f"{API_BASE}/analytics/city").json()
        df_city = pd.DataFrame(city_data)
        if not df_city.empty:
            st.bar_chart(df_city.set_index("city"))

    # Product Sales
    with col2:
        st.subheader("📦 Product Sales")
        product_data = requests.get(f"{API_BASE}/analytics/product").json()
        df_product = pd.DataFrame(product_data)
        if not df_product.empty:
            st.bar_chart(df_product.set_index("product"))

# =====================================================
# 📊 ANALYTICS PAGE
# =====================================================
elif page == "Analytics":

    st.markdown('<p class="main-title">📊 Advanced Analytics</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input("Start Date")

    with col2:
        end_date = st.date_input("End Date")

    if st.button("Apply Filter"):
        res = requests.get(
            f"{API_BASE}/analytics/date-range",
            params={"start": start_date, "end": end_date}
        )
        data = res.json()

        df = pd.DataFrame(data)
        st.write("Filtered Data", df)

    st.divider()

    # Trend
    st.subheader("📈 Daily Sales Trend")

    trend = requests.get(f"{API_BASE}/analytics/daily").json()
    df_trend = pd.DataFrame(trend)

    if not df_trend.empty:
        st.line_chart(df_trend.set_index("date"))

# =====================================================
# 🤖 AI INSIGHTS
# =====================================================
elif page == "AI Insights":

    st.markdown('<p class="main-title">🤖 AI Insights</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # Full Decision
    if col1.button("📊 Generate Full Decision"):
        res = requests.get(f"{API_BASE}/ai-decision").json()
        st.success("AI Decision Generated")
        st.json(res)

    # Quick Insight
    if col2.button("⚡ Quick Insight"):
        res = requests.get(f"{API_BASE}/ai-quick").json()
        st.info(res)

    st.divider()

    # City Insight
    st.subheader("🏙️ City AI Insight")

    city = st.text_input("Enter City Name")

    if st.button("Get City Insight"):
        if city:
            res = requests.get(f"{API_BASE}/ai-city/{city}").json()
            st.json(res)

    # Trend Insight
    if st.button("📈 Trend Insight"):
        res = requests.get(f"{API_BASE}/ai-trend").json()
        st.json(res)

    # Anomaly
    if st.button("⚠️ Detect Anomaly"):
        res = requests.get(f"{API_BASE}/ai-anomaly").json()
        st.json(res)