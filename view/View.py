from env import Env
from eventHandler.EventDispatcher import EventDispatcher
from gui.GuiFactory import GuiFactory

class View:
    def __init__(self, event_dispatcher: EventDispatcher, env: Env):
        print('Ii ii')
        self.gui = GuiFactory()
        self.event_dispatcher = event_dispatcher
        self.env = env

    def initView(self):
        return self.gui.initGuiView(self)
