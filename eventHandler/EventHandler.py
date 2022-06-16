class EventHandler:
    def __init__(self, listeners):
        self.listeners = listeners

    def handle(self, event):
        for listener in self.listeners:
            if listener.supports(event):
                return listener.handle(event)

