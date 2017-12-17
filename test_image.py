## This script will be a demo script to use the raspberry pi camera
## using OpenCV

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
rawCapture = PiRGBArray(camera)

#allow camera to warm up
time.sleep(0.1)

# grab an image from the camera

camera.capture(rawCapture, format="bgr")
image = rawCapture.array

# display the image
cv2.imshow("From Pi Camera", image)
cv2.waitKey(0)
