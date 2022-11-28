"""
Motion Sensor.

This script starts the motion sensor. It takes snapshots periodically and
saves a video to file when motion is detected.

Usage:
    python main.py
"""
from time import sleep
from camera import Camera
from motion_sensor import MotionSensor

camera = Camera()
sensor = MotionSensor()

# use first 10 frames to generate background estimate
for i in range(10):
    img = camera.snapshot()
    sensor.estimate_background(img, i)
    sleep(1)

# run motion detector, record video when sensor is activated
while True:
    img = camera.snapshot()
    if sensor.detect_motion(img):
        camera.record()
    else:
        camera.stop_recording()
    sensor.update_background(img)
    sleep(1)
