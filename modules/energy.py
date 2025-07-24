# modules/energy.py

import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import plotly.express as px

# آدرس سنسور
SENSOR_URL = "http://192.168.43.93/data"

# مقداردهی اولیه دیتا در session_state
if "sensor_data" not in st.session_state:
    st.session_state.sensor_data = pd.DataFrame(columns=["timestamp", "temperature", "humidity"])

# تابع دریافت داده از سنسور
def fetch_sensor_data():
    try:
        response = requests.get(SENSOR_URL, timeout=2)
        if response.status_code == 200:
            json_data = response.json()
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_row = {
                "timestamp": now,
                "temperature": json_data["temp"],
                "humidity": json_data["hum"]
            }
            st.session_state.sensor_data = pd.concat(
                [st.session_state.sensor_data, pd.DataFrame([new_row])],
                ignore_index=True
            ).tail(100)  # فقط ۱۰۰ رکورد آخر
        else:
            st.warning(f"❌ Server returned status code: {response.status_code}")
    except Exception as e:
        st.error(f"⚠️ Error fetching sensor data: {e}")

def run():
    st.header("⚡ Real-time Energy Monitoring")
    st.markdown("Live dashboard from temperature & humidity sensors in the smart grid environment.")

    fetch_sensor_data()  # دریافت داده

    df = st.session_state.sensor_data

    if df.empty:
        st.info("No sensor data yet...")
        return

    # بخش نمودار و جدول
    col_chart, col_table = st.columns([3, 1])

    with col_chart:
        st.subheader("📉 Sensor Data Over Time")
        fig = px.line(
            df,
            x="timestamp",
            y=["temperature", "humidity"],
            labels={"value": "Value", "timestamp": "Time"},
            title="Temperature & Humidity Readings"
        )
        fig.update_layout(
            xaxis=dict(rangeslider_visible=True),
            yaxis_title="Value",
            legend_title_text="Measurement",
            hovermode="x unified"
        )
        fig.update_traces(mode="lines+markers")
        st.plotly_chart(fig, use_container_width=True)

        # متریک‌ها
        latest = df.iloc[-1]
        col1, col2 = st.columns(2)
        col1.metric("🌡️ Temp (°C)", f"{latest['temperature']:.2f}")
        col2.metric("💧 Humidity (%)", f"{latest['humidity']:.2f}")

    with col_table:
        st.subheader("📋 Last Logs")
        st.dataframe(df.tail(10).set_index("timestamp"), height=300, use_container_width=True)

    # دکمه به‌روزرسانی دستی
    if st.button("🔄 Refresh Now"):
        st.rerun()

    # به‌روزرسانی خودکار با countdown (optional)
    st.markdown("⏱️ This page refreshes automatically every 5 seconds.")
    st.experimental_set_query_params(tick=datetime.now().strftime("%H:%M:%S"))
    st.experimental_rerun()
