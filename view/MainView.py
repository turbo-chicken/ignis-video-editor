from view.View import View
from eventHandler.event.ViewEvent import ViewEvent


class MainView(View):
    def open(self):
        self.window = super().initView()
        self.window.render()

        self.event_dispatcher.dispatch(
            ViewEvent(
                ViewEvent.INITIAL_RENDER_COMPLETE,
                {}
            )
        )

        self.window.start()
        pass

    def renderWidgets(self):
        self.window.initVideoControlsWidget()
        video = self.env.getCurrentVideo()
        self.window.initVideoPreviewWidget(self.env.getImg(video))

    def displayVideoFrame(self, i):
        self.window.refreshVideoPreviewWidget(self.env.getNextImg(i))

    def onVideoPlayButtonPress(self):
        self.event_dispatcher.dispatch(
            ViewEvent(
                ViewEvent.MAIN_VIEW_PLAY_VIDEO,
                {}
            )
        )

    #def showVideoControls(self):
        # self.window.initVideoControlsWidget(self.env.getImg())

