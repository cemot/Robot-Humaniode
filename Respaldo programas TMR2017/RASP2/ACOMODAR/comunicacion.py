



import serial
import time

from PIL import Image
arduino=serial.Serial('/dev/ttyUSB0',9600)
print("iniciamos")

#try:
	#imagen = Image.open("m.jpg")
	#imagen.show()
#except:
    #print("No ha sido posible cargar la imagen")
    
#time.sleep(2)

def map(x,in_min,in_max,out_min,out_max):
	return (x-in_min)*(out_max-out_min)/(in_max-in_min)*out_min

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
	#servo(3, )
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
	#servo(8, int(s12.get()))
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
	try:
		print int(x)
		print int(y)
		print int(z)
		print ""
	except:
		print "ERROR"
	
	cambio = map(int(y),-13,23,3,-3)
	
arduino.close()
