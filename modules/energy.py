import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def run():
    st.header("⚡ Energy Digital Twin")
    st.markdown("This module simulates energy consumption, forecasting, and efficiency in smart grids.")

    # Fake data
    days = pd.date_range(end=pd.Timestamp.today(), periods=30)
    usage = np.random.normal(loc=200, scale=30, size=30)
    df = pd.DataFrame({"Date": days, "Energy Usage (kWh)": usage})

    st.subheader("📊 Energy Consumption (Last 30 Days)")
    fig = px.line(df, x="Date", y="Energy Usage (kWh)", title="Daily Energy Usage")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### ⚙️ Forecast Efficiency")
    st.slider("Smart Grid Optimization Level", 0, 100, 50)
    st.success("Optimized grid can reduce peak load by 12% under current config.")
