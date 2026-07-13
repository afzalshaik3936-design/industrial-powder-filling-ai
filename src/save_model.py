import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("data/tablet_manufacturing_dataset.csv")

# Features and target
X = df.drop("Tablet_Weight", axis=1)
y = df["Tablet_Weight"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/tablet_weight_model.pkl")

print("Model saved successfully!")