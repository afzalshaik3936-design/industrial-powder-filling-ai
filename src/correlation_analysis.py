import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/tablet_manufacturing_dataset.csv")
# Correlation matrix
correlation = df.corr()

print(correlation)

plt.figure(figsize=(8,6))

plt.imshow(correlation, cmap="coolwarm")

plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)

plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.show()