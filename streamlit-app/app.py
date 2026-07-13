import streamlit as st
import pandas as pd
import joblib

import os

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "tablet_weight_model.pkl"
)

model = joblib.load(MODEL_PATH)

st.title("🏭 Industrial Powder Filling AI")

powder_density = st.slider("Powder Density", 0.5, 1.5, 0.8)
moisture_content = st.slider("Moisture Content", 0.0, 10.0, 3.2)
particle_size = st.slider("Particle Size", 50, 300, 140)
compression_force = st.slider("Compression Force", 5, 30, 18)
machine_speed = st.slider("Machine Speed", 100, 500, 250)
fill_depth = st.slider("Fill Depth", 5.0, 10.0, 7.5)
ambient_temperature = st.slider("Ambient Temperature", 15, 40, 25)
relative_humidity = st.slider("Relative Humidity", 20, 80, 45)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "Powder_Density":[powder_density],
        "Moisture_Content":[moisture_content],
        "Particle_Size":[particle_size],
        "Compression_Force":[compression_force],
        "Machine_Speed":[machine_speed],
        "Fill_Depth":[fill_depth],
        "Ambient_Temperature":[ambient_temperature],
        "Relative_Humidity":[relative_humidity]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Tablet Weight: {prediction[0]:.2f} mg")