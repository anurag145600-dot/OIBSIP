import os
import requests

from dotenv import load_dotenv

load_dotenv()


class WeatherService:

    def __init__(self):

        self.api_key = os.getenv("OPENWEATHER_API_KEY")

        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

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

                "temperature": data["main"]["temp"],

                "humidity": data["main"]["humidity"],

                "description": data["weather"][0]["description"],

                "wind": data["wind"]["speed"]

            }

            return weather

        except Exception:

            return None