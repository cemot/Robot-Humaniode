import cv2
import numpy as np

foreground1 = cv2.imread("foreground1.jpg")
video = cv2.VideoCapture(0)

cv2.namedWindow("video")
cv2.namedWindow("canny")
cv2.namedWindow("blur")

while True:
    ret, frame = video.read()
   
    framegrey1 = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(framegrey1, (0,0), 2)
    gray = cv2.medianBlur(gray,5)
	
    # Adaptive Guassian Threshold is to detect sharp edges in the Image. For more information Google it.
    gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
		        cv2.THRESH_BINARY,11,3.5)
		
    kernel = np.ones((2.6,2.7),np.uint8)
    gray = cv2.erode(gray,kernel,iterations = 1)
    # gray = erosion
	
    gray = cv2.dilate(gray,kernel,iterations = 1)
    # gray = dilation
    circles =  cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 10, np.array([]), 40, 80, 5, 100)
    if circles is not None:
            for c in circles[0]:
                    cv2.circle(frame, (c[0],c[1]), c[2], (0,255,0),2)
    edges = cv2.Canny( gray, 40, 80 )
    cv2.imshow("video", frame)
    cv2.imshow("canny", edges)
    cv2.imshow("blur", gray)
    key = cv2.waitKey(30)
