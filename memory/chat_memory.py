class ChatMemory:
    def __init__(self):
        self.history = []

    def store(self, q, r):
        self.history.append((q, r))