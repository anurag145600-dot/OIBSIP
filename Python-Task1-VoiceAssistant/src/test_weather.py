from weather import WeatherService

weather = WeatherService()

result = weather.get_weather("Rohtak")

print(result)