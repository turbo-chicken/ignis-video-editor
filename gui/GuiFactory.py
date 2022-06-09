import view.MainView
from gui.windows10.tkinker.TkDefaultTheme import TkDefaultTheme
from gui.windows10.tkinker.Win10TkMainView import Win10TkMainView

class GuiFactory:
    def initGuiView(self, caller):
        if isinstance(caller, view.MainView.MainView):
            return Win10TkMainView(caller, TkDefaultTheme())
        else:
            print('bope')
