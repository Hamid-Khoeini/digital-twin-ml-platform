# app.py
import streamlit as st
from modules import finance, health, energy, city
from utils.overview import show as show_overview  # ⬅️ این خط اصلاح‌شده

st.set_page_config(page_title="Digital Twin ML Platform", layout="wide")

with st.sidebar:
    st.title("🧠 Digital Twin Navigator")
    page = st.radio("Select Domain", ["Overview", "Finance", "Health", "Energy", "City Planning"])

if page == "Overview":
    show_overview()
elif page == "Finance":
    finance.run()
elif page == "Health":
    health.run()
elif page == "Energy":
    energy.run()
elif page == "City Planning":
    city.run()
