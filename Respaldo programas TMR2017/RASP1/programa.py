import sys
sys.path.append("librerias")
from Adafruit_PWM_Servo_Driver import PWM
import time
from Tkinter import *
from PIL import Image
import threading
import cv2
import numpy as np
import time


# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

#servo90 = ((servoMax-servoMin)/2)+servoMin
servoMin = 100  # Min pulse length out of 4096
servoMax = 650  # Max pulse length out of 4096

matrixServos = list()  #matriz de posiciones de los servos
c=0
### CONSTANTES ###                                                    
B1 = 0;  B2 = 1;  B3 = 2;
D1 = 3;  D2 = 4;  D3 = 5;  D4 = 6;  D5 = 7; 

A1 = 8;  A2 = 9;  A3 = 10; 
C1 = 11;  C2 = 12;  C3 = 13;  C4 = 14;  C5 = 15; 

### FIN CONSTANTES ###


def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 50                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

def servo(puerto, angulo):
  frec = int((angulo * ((servoMax-servoMin)/180)) + servoMin)
  pwm.setPWM(puerto ,0 ,frec)
  #time.sleep(.3)
  
def setMatrixServos(archivo):
        with open(archivo, "r") as ins:
		for line in ins:
			matrixServos.append(line.split(","))

def setPositionRobot2(posicion):
	#A
	#a1
        servo(2, int(posicion[1]))
	#a2
	servo(1, int(posicion[2]))
	#a3
	servo(0, int(posicion[3]))
	
	#B
	#b1
	servo(13, int(posicion[4]))
	#b2
	servo(14, int(posicion[5]))
	#b3
	servo(15, int(posicion[6]))
	
	#C
	#c1
	servo(3, int(posicion[7]))
	#c2
	servo(4, int(posicion[8]))
	#c3
	servo(5, int(posicion[9]))
	#c4
	servo(6, int(posicion[10]))
	#c5
	servo(7, int(posicion[11]))
	
	#D
	#d1
	servo(8, int(posicion[12]))
	#d2
	servo(9, int(posicion[13]))
	#d3
	servo(10, int(posicion[14]))
	#d4
	servo(11, int(posicion[15]))
	#d5
	servo(12, int(posicion[16]))
	

def home():
	arch="home.txt"
	setMatrixServos(arch)
       	setPositionsFromFile(arch,1,0.1)
       	
def derecha():
	arch="derecha.txt"
	setMatrixServos(arch)
       	setPositionsFromFile(arch,1,0.8)

def izquierda():
	arch="izquierda.txt"
	setMatrixServos(arch)
       	setPositionsFromFile(arch,1,0.8)

def setPositionsFromFile(file,num,tt):
    arch=str(file)
    setMatrixServos(arch)
    print matrixServos
    for x in range(0,num):
      for i in matrixServos:
        posicion = i
        print posicion
        setPositionRobot2(posicion)
        time.sleep(tt)
      
        

foreground1 = cv2.imread("foreground1.jpg")
video = cv2.VideoCapture(0)

cv2.namedWindow("video")
cv2.namedWindow("canny")
cv2.namedWindow("blur")

def procesar():
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
                      #print c[0]
                      #print c[1]
      edges = cv2.Canny( gray, 40, 80 )
      cv2.imshow("video", frame)
      cv2.imshow("canny", edges)
      cv2.imshow("blur", gray)
      try:
        if c[1] > 250:
          if c[0] > 450:
              print "derecha"
              derecha()
          elif c[0] < 200:
              print "izquierda"
              izquierda()
          else:
              home()	  
        else:
           home()
      except:
        home()
        print "error"
      cv2.waitKey(0)

