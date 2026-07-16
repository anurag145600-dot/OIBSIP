import asyncio
import edge_tts
import pygame
import os
import tempfile


class TextToSpeech:

    def __init__(self):

        pygame.mixer.init()

        self.voice = "en-US-AriaNeural"

    async def _generate(self, text, filename):

        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice
        )

        await communicate.save(filename)

    def speak(self, text):

        print(f"Assistant: {text}")

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        )

        temp_file.close()

        asyncio.run(
            self._generate(
                text,
                temp_file.name
            )
        )

        pygame.mixer.music.load(temp_file.name)

        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():

            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()

        os.remove(temp_file.name)