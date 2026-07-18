from urllib import response
from ai_chat import AIChat

from utils import current_time, current_date
from search import SearchService
from config_loader import CONFIG
from weather import WeatherService
from reminder_manager import ReminderManager
import re

class CommandRouter:

    def __init__(self):
        self.weather_service = WeatherService()
        self.reminder_manager = ReminderManager()
        self.ai = AIChat()
    def process(self, command: str):

        cmd = command.lower().strip()
        words = cmd.split()

        # --------------------------
        # Greeting
        # --------------------------

        if any(word in words for word in CONFIG["greetings"]):

            return (
                "Hello Anurag. Nice to meet you.",
                False
            )

        # --------------------------
        # Time
        # --------------------------

        elif "time" in cmd:

            return (
                f"The current time is {current_time()}",
                False
            )

        # --------------------------
        # Date
        # --------------------------

        elif (
            "date" in cmd
            or "day" in cmd
            or "today" in cmd
        ):

            return (
                f"Today is {current_date()}",
                False
            )

        # --------------------------
        # Open Website
        # --------------------------

        elif cmd.startswith("open"):

            if len(words) < 2:

                return (
                    "Please tell me which website to open.",
                    False
                )

            site = " ".join(words[1:])

            websites = CONFIG["websites"]

            if site in websites:

                SearchService.open_website(
                    websites[site]
                )

                display_name = {

                    "google": "Google",

                    "youtube": "YouTube",

                    "github": "GitHub",

                    "chatgpt": "ChatGPT",

                    "chat gpt": "ChatGPT",

                    "chat gt": "ChatGPT"

                }

                return (

                    f"Opening {display_name.get(site, site.title())}.",

                    False

                )

            return (

                f"I don't know how to open {site}.",

                False

            )

        # --------------------------
        # Weather
        # --------------------------

        elif "weather" in cmd or "temperature" in cmd:

            if " in " in cmd:

                city = cmd.split(
                    " in ",
                    1
                )[1].strip()

            else:

                city = self.weather_service.get_current_city()

            result = self.weather_service.get_weather(city)

            if result is None:

                return (

                    f"Sorry, I could not find weather information for {city}.",

                    False

                )

            response = (

                f"The current weather in {result['city']} is "
                f"{result['description']}. "
                f"The temperature is "
                f"{result['temperature']} degree Celsius. "
                f"It feels like "
                f"{result['feels_like']} degree Celsius. "
                f"Humidity is "
                f"{result['humidity']} percent. "
                f"Wind speed is "
                f"{result['wind']} meters per second. "
                f"Visibility is "
                f"{result['visibility']} kilometers. "
                f"Sunrise is at "
                f"{result['sunrise']}. "
                f"Sunset is at "
                f"{result['sunset']}."

            )

            return (

                response,

                False

            )

        # --------------------------
        # Google Search
        # --------------------------

        elif cmd.startswith("search"):

            query = cmd.replace(
                "search",
                "",
                1
            ).strip()

            if not query:

                return (

                    "Please tell me what you want to search.",

                    False

                )

            SearchService.google_search(query)

            return (

                f"Searching Google for {query}.",

                False

            )

        # --------------------------
        # YouTube Search
        # --------------------------

        elif cmd.startswith("youtube search"):

            query = cmd.replace(
                "youtube search",
                "",
                1
            ).strip()

            if not query:

                return (

                    "Please tell me what you want to search on YouTube.",

                    False

                )

            SearchService.youtube_search(query)

            return (

                f"Searching YouTube for {query}.",

                False

            )

        # -------------------------
        # Reminder
        # -------------------------

        elif "remind" in cmd:

            # Pattern 1:
            # remind me in 10 seconds to drink water
            match = re.search(
                r"remind me in (\d+) (second|seconds|minute|minutes|hour|hours) to (.+)",
                cmd,
            )

            if match:

                amount = int(match.group(1))
                unit = match.group(2)
                message = match.group(3)

                if "second" in unit:
                    seconds = amount
                elif "minute" in unit:
                    seconds = amount * 60
                else:
                    seconds = amount * 3600

                self.reminder_manager.add_reminder(seconds, message)

                return (
                    f"Okay. I will remind you in {amount} {unit} to {message}.",
                    False,
                )

            # Pattern 2:
            # remind me to drink water in 10 seconds
            match = re.search(
                r"remind me to (.+) in (\d+) (second|seconds|minute|minutes|hour|hours)",
                cmd,
            )

            if match:

                message = match.group(1)
                amount = int(match.group(2))
                unit = match.group(3)

                if "second" in unit:
                    seconds = amount
                elif "minute" in unit:
                    seconds = amount * 60
                else:
                    seconds = amount * 3600

                self.reminder_manager.add_reminder(seconds, message)

                return (
                    f"Okay. I will remind you in {amount} {unit} to {message}.",
                    False,
                )

            # Pattern 3:
            # remind me to dance
            match = re.search(
                r"remind me to (.+)",
                cmd,
            )

            if match:

                return (
                    "When should I remind you?",
                    False,
                )

            # Pattern 4:
            # remind me in 10 minutes
            match = re.search(
                r"remind me in (\d+) (second|seconds|minute|minutes|hour|hours)",
                cmd,
            )

            if match:

                return (
                    "What should I remind you about?",
                    False,
                )

            return (
                "Please say something like 'Remind me in 10 minutes to drink water.'",
                False,
            )
        # --------------------------
        # Exit
        # --------------------------

        elif any(word in words for word in CONFIG["exit"]):

            return (
                "Goodbye Anurag. Have a wonderful day.",
                True
            )

        # --------------------------
        # Unknown Command
        # --------------------------

        else:

            response = self.ai.ask(command)

        return (
    response,
    False
)