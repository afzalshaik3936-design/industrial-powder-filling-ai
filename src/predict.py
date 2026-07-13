import pandas as pd
import joblib

# Load the trained model
model = joblib.load("models/tablet_weight_model.pkl")

print("=== Tablet Weight Prediction System ===\n")

powder_density = float(input("Powder Density: "))
moisture_content = float(input("Moisture Content: "))
particle_size = float(input("Particle Size: "))
compression_force = float(input("Compression Force: "))
machine_speed = float(input("Machine Speed: "))
fill_depth = float(input("Fill Depth: "))
ambient_temperature = float(input("Ambient Temperature: "))
relative_humidity = float(input("Relative Humidity: "))

new_data = pd.DataFrame({
    "Powder_Density": [powder_density],
    "Moisture_Content": [moisture_content],
    "Particle_Size": [particle_size],
    "Compression_Force": [compression_force],
    "Machine_Speed": [machine_speed],
    "Fill_Depth": [fill_depth],
    "Ambient_Temperature": [ambient_temperature],
    "Relative_Humidity": [relative_humidity]
})

prediction = model.predict(new_data)

print("\n==============================")
print(f"Predicted Tablet Weight: {prediction[0]:.2f} mg")
print("==============================")