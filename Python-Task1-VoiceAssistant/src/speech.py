import time
import speech_recognition as sr  # type: ignore
from tts import TextToSpeech


class SpeechRecognizer:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.recognizer.pause_threshold = 0.8
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True

        self.speaker = TextToSpeech()

    def listen(self):

        # Wait while assistant is speaking
        while self.speaker.is_speaking:
            time.sleep(0.1)

        with sr.Microphone() as source:

            print("\nListening...")

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            try:

                audio = self.recognizer.listen(
                    source,
                    timeout=1,
                    phrase_time_limit=6
                )

            except sr.WaitTimeoutError:
                # Nobody spoke within 1 second
                return ""

        # Assistant started speaking while we were recording
        if self.speaker.is_speaking:
            return ""

        try:

            command = self.recognizer.recognize_google(audio)

            command = command.lower().strip()

            print(f"\nYou : {command}")

            return command

        except sr.UnknownValueError:

            return ""

        except sr.RequestError:

            print("Speech Recognition Service unavailable.")

            return ""