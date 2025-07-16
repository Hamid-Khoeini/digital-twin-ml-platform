import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

def run():
    st.header("🏙️ Urban Planning Digital Twin")
    st.markdown("This module explores simulations of urban metrics like traffic flow, pollution, and population density.")

    # Mock data
    sectors = ["North", "South", "East", "West", "Center"]
    traffic = np.random.randint(50, 100, size=5)
    pollution = np.random.uniform(20, 80, size=5)
    df = pd.DataFrame({
        "Sector": sectors,
        "Traffic": traffic,
        "Pollution Index": pollution
    })

    st.subheader("🚦 Traffic & Pollution by City Sector")
    fig = px.scatter(df, x="Traffic", y="Pollution Index", color="Sector", size="Pollution Index", hover_name="Sector")
    st.plotly_chart(fig)

    st.markdown("### 🏗️ Zoning Recommendation")
    st.warning("High traffic in 'Center' zone suggests need for traffic control policies.")
