# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np
import cv2
 
def nothing(x):
    pass
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
t=0
# allow the camera to warmup
time.sleep(0.1)


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array
 	ret=frame.array
 	# show the frame
	cv2.imshow("Frame", image)

	
	rawCapture.truncate(0)
	if cv2.waitKey(30) & 0xFF == ord('q'): # Indicamos que al pulsar "q" el programa se cierre
		cv2.destroyWindow("output")
		output = image.copy()
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		
		gray = cv2.GaussianBlur(gray,(5,5),0);
		gray = cv2.medianBlur(gray,5)
	
		# Adaptive Guassian Threshold is to detect sharp edges in the Image. For more information Google it.
		gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
		        cv2.THRESH_BINARY,11,3.5)
		
		kernel = np.ones((2.6,2.7),np.uint8)
		gray = cv2.erode(gray,kernel,iterations = 1)
		# gray = erosion
	
		gray = cv2.dilate(gray,kernel,iterations = 1)
		# gray = dilation
               
		circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 30, param1=50, param2=22, minRadius=5, maxRadius=25)
		 
		# ensure at least some circles were found
		if circles is not None:
			# convert the (x, y) coordinates and radius of the circles to integers
			circles = np.round(circles[0, :]).astype("int")
		 
			# loop over the (x, y) coordinates and radius of the circles
			for (x, y, r) in circles:
				# draw the circle in the output image, then draw a rectangle
				# corresponding to the center of the circle
				cv2.circle(output, (x, y), r, (0, 255, 0), 4)
				cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
		 
			# show the output image
			cv2.imshow("output", output)


 
