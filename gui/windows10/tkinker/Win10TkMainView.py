from gui.windows10.tkinker.TkView import TkView

class Win10TkMainView(TkView):
    # def __init__(self, caller: MainView):
    #     self.caller = caller

    def render(self):
        tkRoot = super().getRoot()

        super().start()

