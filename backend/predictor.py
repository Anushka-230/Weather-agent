import joblib
import pandas as pd

from datetime import datetime
from geopy.geocoders import Nominatim

# Load model
model = joblib.load("../model/weather_model.pkl")

geolocator = Nominatim(user_agent="weather-agent")


def predict_temperature(city, month, day):
    location = geolocator.geocode(city)

    if location is None:
        return None

    latitude = location.latitude
    longitude = location.longitude

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
