from PIL.ImageTk import PhotoImage

from core.video.Video import Video
from core.video.VideoFactory import VideoFactory


class Env:
    def __init__(self, video_factory: VideoFactory):
        self.img = None

    def getImg(self, video):
        # self.img = PhotoImage(file=r"C:\work\experiments\python\ignis-video-editor\data\bananas.png")
        return video.getFrame(3)
        return self.img

    def getNextImg(self, i):
        self.img = PhotoImage(file=r"C:\work\experiments\python\ignis-video-editor\data\bananas" + str(i) + ".png")
        return self.img

    def getCurrentVideo(self):
        return Video('test', 'data/video/vid_1.mp4')
