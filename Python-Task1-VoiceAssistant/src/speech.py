import speech_recognition as sr


class SpeechRecognizer:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):

        with sr.Microphone() as source:

            print("\nListening...")

            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = self.recognizer.listen(source)

        try:

            command = self.recognizer.recognize_google(audio)

            command = command.lower()

            print(f"\nYou : {command}")

            return command

        except sr.UnknownValueError:

            print("Sorry, I could not understand.")

            return ""

        except sr.RequestError:

            print("Speech Recognition Service unavailable.")

            return ""