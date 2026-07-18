class IntentParser:

    def normalize(self, command: str):

        # -------------------------
        # Safety Check
        # -------------------------

        if not command:
            return ""

        cmd = command.lower().strip()
        words = cmd.split()

        # -------------------------
        # Greetings
        # -------------------------

        greetings = [
            "hello",
            "hi",
            "hey"
        ]

        # Match complete words only
        if any(word in words for word in greetings):
            return "hello"

        # -------------------------
        # Exit
        # -------------------------

        exits = [
            "exit",
            "quit",
            "bye",
            "goodbye",
            "stop"
        ]

        if any(word in words for word in exits):
            return "exit"

        # -------------------------
        # Open Websites
        # -------------------------

        websites = {
            "google": "google",
            "youtube": "youtube",
            "github": "github",
            "chatgpt": "chatgpt",
            "chat gpt": "chatgpt",
            "chat gt": "chatgpt"
        }

        for site in websites:

            if site in cmd:

                if any(action in words for action in ["open", "launch", "start"]):

                    return f"open {websites[site]}"

        # -------------------------
        # Weather
        # -------------------------

        weather_words = [

            "weather",
            "whether",
            "temperature",
            "outside",
            "climate"

        ]

        if any(word in words for word in weather_words):

            return cmd

        # -------------------------
        # YouTube Search
        # -------------------------

        youtube_prefixes = [

            "find on youtube ",
            "search youtube ",
            "youtube search ",
            "play "

        ]

        for prefix in youtube_prefixes:

            if cmd.startswith(prefix):

                query = cmd[len(prefix):].strip()

                if not query:
                    return "youtube search"

                return f"youtube search {query}"

        # -------------------------
        # Google Search
        # -------------------------

        search_prefixes = [

            "search ",
            "find ",
            "google ",
            "look up "

        ]

        useless = [

            "information",
            "information about",
            "about"

        ]

        for prefix in search_prefixes:

            if cmd.startswith(prefix):

                query = cmd[len(prefix):].strip()

                if not query:
                    return "search"

                if query in useless:
                    return "search"

                return f"search {query}"

        # -------------------------
        # Default
        # -------------------------

        return cmd