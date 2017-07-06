import sys
sys.path.append("librerias")
from Adafruit_PWM_Servo_Driver import PWM
import time
from Tkinter import *
from PIL import Image
import threading



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
 

###
###Funcion para leer archivo txt y agregarlo a una matriz
###
def setMatrixServos(archivo):
        with open(archivo, "r") as ins:
		for line in ins:
			matrixServos.append(line.split(","))
#------------------

###
### obtengo las posiciones segun el nombre asignado en el archivo
###
def getPositions(str):
	for i in matrixServos:
		if i[0] == str:
			return i 
#----------------

#----------------


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

def modo_real(nombre,n,t):
	arch=nombre
	numero=n
	tiempo=t
	setMatrixServos(arch)
       	setPositionsFromFile(arch,numero,tiempo)

        
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

home()
time.sleep(3)
modo_real("puntoxy.txt",1,0.1)
home()
time.sleep(3)
modo_real("kick.txt",1,0.1)

        
