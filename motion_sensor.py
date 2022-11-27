import numpy as np

class MotionSensor:
    def __init__(self) -> None:
        self.alpha = 0.01
        self.size = (640,640)
        self.bg = np.zeros(self.size)
        self.var = np.zeros(self.size)
        self.threshold = 3.5

    def detect_motion(self, img):
        diff = np.abs(np.subtract(np.array(img), np.array(self.bg), dtype=float))
        return np.mean(diff) > self.threshold

    def convert_to_grayscale(self, img):
        img = img.reshape((self.size[0],self.size[1],3))
        return np.mean(img, axis=2)

    def estimate_background(self, img, n):
        img = self.convert_to_grayscale(img)
        self.bg = self.bg + (img - self.bg)/n
        self.var = self.var + np.square(np.abs(img - self.bg))/n

    def update_background(self, img):
        img = self.convert_to_grayscale(img)
        self.bg = self.alpha * img + (1-self.alpha) * self.bg
        self.var = self.alpha * np.square(np.abs(img - self.bg)) + (1-self.alpha) * self.var
 