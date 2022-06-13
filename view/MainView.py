from view.View import View


class MainView(View):

    def open(self):
        self.window = super().initView()
        self.window.render()
        self.event_dispatcher.dispatch()
        self.window.start()
        pass
