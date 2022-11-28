"""
This module provides a wrapper class for the camera hardware.

Classes:
    Camera
"""
import time
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder, Quality
from picamera2.outputs import FileOutput

class Camera:
    """
    Class that represents the Camera module.

    Provides an interface for taking snapshots and recording videos to file.

    Attributes:
        encoder (Encoder): Picamera's encoder that writes video to file.
        recording (boolean): Bool to keep track of whether encoder is running.
        camera (Picamera2): Picamera's camera module.
    """
    def __init__(self) -> None:
        self.encoder = H264Encoder()
        self.recording = False
        self.camera = Picamera2()
        size = (640, 480)
        config = self.camera.create_video_configuration(main={"size": size})
        self.camera.configure(config)
        self.camera.start()

    def snapshot(self):
        """Takes a still photo with the camera.

        Returns:
            ndarray: Array of ints with dimensions WidthxHeightx3 that represents a
                single camera photo.
        """
        return self.camera.capture_buffer("main")

    def record(self):
        """Starts the encoder to record video to file."""
        if self.recording:
            return
        print("Motion sensor activated!")
        self.recording = True
        self.encoder.output = FileOutput('videos/out' + time.strftime("%Y%m%d-%H%M%S") + '.h264')
        self.camera.start_encoder(self.encoder, Quality.VERY_LOW)

    def stop_recording(self):
        """Stops recording video to file by pausing the encoder."""
        if not self.recording:
            return
        print("Motion sensor deactivated.")
        self.recording = False
        self.camera.stop_encoder()
