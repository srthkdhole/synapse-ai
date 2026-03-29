# 🚀 Synapse AI – Business Analytics Platform

An AI-powered analytics platform that provides business insights using real-time data, interactive dashboards, and Retrieval-Augmented Generation (RAG).

---

## 📊 Features

* 📈 KPI Dashboard (Sales, Orders, Avg Sales)
* 🏙️ City & Product Analysis
* 📅 Time-Series Trend Analysis
* 🤖 AI-Powered Business Insights (RAG)
* ⚡ Quick Insights & Decision Engine
* 🔍 City-specific AI Analysis
* ⚠️ Anomaly Detection

---

## 🧠 Architecture

```
Data → MySQL → Agents → Services → FastAPI → Streamlit UI → AI (RAG)
```

---

## 🛠️ Tech Stack

* Backend: FastAPI
* Frontend: Streamlit
* Database: MySQL
* AI: Ollama (Phi Model)
* RAG: LangChain + FAISS
* Language: Python

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/srthkdhole/synapse-ai.git
cd synapse-ai
```

### 2. Create Virtual Environment

```
py -3.11 -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Backend

```
uvicorn backend.app.main:app --reload
```

### 5. Run Frontend

```
streamlit run frontend/app.py
```

---

## 📡 API Endpoints

* `/analytics/kpi`
* `/analytics/city`
* `/ai-decision`
* `/ai-quick`
* `/ai-city/{city}`

---

## 📸 Screenshots

(Add screenshots here)

---

## 🎯 Future Improvements

* Dark mode UI
* Chat-based AI interface
* Deployment (Cloud)

---

## 👨‍💻 Author

Sarthak Dhole
Aspiring Data Analyst | AI Builder 🚀

---

