import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Manufacturing Analytics Dashboard")
st.caption("AI Insights from Manufacturing Data")

# ----------------------------
# LOAD DATA
# ----------------------------

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "tablet_manufacturing_dataset.csv"
)

if not os.path.exists(DATA_PATH):
    st.error("Dataset not found.")
    st.stop()

df = pd.read_csv(DATA_PATH)

# ----------------------------
# KPI CARDS
# ----------------------------

k1, k2, k3, k4 = st.columns(4)

k1.metric("Records", len(df))
k2.metric("Features", len(df.columns))
k3.metric("Average Weight", f"{df['Tablet_Weight'].mean():.2f} mg")
k4.metric("Max Weight", f"{df['Tablet_Weight'].max():.2f} mg")

st.markdown("---")

# ----------------------------
# DATA PREVIEW
# ----------------------------

st.subheader("📋 Dataset Preview")
st.dataframe(df.head(10), use_container_width=True)

st.markdown("---")

# ----------------------------
# CORRELATION
# ----------------------------

st.subheader("🔥 Correlation Heatmap")

corr = df.corr(numeric_only=True)

fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    aspect="auto"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ----------------------------
# DISTRIBUTIONS
# ----------------------------

left, right = st.columns(2)

with left:

    feature = st.selectbox(
        "Distribution",
        df.select_dtypes(include="number").columns
    )

    fig = px.histogram(
        df,
        x=feature,
        nbins=30,
        color_discrete_sequence=["royalblue"]
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    numeric = df.select_dtypes(include="number").columns

    x = st.selectbox("X-axis", numeric)

    y = st.selectbox("Y-axis", numeric, index=1)

    fig = px.scatter(
        df,
        x=x,
        y=y,
        color="Tablet_Weight",
        color_continuous_scale="Viridis"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ----------------------------
# BOXPLOT
# ----------------------------

st.subheader("📦 Feature Spread")

feature2 = st.selectbox(
    "Choose Feature",
    df.select_dtypes(include="number").columns,
    key="box"
)

fig = px.box(
    df,
    y=feature2,
    color_discrete_sequence=["orange"]
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ----------------------------
# SUMMARY
# ----------------------------

st.subheader("📑 Statistical Summary")

st.dataframe(
    df.describe(),
    use_container_width=True
)

st.download_button(
    "📥 Download Dataset",
    df.to_csv(index=False),
    file_name="tablet_manufacturing_dataset.csv",
    mime="text/csv"
)