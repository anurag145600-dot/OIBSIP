from utils import current_time, current_date
from search import SearchService


class CommandRouter:

    def process(self, command: str):

        cmd = command.lower().strip()

        words = cmd.split()

        # --------------------------
        # Greetings
        # --------------------------

        if any(word in words for word in ["hello", "hi", "hey"]):

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

        elif "date" in cmd:

            return (
                f"Today is {current_date()}",
                False
            )

        # --------------------------
        # Open Websites
        # --------------------------

        elif "open google" in cmd:

            SearchService.open_google()

            return (
                "Opening Google.",
                False
            )

        elif "open youtube" in cmd:

            SearchService.open_youtube()

            return (
                "Opening YouTube.",
                False
            )

        elif "open github" in cmd:

            SearchService.open_github()

            return (
                "Opening GitHub.",
                False
            )

        elif (
            "open chatgpt" in cmd
            or "open chat gpt" in cmd
            or "open chat gt" in cmd
        ):

            SearchService.open_chatgpt()

            return (
                "Opening ChatGPT.",
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
                f"Searching Google for {query}",
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
                f"Searching YouTube for {query}",
                False
            )

        # --------------------------
        # Exit
        # --------------------------

        elif any(word in words for word in ["exit", "quit", "stop"]):

            return (
                "Goodbye Anurag. Have a wonderful day.",
                True
            )

        # --------------------------
        # Unknown Command
        # --------------------------

        else:

            return (
                "Sorry. I do not know this command yet.",
                False
            )