from io import BytesIO
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder, Quality
from picamera2.outputs import FileOutput
from time import sleep
import numpy as np

camera= Picamera2()
size = (640, 480)
config = camera.create_video_configuration(main={"size": size})
camera.configure(config)
encoder = H264Encoder()
i = 1
def record():
    global i
    print("motion sensor activated!")
    encoder.output = FileOutput('videos/out' + str(i) + '.h264')
    i += 1
    camera.start_encoder(encoder,Quality.VERY_LOW)
    
def detect_motion(img, bg):
    diff = np.abs(np.subtract(np.array(img), np.array(bg), dtype=float))
    m = np.mean(diff)
    print(m)
    return m > 7

prev = None
camera.start()
bg = np.zeros((640 ,640))
var = np.zeros((640,640))
n = 1
a = 0.01
recording = False
while True:
    img = camera.capture_buffer("main")
    img = img.reshape((640,640,3))
    img = np.mean(img, axis=2)
    if n <= 10:
        bg = bg + (img - bg)/n
        var = var + np.square(np.abs(img - bg))/n
    else:
        if detect_motion(img, bg):
            if not recording:
                recording = True
                record()
        elif recording:
            print("stop recording")
            recording = False
            camera.stop_encoder()
        bg = a * img + (1-a) * bg
        var = a * np.square(np.abs(img - bg)) + (1-a) * var
    n += 1
    sleep(1)
