




#Version 1.4
#CODIGO
#TUXTEAM
import cv2
import numpy as np

maxCirculos=6
maxCirculos=maxCirculos-1
video = cv2.VideoCapture(0)
while True:
    ret, frame = video.read()
    framegrey1 = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow("Original", framegrey1)
    gray = cv2.GaussianBlur(framegrey1, (1,1), 2)
    gray = cv2.medianBlur(gray,5)
    gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
		        cv2.THRESH_BINARY,19,3)

    kernel = np.ones((2.6,2.7),np.uint8)
    gray = cv2.erode(gray,kernel,iterations = 1) 
    gray = cv2.dilate(gray,kernel,iterations = 1)
    
    circles =  cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 10, np.array([]), 40, 80, 5, 100)
    circulos=0
    if circles is not None:
            for c in circles[0]:
                    cv2.circle(frame, (c[0],c[1]), c[2], (0,255,0),2)
                    circulos=circulos+1
                    print "Coordenada X: " + str(c[0])
                    print "Coordenada Y: " + str(c[1])
                    if(circulos>maxCirculos):
                    	break
    else:
		print("NO SE DETECTA EL BALON");
    
  
    cv2.imshow("video", frame)
    cv2.imshow("filtros", gray)
    key = cv2.waitKey(1)
