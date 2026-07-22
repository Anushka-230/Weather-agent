import joblib
import pandas as pd
from datetime import datetime

# Load model
model = joblib.load("../model/weather_model.pkl")

# Coordinates of supported cities
CITY_COORDS = {
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Bangalore": (12.9716, 77.5946),
    "Bhubaneswar": (20.2961, 85.8245),
    "Kolkata": (22.5726, 88.3639),
    "Puri": (19.8135, 85.8312),
}


def predict_temperature(city, month, day):
    # Get coordinates from dictionary
    coords = CITY_COORDS.get(city.title())

    if coords is None:
        return None

    latitude, longitude = coords

    day_of_year = datetime(2025, month, day).timetuple().tm_yday

    features = pd.DataFrame(
        [[latitude, longitude, month, day, day_of_year]],
        columns=[
            "latitude",
            "longitude",
            "month",
            "day",
            "day_of_year",
        ],
    )

    prediction = model.predict(features)[0]

    return round(float(prediction), 2)