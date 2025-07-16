# modules/finance.py
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def run():
    st.header("💵 Finance Twin")
    st.markdown("Analysis of financial KPIs, dimensionality reduction and risk mapping")

    # Synthetic data
    df = pd.read_csv("data/finance.csv")

    # KPI cards
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"${df['revenue'].sum():,.0f}")
    col2.metric("Avg Profit", f"${df['profit'].mean():,.0f}")
    col3.metric("Risk Level", "Moderate")

    # PCA
    st.subheader("PCA Projection")
    features = ['revenue', 'profit', 'expenses']
    x = StandardScaler().fit_transform(df[features])
    pca = PCA(n_components=2)
    components = pca.fit_transform(x)
    pca_df = pd.DataFrame(data=components, columns=['PC1', 'PC2'])
    pca_df["dept"] = df["department"]

    fig = px.scatter(pca_df, x="PC1", y="PC2", color="dept", title="Principal Component Projection")
    st.plotly_chart(fig, use_container_width=True)

    # Data Table
    with st.expander("🔍 Raw Data"):
        st.dataframe(df)
