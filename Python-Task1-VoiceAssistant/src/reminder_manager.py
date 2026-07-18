import threading
import time

from reminder import Reminder
from tts import TextToSpeech
from notification import NotificationService


class ReminderManager:

    def __init__(self):

        self.speaker = TextToSpeech()

        self.notification = NotificationService()

        self.active_reminders = []

    def add_reminder(self, seconds, message):

        reminder = Reminder(
            message=message,
            delay=seconds
        )

        self.active_reminders.append(reminder)

        thread = threading.Thread(
            target=self._run_reminder,
            args=(reminder,),
            daemon=True
        )

        thread.start()

        return True

    def _run_reminder(self, reminder):

        time.sleep(reminder.delay)

        if self.speaker.is_shutdown:
            return

        reminder_text = f"Reminder. {reminder.message}"

        print("\n" + "=" * 40)
        print(reminder_text)
        print("=" * 40)

        self.notification.show(
            "AI Voice Assistant",
            reminder.message
        )

        self.speaker.speak(reminder_text)

        if reminder in self.active_reminders:
            self.active_reminders.remove(reminder)

    def get_active_reminders(self):

        return self.active_reminders