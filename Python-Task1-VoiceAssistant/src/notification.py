from plyer import notification


class NotificationService:

    def show(self, title, message):

        notification.notify(
            title=title,
            message=message,
            app_name="AI Voice Assistant",
            timeout=5
        )