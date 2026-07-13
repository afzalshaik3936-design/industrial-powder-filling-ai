import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/tablet_manufacturing_dataset.csv")
plt.figure(figsize=(8,5))
plt.hist(df["Tablet_Weight"], bins=30)
plt.title("Distribution of Tablet Weight")
plt.xlabel("Tablet Weight (mg)")
plt.ylabel("Frequency")
plt.show()
