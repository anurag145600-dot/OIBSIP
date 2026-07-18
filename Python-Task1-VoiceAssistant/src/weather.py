import os
import requests
import geocoder
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class WeatherService:

    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_current_city(self):
        try:
            g = geocoder.ip("me")
            if g.city:
                return g.city
        except Exception:
            pass

        return "Delhi"

    def get_weather(self, city):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(
                self.base_url,
                params=params,
                timeout=10
            )

            data = response.json()

            if response.status_code != 200:
                return None

            weather = {
                "city": data["name"],
                "temperature": round(data["main"]["temp"], 1),
                "feels_like": round(data["main"]["feels_like"], 1),
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
                "wind": round(data["wind"]["speed"], 1),
                "visibility": round(data.get("visibility", 0) / 1000, 1),
                "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%I:%M %p"),
                "sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%I:%M %p")
            }

            return weather
        except Exception:
            return None