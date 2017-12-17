## This script will be a demo script to use the raspberry pi camera
## using OpenCV

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640,480))

#allow camera to warm up
time.sleep(0.1)

#capture frames from camera

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("q"):
        break
                        
# grab an image from the camera

camera.capture(rawCapture, format="bgr")
image = rawCapture.array

# display the image
cv2.imshow("From Pi Camera", image)
cv2.waitKey(0)
