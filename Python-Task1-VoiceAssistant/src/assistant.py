from speech import SpeechRecognizer
from tts import TextToSpeech
from command_router import CommandRouter
from intent_parser import IntentParser


class Assistant:

    def __init__(self):

        self.speaker = TextToSpeech()

        self.listener = SpeechRecognizer()

        self.router = CommandRouter()

        self.intent_parser = IntentParser()

    def start(self):

        self.speaker.speak(
            "Hello Anurag. I am your AI Voice Assistant."
        )

        while True:

            # Listen to user
            command = self.listener.listen()

            # If speech was not recognized
            if not command:
                continue

            # Normalize command
            command = self.intent_parser.normalize(command)

            # Process command
            response, should_exit = self.router.process(command)

            # Speak response
            self.speaker.speak(response)

            # Exit if requested
            if should_exit:
                break