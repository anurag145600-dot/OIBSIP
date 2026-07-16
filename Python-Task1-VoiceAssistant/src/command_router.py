from utils import current_time, current_date


class CommandRouter:

    def process(self, command: str):

        if any(word in command for word in ["hello", "hi", "hey"]):

            return (
                "Hello Anurag. Nice to meet you.",
                False
            )

        elif "time" in command:

            return (
                f"The current time is {current_time()}",
                False
            )

        elif "date" in command:

            return (
                f"Today is {current_date()}",
                False
            )

        elif any(word in command for word in ["exit", "quit", "stop"]):

            return (
                "Goodbye Anurag. Have a wonderful day.",
                True
            )

        else:

            return (
                "Sorry. I do not know this command yet.",
                False
            )