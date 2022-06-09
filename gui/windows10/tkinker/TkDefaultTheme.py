from tkinter.ttk import Style


class TkDefaultTheme:
    LEFT_PANEL = 'LeftSide.TFrame'
    TOP_PANEL = 'Top.TFrame'
    BOTTOM_PANEL = 'Bottom.TFrame'

    def configure(self):
        self.leftPanelStyle = Style()
        self.leftPanelStyle.configure(self.LEFT_PANEL, background='#00A0B0')

        self.topPanelStyle = Style()
        self.topPanelStyle.configure(self.TOP_PANEL, background='#EDC951')

        self.bottomPanelStyle = Style()
        self.bottomPanelStyle.configure(self.BOTTOM_PANEL, background='#EB6841')

    def leftPanelStyleName(self):
        return self.LEFT_PANEL

    def topPanelStyleName(self):
        return self.TOP_PANEL

    def bottomPanelStyleName(self):
        return self.BOTTOM_PANEL