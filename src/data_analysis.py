import pandas as pd

# Load dataset
df = pd.read_csv("data/tablet_manufacturing_dataset.csv")

# Show first 5 rows
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())