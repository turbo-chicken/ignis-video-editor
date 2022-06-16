from view.MainView import MainView


class AppRuntime:
    def __init__(self, main_view: MainView):
        self.main_view = main_view
        pass
    #
    # def configureListeners(self):
    #     self.eventHandler.addListener()
    #
    #
    # def dispatch(self, event):
    #     print('Dispatched ', event)
    #     pass
    #
    # def addListener(self, listener):
    #     print('Adding listener ', listener)
    #     pass
    #
    def startMainView(self):
        self.main_view.open()
