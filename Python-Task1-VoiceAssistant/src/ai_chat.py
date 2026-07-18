import os

from dotenv import load_dotenv
from google import genai


class AIChat:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("Gemini API Key not found.")

        self.client = genai.Client(api_key=api_key)

        self.model = "gemini-3.5-flash"

        self.history = []

        self.system_prompt = """
You are Anurag's AI Voice Assistant.

Rules:

- Answer naturally.
- Keep answers concise unless asked.
- Help with programming, AI, ML, Python, college studies and general knowledge.
- Speak naturally because your answers will be converted into speech.
- Never use markdown.
"""

    def ask(self, question):

        self.history.append(
            {
                "role": "user",
                "text": question
            }
        )

        conversation = self.system_prompt + "\n\n"

        for message in self.history:

            conversation += (
                f"{message['role'].capitalize()}: "
                f"{message['text']}\n"
            )
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=conversation
            )

            # response may provide text attribute or .result; handle common case
            answer = getattr(response, "text", None) or str(response)
            answer = answer.strip()

        except Exception as e:
            answer = f"Gemini Error: {e}"

        # append assistant answer to history
        self.history.append({"role": "assistant", "text": answer})

        # Keep only last 20 messages
        if len(self.history) > 20:
            self.history = self.history[-20:]

        return answer