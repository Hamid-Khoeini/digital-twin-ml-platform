import streamlit as st

def run():
    st.header("🩺 Human Body Digital Twin")
    st.markdown("This module simulates and monitors physiological parameters like heart rate, oxygen level, and temperature.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Heart Rate", "76 bpm")
    col2.metric("SpO2", "98%")
    col3.metric("Temperature", "36.8 °C")

    st.markdown("### 🧬 Sample Insights")
    st.info("Your current vitals are within normal range.")

    st.markdown("### 📈 Simulation Placeholder")
    st.line_chart({
        "Heart Rate": [75, 78, 76, 79, 74, 77],
        "SpO2": [97, 98, 99, 98, 97, 98]
    })
