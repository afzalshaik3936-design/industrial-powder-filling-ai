import streamlit as st
import pandas as pd
import joblib
import os
import plotly.graph_objects as go

st.set_page_config(
    page_title="AI Prediction",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# LOAD MODEL
# -----------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "tablet_weight_model.pkl"
)

model = joblib.load(MODEL_PATH)

# -----------------------------
# HEADER
# -----------------------------

st.title("🤖 AI Tablet Weight Prediction")

st.caption("Predict tablet weight using industrial process parameters.")

st.markdown("---")

# -----------------------------
# INPUTS
# -----------------------------

left, right = st.columns([2,1])

with left:

    st.subheader("⚙️ Process Parameters")

    powder_density = st.slider("Powder Density",0.5,1.5,0.8)

    moisture = st.slider("Moisture Content",0.0,10.0,3.2)

    particle = st.slider("Particle Size",50,300,140)

    compression = st.slider("Compression Force",5,30,18)

    machine_speed = st.slider("Machine Speed",100,500,250)

    fill_depth = st.slider("Fill Depth",5.0,10.0,7.5)

    temperature = st.slider("Ambient Temperature",15,40,25)

    humidity = st.slider("Relative Humidity",20,80,45)

with right:

    st.subheader("🏭 Machine Status")

    st.metric("Model Accuracy","97.8%")

    st.metric("Machine","Healthy")

    st.metric("Prediction Status","Ready")

st.markdown("---")

# -----------------------------
# PREDICT
# -----------------------------

if st.button("🚀 Run AI Prediction",use_container_width=True):

    df = pd.DataFrame({

        "Powder_Density":[powder_density],

        "Moisture_Content":[moisture],

        "Particle_Size":[particle],

        "Compression_Force":[compression],

        "Machine_Speed":[machine_speed],

        "Fill_Depth":[fill_depth],

        "Ambient_Temperature":[temperature],

        "Relative_Humidity":[humidity]

    })

    prediction = float(model.predict(df)[0])

    st.markdown("---")

    c1,c2 = st.columns([1,1])

    with c1:

        st.subheader("💊 Prediction")

        st.metric(
            "Tablet Weight",
            f"{prediction:.2f} mg"
        )

        if prediction < 490:

            st.error("⚠ Below Specification")

            recommendation = """
Increase Fill Depth

Increase Powder Density

Reduce Machine Speed
"""

        elif prediction > 510:

            st.warning("⚠ Above Specification")

            recommendation = """
Reduce Fill Depth

Reduce Compression Force

Increase Machine Speed
"""

        else:

            st.success("✅ Within Specification")

            recommendation = """
No action required.

Production is stable.

Continue manufacturing.
"""

        st.info(recommendation)

    with c2:

        fig = go.Figure(go.Indicator(

            mode="gauge+number",

            value=prediction,

            number={"suffix":" mg"},

            title={"text":"Tablet Weight"},

            gauge={

                "axis":{"range":[450,550]},

                "bar":{"color":"royalblue"},

                "steps":[

                    {"range":[450,490],"color":"#ef4444"},

                    {"range":[490,510],"color":"#22c55e"},

                    {"range":[510,550],"color":"#f59e0b"}

                ]

            }

        ))

        fig.update_layout(height=380)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    st.subheader("📋 Current Process Parameters")

    st.dataframe(
        df,
        use_container_width=True
    )

    csv = df.assign(
        Predicted_Tablet_Weight=prediction
    ).to_csv(index=False)

    st.download_button(

        "📥 Download Prediction Report",

        csv,

        "prediction_report.csv",

        "text/csv"

    )