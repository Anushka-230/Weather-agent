# 🌤 Weather Prediction Agent

An AI-powered Weather Prediction Agent that predicts future temperatures using a Machine Learning model trained on historical weather data. The application accepts natural language queries, extracts the required information using an LLM, predicts the temperature using a Random Forest Regression model, and generates a human-friendly response.

---

## 📌 Features

- 🤖 Natural language weather queries
- 🌍 Supports multiple cities
- 📅 Predicts future temperatures for any given date
- 🧠 Machine Learning based prediction
- 💬 AI-generated conversational responses
- 🚀 REST API built with FastAPI
- 🌐 Interactive frontend using HTML, CSS and JavaScript

---

## 🏗️ Architecture

```
User
   │
   ▼
Frontend (HTML/CSS/JS)
   │
   ▼
FastAPI Backend
   │
   ├── LLM (OpenRouter)
   │       │
   │       ▼
   │  Extract City & Date
   │
   └── Random Forest Model
           │
           ▼
     Temperature Prediction
           │
           ▼
LLM generates a natural response
           │
           ▼
Frontend displays prediction
```

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI

### Machine Learning
- Scikit-learn
- Random Forest Regressor
- Pandas
- NumPy

### AI
- OpenRouter API
- LLM for natural language understanding

### Data
- Open-Meteo Historical Weather API

### Frontend
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```
Weather-agent/
│
├── backend/
│   ├── app.py
│   ├── predictor.py
│   ├── llm.py
│   └── model/
│
├── data/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── scripts/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Anushka-230/Weather-agent.git

cd Weather-agent
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
OPENROUTER_API_KEY=your_api_key
```

### Start the backend

```bash
cd backend

uvicorn app:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

## 🚀 Example Queries

```
What will be the temperature in Puri on 15 July 2027?
```

```
What will be the temperature in Mumbai on Christmas 2027?
```

```
What will be the temperature in Delhi on 1 January 2028?
```

---

## 📖 API Endpoints

### Home

```
GET /
```

Returns API status.

---

### Predict Temperature

```
GET /predict
```

Example:

```
/predict?city=Puri&month=7&day=15
```

---

### Chat Endpoint

```
GET /chat
```

Example:

```
/chat?query=What will be the temperature in Mumbai on Christmas 2027?
```

Sample Response

```json
{
    "success": true,
    "question": "What will be the temperature in Mumbai on Christmas 2027?",
    "answer": "The predicted temperature in Mumbai on December 25, 2027 is approximately 23.17°C. The weather is expected to be pleasant and comfortable. A light outfit should be suitable if you're planning to spend time outdoors.",
    "prediction": {
        "city": "Mumbai",
        "date": "2027-12-25",
        "temperature": 23.17
    }
}
```

---

## 📊 Machine Learning Model

- Algorithm: Random Forest Regression
- Training Data: Historical weather data from Open-Meteo
- Features:
  - Latitude
  - Longitude
  - Month
  - Day
  - Day of Year
- Target:
  - Daily Average Temperature

---

## 🔮 Future Improvements

- Weather condition prediction (Sunny, Rainy, Cloudy)
- Humidity prediction
- Wind speed prediction
- Rainfall forecasting
- Interactive charts
- Multi-language support
- Docker deployment

---

## 👩‍💻 Author

**Anushka Das**

B.Tech Computer Science Engineering  
KIIT University

GitHub: https://github.com/Anushka-230
