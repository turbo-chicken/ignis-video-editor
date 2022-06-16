class Event:
    def __init__(self, type: str, details):
        if details is None:
            details = {}
        self.details = details
        self.type = type

    def getType(self):
        return self.type