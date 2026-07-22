import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# --------------------
# Load Data
# --------------------

df = pd.read_csv("../data/merged_weather.csv")

# --------------------
# Features
# --------------------

features = [
    "latitude",
    "longitude",
    "month",
    "day",
    "day_of_year"
]

# --------------------
# Train/Test Split by Year
# --------------------

train_df = df[(df["year"] >= 2020) & (df["year"] <= 2025)]
test_df = df[df["year"] == 2026]

X_train = train_df[features]
y_train = train_df["temperature"]

X_test = test_df[features]
y_test = test_df["temperature"]
# --------------------
# Model
# --------------------

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

print("Training model...")

model.fit(X_train, y_train)

print("Training complete!")

# --------------------
# Evaluation
# --------------------

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = mse ** 0.5
r2 = r2_score(y_test, predictions)

print("\nModel Performance")
print("------------------------")
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

# --------------------
# Save Model
# --------------------

os.makedirs("../model", exist_ok=True)

joblib.dump(model, "../model/weather_model.pkl")

print("\nModel saved successfully!")