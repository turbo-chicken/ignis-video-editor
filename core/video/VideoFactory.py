from core.video.Video import Video

class VideoFactory:
    def __init__(self):
        pass

    def create(self, name, path):
        return Video(name, path)