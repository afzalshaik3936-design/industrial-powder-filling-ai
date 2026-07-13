import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
df = pd.read_csv("data/tablet_manufacturing_dataset.csv")
X = df.drop("Tablet_Weight", axis=1)
y = df["Tablet_Weight"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = LinearRegression()

model.fit(X_train, y_train)
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

mse = mean_squared_error(y_test, predictions)

r2 = r2_score(y_test, predictions)
print("Model Performance")

print("-------------------")

print(f"MAE : {mae:.2f}")

print(f"MSE : {mse:.2f}")

print(f"R² Score : {r2:.3f}")