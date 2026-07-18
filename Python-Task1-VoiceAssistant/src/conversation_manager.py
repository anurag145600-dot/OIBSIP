class ConversationManager:

    def __init__(self):

        self.clear()

    def clear(self):

        self.pending_intent = None
        self.pending_data = {}

    def start(self, intent, **data):

        self.pending_intent = intent
        self.pending_data = data

    def has_pending(self):

        return self.pending_intent is not None

    def get_intent(self):

        return self.pending_intent

    def get_data(self):

        return self.pending_data