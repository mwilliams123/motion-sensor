"""
This module provides a class for the Motion Sensor.

Classes:
    MotionSensor
"""
import numpy as np

class MotionSensor:
    """
    Class for operating a motion sensor.

    The motion sensor maintains an adaptive estimate of a scene's background. The
    background can change over time as lighting or other conditions shift.
    This background estimate is compared to camera stills to determine if someone
    has entered into frame.

    Attributes:
        alpha (float): Parameter to control how quickly background adapts to changes.
            Larger alpha means background estimate is updated quicker.
        size ((int,int)): Pixel dimensions (Width, Height) of the camera stills.
        background (ndarray): Current background estimate. Array of floats of size (Width, Height).
        var (ndarray): Variance estimate of the background. Array of floats of size (Width, Height).
        threshold (float): Minimum average pixel value change to trigger motion sensor.
            Higher thresholds trigger the motion sensor less often.
    """
    def __init__(self) -> None:
        self.alpha = 0.01
        self.size = (640,640)
        self.background = np.zeros(self.size)
        self.var = np.zeros(self.size)
        self.threshold = 3.5

    def detect_motion(self, img):
        """Determine if something of interest is in frame by comparing an image
            to the background estimate.

        Args:
            img (ndarray): A single still from the camera. Is an array of ints
                with dimensions WidthxHeightx3.

        Returns:
            boolean: True if motion is detected, False otherwise.
        """
        diff = np.abs(np.subtract(np.array(img), np.array(self.background), dtype=float))
        return np.mean(diff) > self.threshold

    def convert_to_grayscale(self, img):
        """Convert a color image to grayscale.

        Args:
            img (ndarray): A single still from the camera. Is an array of ints
                with dimensions Width x Height x 3.

        Returns:
            ndarray: A flattened black and white image. Is an array of floats with
                dimensions Width*Height x 1.
        """
        img = img.reshape((self.size[0],self.size[1],3))
        return np.mean(img, axis=2)

    def estimate_background(self, img, frame):
        """Update the initial background estimate with a new running average
            of the first few frames.

        Args:
            img (ndarray): A single still from the camera. Is an array of ints
                with dimensions Width x Height x 3.
            frame (int): Frame number.
        """
        img = self.convert_to_grayscale(img)
        self.background = self.background + (img - self.background)/frame
        self.var = self.var + np.square(np.abs(img - self.background))/frame

    def update_background(self, img):
        """Update the current background estimate and variance given a new image.
            Allows motion sensor to be adaptive to changing backgrounds.

        Args:
            img (ndarray): A single still from the camera. Is an array of ints
                with dimensions Width x Height x 3.
        """
        img = self.convert_to_grayscale(img)
        self.background = self.alpha * img + (1-self.alpha) * self.background
        self.var = self.alpha * np.square(np.abs(img - self.background)) + (1-self.alpha) * self.var
 