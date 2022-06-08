from tkinter import *

from config.constants import APP_TITLE


class TkView:
    def __init__(self):
        self.tkRoot = None

    def getRoot(self):
        if isinstance(self.tkRoot, Tk) is False:
            self.tkRoot = Tk()
            screenW = 1920
            screenH = 1280
            self.tkRoot.title(APP_TITLE)
            # tkRoot.geometry('780x395+' + str(screenW - 780) + '+' + str(screenH - 695))
            #self.tkRoot.geometry('780x445+' + str(screenW - 2000) + '+' + str(screenH - 1400))
            self.tkRoot.geometry('{0}x{1}+290+100'.format(screenW, screenH))

        return self.tkRoot

    def start(self):
        self.tkRoot.mainloop()