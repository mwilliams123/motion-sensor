from picamera2 import Picamera2
from picamera2.encoders import H264Encoder, Quality
from picamera2.outputs import FileOutput

class Camera:
    def __init__(self) -> None:
        self.encoder = H264Encoder()
        self.file_number = 1
        self.recording = False
        self.camera = Picamera2()
        size = (640, 480)
        config = self.camera.create_video_configuration(main={"size": size})
        self.camera.configure(config)
        self.camera.start()

    def snapshot(self):
        return self.camera.capture_buffer("main")

    def record(self):
        if self.recording:
            return
        print("Motion sensor activated!")
        self.recording = True
        self.encoder.output = FileOutput('videos/out' + str(self.file_number) + '.h264')
        self.file_number += 1
        self.camera.start_encoder(self.encoder, Quality.VERY_LOW)

    def stop_recording(self):
        if not self.recording:
            return
        print("Motion sensor deactivated.")
        self.recording = False
        self.camera.stop_encoder()

    
