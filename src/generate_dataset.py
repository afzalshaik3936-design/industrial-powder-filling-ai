import pandas as pd
import numpy as np

# Make random values reproducible
np.random.seed(42)

rows = 10000

# Manufacturing Parameters
powder_density = np.random.normal(0.72, 0.03, rows)
moisture_content = np.random.normal(5.0, 0.8, rows)
particle_size = np.random.normal(150, 20, rows)
compression_force = np.random.normal(18, 2, rows)
machine_speed = np.random.normal(250, 20, rows)
fill_depth = np.random.normal(8.0, 0.4, rows)
ambient_temperature = np.random.normal(23, 2, rows)
relative_humidity = np.random.normal(45, 5, rows)
# create target variable 
tablet_weight = (
    500
    + (powder_density - 0.72) * 180
    + (fill_depth - 8.0) * 18
    + (compression_force - 18) * 2
    - (machine_speed - 250) * 0.08
    + np.random.normal(0, 1.5, rows)
)
df = pd.DataFrame({
    "Powder_Density": powder_density,
    "Moisture_Content": moisture_content,
    "Particle_Size": particle_size,
    "Compression_Force": compression_force,
    "Machine_Speed": machine_speed,
    "Fill_Depth": fill_depth,
    "Ambient_Temperature": ambient_temperature,
    "Relative_Humidity": relative_humidity,
    "Tablet_Weight": tablet_weight
})
df.to_csv("data/tablet_manufacturing_dataset.csv", index=False)
print(df.head())
print("\nDataset saved successfully!")