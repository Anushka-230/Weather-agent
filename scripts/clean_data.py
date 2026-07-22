import os
import pandas as pd

DATA_FOLDER = "../data"

files = [
    "Bangalore.csv",
    "Bhubaneswar.csv",
    "Delhi.csv",
    "Kolkata.csv",
    "Mumbai.csv"
]

dfs = []

for file in files:

    path = os.path.join(DATA_FOLDER, file)

    df = pd.read_csv(path)

    dfs.append(df)

merged = pd.concat(dfs, ignore_index=True)

print("Rows before cleaning:", len(merged))

# Remove duplicates
merged.drop_duplicates(inplace=True)

# Keep only the columns we need
columns = [
    "time",
    "city",
    "latitude",
    "longitude",
    "temperature_2m_mean",
    "temperature_2m_max",
    "temperature_2m_min",
    "precipitation_sum",
    "wind_speed_10m_max"
]

merged = merged[columns]

# Rename columns
merged.rename(columns={
    "time": "date",
    "temperature_2m_mean": "temperature",
    "temperature_2m_max": "temp_max",
    "temperature_2m_min": "temp_min",
    "precipitation_sum": "precipitation",
    "wind_speed_10m_max": "wind_speed"
}, inplace=True)

# Convert date
merged["date"] = pd.to_datetime(merged["date"])

# Feature Engineering
merged["year"] = merged["date"].dt.year
merged["month"] = merged["date"].dt.month
merged["day"] = merged["date"].dt.day
merged["day_of_year"] = merged["date"].dt.dayofyear

# Remove rows with missing target
merged.dropna(subset=["temperature"], inplace=True)

# Fill missing values
numeric_cols = merged.select_dtypes(include="number").columns
merged[numeric_cols] = merged[numeric_cols].fillna(
    merged[numeric_cols].median()
)

output = "../data/merged_weather.csv"

merged.to_csv(output, index=False)

print("Rows after cleaning:", len(merged))
print("Saved to:", output)
print("\nColumns:")
print(merged.columns.tolist())
print("\nFirst five rows:")
print(merged.head())