from PIL import ImageTk, Image
from tkinter.ttk import Frame, Label
import tkinter as tk

from PIL.ImageTk import PhotoImage

from gui.windows10.tkinker.TkView import TkView

class Win10TkMainView(TkView):
    # def __init__(self, caller: MainView):
    #     self.caller = caller

    def render(self):
        tkRoot = super().getRoot()

        frame = Frame(tkRoot, width=800, height=600)
        frame.grid(row=1, column=1)
        #
        # img = ImageTk.PhotoImage(Image.open(r"C:\work\experiments\python\ignis-video-editor\data\bananas.png"), size=(100, 50))


        self.b = tk.Button(frame, text='test', command=lambda: self.a1testUI(), bg='#333', fg='#fff')
        self.b.grid(row=4, column=4)
        # uiRef['followAll'].configure(width=64, height=64)
        self.b.configure(width=10)

        self.c = tk.Canvas(frame, width=650, height=350)
        self.c.grid(row=1, column=1)
        img1 = PhotoImage(file=r"C:\work\experiments\python\ignis-video-editor\data\bananas.png")
        self.image_container = self.c.create_image(0, 0, anchor="nw", image=img1)

        super().start()

    def a1testUI(self):
        img2 = PhotoImage(file=r"C:\work\experiments\python\ignis-video-editor\data\bananas2.PNG")
        # image_container = self.c.create_image(0, 0, anchor="nw", image=img1)
        self.c.itemconfig(self.image_container,image=img2)
        # self.c.create_image(0, 0, anchor="nw", image=img2)
