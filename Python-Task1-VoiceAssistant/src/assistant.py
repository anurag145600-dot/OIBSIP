import time
import re

from speech import SpeechRecognizer
from tts import TextToSpeech
from command_router import CommandRouter
from intent_parser import IntentParser
from conversation_manager import ConversationManager


class Assistant:

    def __init__(self):

        self.speaker = TextToSpeech()

        self.listener = SpeechRecognizer()

        self.router = CommandRouter()

        self.intent_parser = IntentParser()

        self.conversation = ConversationManager()

    def start(self):

        greeting = "Hello Anurag. I am your AI Voice Assistant."

        print(f"Assistant: {greeting}")
        self.speaker.speak(greeting)

        try:

            while True:

                while self.speaker.is_speaking:
                    time.sleep(0.1)

                command = self.listener.listen()

                if not command:
                    continue

                command = self.intent_parser.normalize(command)

                # --------------------------------------------------
                # Continue an unfinished conversation
                # --------------------------------------------------

                if self.conversation.has_pending():

                    intent = self.conversation.get_intent()
                    data = self.conversation.get_data()

                    if intent == "reminder_time":

                        message = data["message"]

                        command = f"remind me to {message} in {command}"

                        self.conversation.clear()

                # --------------------------------------------------
                # Process command
                # --------------------------------------------------

                response, should_exit = self.router.process(command)

                # --------------------------------------------------
                # Start a conversation if needed
                # --------------------------------------------------

                match = re.fullmatch(
                    r"remind me to (.+)",
                    command
                )

                if match and response == "When should I remind you?":

                    reminder_message = match.group(1).strip()

                    self.conversation.start(
                        "reminder_time",
                        message=reminder_message
                    )

                if response:

                    print(f"Assistant: {response}")

                    self.speaker.speak(response)

                if should_exit:

                    break

        finally:

            self.speaker.shutdown()