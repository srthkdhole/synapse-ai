from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM


# -------------------------
# MODEL HANDLER (SMART SWITCH)
# -------------------------
def get_llm_model():
    try:
        return OllamaLLM(model="phi", temperature=0.3)
    except:
        return OllamaLLM(model="phi3:mini", temperature=0.3)


# -------------------------
# MAIN RAG FUNCTION
# -------------------------
def get_rag_response(data, query):
    try:
        if not data:
            return "No data available"

        # -------------------------
        # FORMAT DATA
        # -------------------------
        documents = [
            f"City {item.get('city')} has sales {item.get('total_sales')}"
            for item in data
        ]

        # -------------------------
        # EMBEDDINGS
        # -------------------------
        embeddings = OllamaEmbeddings(model="phi")

        # -------------------------
        # VECTOR STORE
        # -------------------------
        db = FAISS.from_texts(documents, embeddings)

        # -------------------------
        # SEARCH
        # -------------------------
        docs = db.similarity_search(query, k=2)
        context = "\n".join([doc.page_content for doc in docs])

        # -------------------------
        # LLM
        # -------------------------
        llm = get_llm_model()

        prompt = f"""
        You are a business analyst.

        Context:
        {context}

        Question:
        {query}

        Give only 2-3 line actionable insight.
        """

        response = llm.invoke(prompt)

        return response.strip()

    except Exception as e:
        return f"RAG Error: {str(e)}"


# -------------------------
# QUICK INSIGHT
# -------------------------
def get_quick_insight(data):
    return get_rag_response(data, "Give quick 2-line business insight")


# -------------------------
# CITY INSIGHT
# -------------------------
def get_city_insight(data, city_name):
    filtered = [d for d in data if d.get("city") == city_name]

    if not filtered:
        return "No data for this city"

    return get_rag_response(filtered, f"Analyze sales for {city_name}")


# -------------------------
# TREND INSIGHT
# -------------------------
def get_trend_insight(data):
    return get_rag_response(data, "Identify trends and performance pattern")


# -------------------------
# ANOMALY DETECTION
# -------------------------
def detect_anomalies(data):
    return get_rag_response(data, "Find any anomaly in sales data")


# -------------------------
# SUMMARY INSIGHT
# -------------------------
def get_summary_insight(data):
    return get_rag_response(data, "Summarize overall business performance")