import requests
import os
from fastapi import FastAPI


app = FastAPI()
api_key = os.environ.get("API_KEY")

@app.get("/")
def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data