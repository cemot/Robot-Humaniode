




from Adafruit_PWM_Servo_Driver import PWM
import time
import threading
import serial

arduino=serial.Serial('/dev/ttyUSB0',38400)
print("iniciamos")
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
 

#setMatrixServos() 
#posicion = getPositions("home")  #nos devuelve el renglon
#print posicion
#setPositionRobot(posicion)


pwm.setPWMFreq(60)   

def equilibrioX():
	while True:
		print "EQUILIBRANDO X"
		time.sleep(2)

def equilibrioY():
	while True:
		print "EQUILIBRANDO Y"
		time.sleep(1)

#task1=threading.Thread(target=equilibrioX,name="EQUILIBRIOX")
#task2=threading.Thread(target=equilibrioY,name="EQUILIBRIOY")
#task1.start()
#task2.start()
def map(x,in_min,in_max,out_min,out_max):
	return (x-in_min)*(out_max-out_min)/(in_max-in_min)+out_min

def home():
	#A
	#a1
	servo(2, 115)
	#a2
	servo(1, 55)
	#a3
	servo(0, 90)
	
	#B
	#b1
	servo(13, 65)
	#b2
	servo(14, 135)
	#b3
	servo(15, 90)
	
	#C
	#c1
	servo(3, 90)
	#c2
	servo(4, 40)
	#c3
	servo(5, 40)
	#c4
	servo(6, 80)
	#c5
	servo(7, 90)
	
	#D
	#d1
	servo(8, 90)
	#d2
	servo(9, 90)
	#d3
	servo(10, 130)
	#d4
	servo(11, 105)
	#d5
	servo(12, 90)
	
while(True):
	home()
	var = arduino.readline()
	x=var.split(",")[0]
	y=var.split(",")[1]
	z=var.split(",")[2]
	
	#cambio = map(int(y),-13,23,6,-6)
	print x+","+y+","+z

arduino.close()
