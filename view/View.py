from eventHandler.EventDispatcher import EventDispatcher
from gui.GuiFactory import GuiFactory

class View:
    def __init__(self, event_dispatcher: EventDispatcher):
        self.gui = GuiFactory()
        self.event_dispatcher = event_dispatcher

    def initView(self):
        return self.gui.initGuiView(self)
