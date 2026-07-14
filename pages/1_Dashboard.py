import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("🏭 Industrial Powder Filling AI")
st.subheader("AI Powered Manufacturing Decision Support System")

st.markdown("---")

k1, k2, k3, k4 = st.columns(4)

k1.metric("🎯 Accuracy", "97.8%")
k2.metric("🧠 Model", "Linear Regression")
k3.metric("⚙️ Status", "Healthy")
k4.metric("📦 Features", "8")

st.markdown("---")

left, right = st.columns([2,1])

with left:

    st.header("🏭 Factory Status")

    st.success("🟢 Machine A : Running")

    st.success("🟢 Machine B : Running")

    st.warning("🟡 Machine C : Maintenance Soon")

    st.info("📦 Current Batch : BT-2026-0714")

with right:

    st.header("🤖 AI Recommendation")

    st.success("""
Production is operating normally.

• Tablet weight stable

• Moisture level acceptable

• Compression force optimal

• No action required
""")

st.markdown("---")

st.header("Welcome")

st.write("""
This AI dashboard predicts tablet weight using machine learning.

### Available Modules

- 📊 Dashboard
- 🎯 Prediction
- 📈 Analytics
- ℹ️ About

Use the sidebar to navigate between pages.
""")