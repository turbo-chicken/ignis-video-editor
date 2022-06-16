import ffmpeg
import numpy as np
from ffprobe import FFProbe

class Video:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.frames = 0
        self.initProbeDetails()

    def initProbeDetails(self):
        metadata = FFProbe(self.path)
        print(metadata)
        for stream in metadata.streams:
            if stream.is_video():
                self.frames = stream.frames()
                print('Stream contains {} frames.'.format(stream.frames()))
        pass

    def getFrame(self, frameIndex):
        width = 900
        height = 600

        out, _ = (
            ffmpeg
                .input(self.path)
                .filter('select', 'gte(n,{})'.format(3))
                .output('pipe:', vframes=1, format='image2', vcodec='mjpeg')
                .run(capture_stdout=True)
        )
        #print(out)
        from PIL.Image import Image
        import io
        image = Image.open(io.BytesIO(out))
        return image

        # out, _ = (
        #     ffmpeg
        #         .input(self.path)
        #         .output('pipe:', format='rawvideo', pix_fmt='rgb24')
        #         .run(capture_stdout=True)
        # )
        # video = (
        #     np
        #         .frombuffer(out, np.uint8)
        #         .reshape([-1, height, width, 3])
        # )
        #
        # return video