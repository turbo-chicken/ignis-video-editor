from gui.GuiFactory import GuiFactory

class View:
    def __init__(self):
        self.gui = GuiFactory()

    def initView(self):
        return self.gui.initGuiView(self)