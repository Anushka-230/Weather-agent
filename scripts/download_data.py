import requests
import pandas as pd
import os
from datetime import date

cities = {
    "Bangalore": (12.9716, 77.5946),
    "Bhubaneswar": (20.2961, 85.8245),
    "Delhi": (28.6139, 77.2090),
    "Kolkata": (22.5726, 88.3639),
    "Mumbai": (19.0760, 72.8777)
}

START_DATE = "2020-01-01"
END_DATE = date.today().strftime("%Y-%m-%d")

os.makedirs("../data", exist_ok=True)

for city, (lat, lon) in cities.items():

    print(f"\nDownloading {city}...")

    url = (
        "https://archive-api.open-meteo.com/v1/archive"
        f"?latitude={lat}"
        f"&longitude={lon}"
        f"&start_date={START_DATE}"
        f"&end_date={END_DATE}"
        "&daily=temperature_2m_mean,"
        "temperature_2m_max,"
        "temperature_2m_min,"
        "precipitation_sum,"
        "wind_speed_10m_max"
        "&timezone=auto"
    )

    response = requests.get(url)

    if response.status_code != 200:
        print(response.text)
        continue

    data = response.json()

    df = pd.DataFrame(data["daily"])

    df["city"] = city
    df["latitude"] = lat
    df["longitude"] = lon

    df.to_csv(f"../data/{city}.csv", index=False)

    print(f"Saved {city}.csv ({len(df)} rows)")

print("\nFinished downloading all cities!")