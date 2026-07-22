from fastapi import FastAPI
from predictor import predict_temperature
from llm import extract_weather_query, generate_weather_response
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="Weather Prediction API",
    description="Predict future temperature using historical weather data",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://weather-agent-68sn.onrender.com"],  # Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {"message": "Weather Prediction API is running!"}


@app.get("/predict")
def predict(city: str, month: int, day: int):
    temp = predict_temperature(city, month, day)

    if temp is None:
        return {"error": "City not found"}

    return {
        "city": city,
        "month": month,
        "day": day,
        "predicted_temperature": temp,
    }


@app.get("/chat")
def chat(query: str):

    try:
        # Extract information from the user's question
        data = extract_weather_query(query)

        # Predict temperature
        temp = predict_temperature(
            data["city"],
            data["month"],
            data["day"],
        )

        if temp is None:
            return {
                "success": False,
                "error": f"Sorry, I couldn't find the city '{data['city']}'."
            }

        # Generate natural language response
        answer = generate_weather_response(
            data["city"],
            data["year"],
            data["month"],
            data["day"],
            temp
        )

        return {
            "success": True,
            "question": query,
            "answer": answer,
            "prediction": {
                "city": data["city"],
                "date": f"{data['year']}-{data['month']:02d}-{data['day']:02d}",
                "temperature": round(temp, 2)
            }
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }