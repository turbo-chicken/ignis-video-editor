from eventHandler.EventHandler import EventHandler

class EventDispatcher:
    def __init__(self, event_handler: EventHandler):
        self.event_handler = event_handler

    def dispatch(self, event):
        print(event)
        self.event_handler.handle(event)