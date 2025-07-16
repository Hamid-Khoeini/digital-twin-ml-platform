import streamlit as st

def show():
    st.header("📊 Digital Twin Strategic Overview")
    st.markdown("""
    Welcome to the ML-powered Digital Twin platform. This tool enables modular simulation, analysis, 
    and decision-making across various domains including Finance, Human Body, Energy, and Urban Planning.

    Use the sidebar to navigate between different domain-specific dashboards.
    """)
    
    st.markdown("### 🔧 Architecture Flow")
    st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MyPOV0dBP-YvbtzA7cW1Aw.png", caption="Typical Digital Twin Architecture (for illustration)")
    
    st.success("This platform is modular — each team can customize their domain’s dashboard independently.")
