import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="Industrial Powder Filling AI",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# LOAD CSS
# =========================
css_path = os.path.join("assets", "styles.css")

if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
logo_path = os.path.join("assets", "logo.png")

if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.sidebar.image(logo, width=150)

st.sidebar.title("Industrial AI")

st.sidebar.success("🟢 System Online")

st.sidebar.markdown("---")

st.sidebar.info("""
### Modules

📊 Dashboard

🤖 Prediction

📈 Analytics

ℹ️ About
""")

st.sidebar.markdown("---")

st.sidebar.caption("Version 3.0")

# =========================
# HOME PAGE
# =========================

st.title("🏭 Industrial Powder Filling AI")

st.markdown("## AI Powered Manufacturing Decision Support Platform")

st.success("👈 Select a module from the left sidebar.")

st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Production Lines", "12")

with c2:
    st.metric("Models Running", "1")

with c3:
    st.metric("System Health", "100%")

st.markdown("---")

st.header("Welcome")

st.write("""
This platform demonstrates how Artificial Intelligence can improve
industrial tablet manufacturing through machine learning.

### Included Modules

- Dashboard
- Prediction
- Analytics
- About

Navigate using the left sidebar.
""")