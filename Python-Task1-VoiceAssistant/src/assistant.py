from speech import SpeechRecognizer
from tts import TextToSpeech
from command_router import CommandRouter


class Assistant:

    def __init__(self):

        self.speaker = TextToSpeech()

        self.listener = SpeechRecognizer()

        self.router = CommandRouter()

    def start(self):

        self.speaker.speak(
            "Hello Anurag. I am your AI Voice Assistant."
        )

        while True:

            command = self.listener.listen()

            if not command:
                continue

            response, should_exit = self.router.process(command)

            self.speaker.speak(response)

            if should_exit:
                break