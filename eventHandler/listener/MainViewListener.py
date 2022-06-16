import threading
from time import sleep

from eventHandler.event.ViewEvent import ViewEvent
from view.MainView import MainView


class MainViewListener:
    def __init__(self, main_view: MainView):
        self.main_view = main_view
        pass

    def supports(self, event):
        if isinstance(event, ViewEvent):
            return True

        return False

    def handle(self, event):
        if event.getType() == ViewEvent.INITIAL_RENDER_COMPLETE:
            return self.onRenderComplete()
        if event.getType() == ViewEvent.MAIN_VIEW_PLAY_VIDEO:
            pThread = threading.Thread(target=self.onMainViewPlayVideo, args=[])
            pThread.start()
            return

    def onRenderComplete(self):
        print('on render complete')
        self.main_view.renderWidgets()
        pass

    def onMainViewPlayVideo(self):
        for i in range(2,4):
            self.main_view.displayVideoFrame(i)
            sleep(0.2)