import requests
import os

def get_weather(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

lat = os.environ.get("LAT")
lon = os.environ.get("LONG")

api_key = os.environ.get("API_KEY")

weather_data = get_weather(lat, lon, api_key)

print(weather_data)


temperature = weather_data["main"]["temp"]
endroit = weather_data["name"]
meteo = weather_data["weather"][0]["description"]

print(f"La température actuelle est de {temperature} degrés Celsius à {endroit}.")
print(f"Le temps est {meteo}.")