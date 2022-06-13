from PIL import ImageTk, Image
from tkinter import *
from tkinter.ttk import Frame, Label, Style
import tkinter as tk

from PIL.ImageTk import PhotoImage

from gui.windows10.tkinker.TkView import TkView


class Win10TkMainView(TkView):
    def __init__(self, caller, theme):
        self.caller = caller
        self.theme = theme
        super().__init__()

        self.frames = {}
        self.ref = {}

    def render(self):
        super().initRoot()
        self.theme.configure()
        self.configureFrames()

        self.initVideoPreviewWidget()

        # super().start()

    def start(self):
        super().start()



    def configureFrames(self):
        self.frames['left'] = Frame(super().getRoot(), width=300, style=self.theme.leftPanelStyleName())
        self.frames['left'].pack(side=LEFT, expand=False, fill=BOTH)

        self.frames['video'] = Frame(super().getRoot(), width=1200, height=600, style=self.theme.topPanelStyleName())
        self.frames['video'].pack(side=TOP, expand=False, fill=BOTH)

        self.frames['controls'] = Frame(super().getRoot(), width=1200, height=600, style=self.theme.bottomPanelStyleName())
        self.frames['controls'].pack(side=BOTTOM, expand=False, fill=BOTH)

        return True

    def initVideoPreviewWidget(self):
        self.ref['preview-a'] = tk.Canvas(self.frames['video'], width=650, height=350)
        self.ref['preview-a'].pack(side=LEFT, expand=False, fill=NONE)


        #     self.c.grid(row=1, column=1)
        # img1 = PhotoImage(file=r"C:\work\experiments\python\ignis-video-editor\data\bananas.png")
        # self.ref['image-container'] = self.ref['preview-a'].create_image(0, 0, anchor="nw", image=img1)

        return True
    # def a1testUI(self):
    #     tkRoot = super().getRoot()
    #     frame = Frame(tkRoot, width=800, height=600)
    #     frame.grid(row=1, column=1)
    #
    #     self.b = tk.Button(frame, text='test', command=lambda: self.a1testUI(), bg='#333', fg='#fff')
    #     self.b.grid(row=4, column=4)
    #                 # uiRef['followAll'].configure(width=64, height=64)
    #     self.b.configure(width=10)
    #
    #     self.c = tk.Canvas(frame, width=650, height=350)
    #     self.c.grid(row=1, column=1)
    #     img1 = PhotoImage(file=r"C:\work\experiments\python\ignis-video-editor\data\bananas.png")
    #     self.image_container = self.c.create_image(0, 0, anchor="nw", image=img1)
    #
    #
    #     # import threading
    #     # uiThread = threading.Thread(target=self.x(), args=[])
    #     # uiThread.start()
    #     self.img2 = PhotoImage(file=r"C:\work\experiments\python\ignis-video-editor\data\bananas2.PNG")
    #     # image_container = self.c.create_image(0, 0, anchor="nw", image=img1)
    #     print(self.c)
    #     self.c.itemconfig(self.image_container, image=self.img2)
    #     # self.c.create_image(0, 0, anchor="nw", image=img2)
