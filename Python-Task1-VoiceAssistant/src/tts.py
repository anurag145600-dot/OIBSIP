import asyncio
import os
import tempfile
import threading

import edge_tts
import pygame


class TextToSpeech:

    _instance = None
    _instance_lock = threading.Lock()

    def __new__(cls):

        with cls._instance_lock:

            if cls._instance is None:

                cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):

        if getattr(self, "_initialized", False):
            return

        pygame.mixer.init()

        self.voice = "en-US-GuyNeural"
        self.rate = "+0%"
        self.volume = "+0%"

        self.is_speaking = False
        self.is_shutdown = False

        self._speech_lock = threading.Lock()

        self._initialized = True

    async def _save_audio(self, text, filename):

        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice,
            rate=self.rate,
            volume=self.volume
        )

        await communicate.save(filename)

    def speak(self, text):

        if self.is_shutdown:
            return

        if not text:
            return

        with self._speech_lock:

            self.is_speaking = True

            fd, filename = tempfile.mkstemp(suffix=".mp3")
            os.close(fd)

            try:

                asyncio.run(self._save_audio(text, filename))

                pygame.mixer.music.load(filename)

                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():

                    pygame.time.wait(100)

            except Exception as e:

                print(f"TTS Error: {e}")

            finally:

                pygame.mixer.music.stop()

                try:
                    if os.path.exists(filename):
                        os.remove(filename)
                except Exception:
                    pass

                self.is_speaking = False

    def shutdown(self):

        self.is_shutdown = True