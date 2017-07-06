from Adafruit_PWM_Servo_Driver import PWM
import time
from Tkinter import *
from PIL import Image
import threading

imagen = Image.open("robot.jpg")
imagen.show()

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

###
### setteo cada posicion leida del archivo al robot
###
def setPositionRobot(posicion):
	servoPort = 0 
	ft = False  #primera vez first time. es por que el internet esta lento y no pude buscar como hacerlo mejor :(	
	for p in posicion:
		if ft and servoPort <= 15:
			servo(servoPort, int(p) ) 
			servoPort = servoPort + 1 		
		else:
			ft = True 
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

def cambiarValores(posicion):
	#A
	s1.set(int(posicion[1]))
	s2.set(int(posicion[2]))
	s3.set(int(posicion[3]))
    
    #B
	s4.set(int(posicion[4]))
	s5.set(int(posicion[5]))
	s6.set(int(posicion[6]))
	
	#C
	s7.set(int(posicion[7]))
	s8.set(int(posicion[8]))
	s9.set(int(posicion[9]))
	s10.set(int(posicion[10]))
	s11.set(int(posicion[11]))
	
	#D
	s12.set(int(posicion[12]))
	s13.set(int(posicion[13]))
	s14.set(int(posicion[14]))
	s15.set(int(posicion[15]))
	s16.set(int(posicion[16]))

#setMatrixServos() 
#posicion = getPositions("home")  #nos devuelve el renglon
#print posicion
#setPositionRobot(posicion)


pwm.setPWMFreq(60)   

def modo_real():
	arch=str(nombre_entry.get())+".txt"
	setMatrixServos(arch) 
	print "Archivo: "+arch
	
	posicion = getPositions("home5")
	setPositionRobot2(posicion)
	time.sleep(3)
	
	for x in range(0,50):
		posicion = getPositions("home5")
		setPositionRobot2(posicion)
		time.sleep(2)
	
		posicion = getPositions("t")
		setPositionRobot2(posicion)
		time.sleep(1)
	
		posicion = getPositions("tt2")
		setPositionRobot2(posicion)
		time.sleep(1)
		
		posicion = getPositions("tt3")
		setPositionRobot2(posicion)
		time.sleep(1)
		
		posicion = getPositions("tt4")
		setPositionRobot2(posicion)
		time.sleep(1)
	
	

def boton_cambiarValores():	
	arch2=str(nombre_entry.get())+".txt"
	setMatrixServos(arch2) 
	pos=str(nombre_entry2.get())
	posicion = getPositions(pos)
	print pos
	cambiarValores(posicion)
	
def home():			
	
	#A
	s1.set(65)
	s2.set(11)
	s3.set(170)
    
    #B
	s4.set(140)
	s5.set(170)
	s6.set(23)
	
	#C
	s7.set(90)
	s8.set(150)
	s9.set(110)
	s10.set(58)
	s11.set(103)
	
	#D
	s12.set(95)
	s13.set(42)
	s14.set(80)
	s15.set(138)
	s16.set(95)

def valores_servos():
	#A
	#a1
	print s1.get()
	servo(2, int(s1.get()))
	#a2
	print s2.get()
	servo(1, int(s2.get()))
	#a3
	print s3.get()
	servo(0, int(s3.get()))
	
	#B
	#b1
	print s4.get()
	servo(13, int(s4.get()))
	#b2
	print s5.get()
	servo(14, int(s5.get()))
	#b3
	print s6.get()
	servo(15, int(s6.get()))
	
	#C
	#c1
	print s7.get()
	servo(3, int(s7.get()))
	#c2
	print s8.get()
	servo(4, int(s8.get()))
	#c3
	print s9.get()
	servo(5, int(s9.get()))
	#c4
	print s10.get()
	servo(6, int(s10.get()))
	#c5
	print s11.get()
	servo(7, int(s11.get()))
	
	#D
	#d1
	print s12.get()
	servo(8, int(s12.get()))
	#d2
	print s13.get()
	servo(9, int(s13.get()))
	#d3
	print s14.get()
	servo(10, int(s14.get()))
	#d4
	print s15.get()
	servo(11, int(s15.get()))
	#d5
	print s16.get()
	servo(12, int(s16.get()))

    
def agregar_datos():
	archi=open(str(nombre_entry.get())+".txt",'a')
	archi.write('\n')
	archi.write(str(nombre_entry2.get())+",")
	archi.write(str(s1.get())+",")
	archi.write(str(s2.get())+",")
	archi.write(str(s3.get())+",")
	archi.write(str(s4.get())+",")
	archi.write(str(s5.get())+",")
	archi.write(str(s6.get())+",")
	archi.write(str(s7.get())+",")
	archi.write(str(s8.get())+",")
	archi.write(str(s9.get())+",")
	archi.write(str(s10.get())+",")
	archi.write(str(s11.get())+",")
	archi.write(str(s12.get())+",")
	archi.write(str(s13.get())+",")
	archi.write(str(s14.get())+",")
	archi.write(str(s15.get())+",")
	archi.write(str(s16.get()))
	archi.close()
	print "SE HA AGREGADO AL ARCHIVO"

def crear_archivo():
	archi=open(str(nombre_entry.get())+".txt",'w')
	archi.write(str(nombre_entry2.get())+",")
	archi.write(str(s1.get())+",")
	archi.write(str(s2.get())+",")
	archi.write(str(s3.get())+",")
	archi.write(str(s4.get())+",")
	archi.write(str(s5.get())+",")
	archi.write(str(s6.get())+",")
	archi.write(str(s7.get())+",")
	archi.write(str(s8.get())+",")
	archi.write(str(s9.get())+",")
	archi.write(str(s10.get())+",")
	archi.write(str(s11.get())+",")
	archi.write(str(s12.get())+",")
	archi.write(str(s13.get())+",")
	archi.write(str(s14.get())+",")
	archi.write(str(s15.get())+",")
	archi.write(str(s16.get()))
	archi.close()
	print "SE HA GUARDADO EL ARCHIVO"
    


master = Tk()
master.title('A')
a1 = IntVar()
c = Checkbutton(master, text="Modo tiempo real", variable=a1, onvalue=1,offvalue=0)
c.pack()
s1 = Scale(master, from_=0, to=180, label="A1",  orient=HORIZONTAL)
s1.pack()
a2 = IntVar()
c2 = Checkbutton(master, text="Modo tiempo real", variable=a2,onvalue=1,offvalue=0)
c2.pack()
s2 = Scale(master, from_=0, to=180, label="A2", orient=HORIZONTAL)
s2.pack()
a3 = IntVar()
c3 = Checkbutton(master, text="Modo tiempo real", variable=a3)
c3.pack()
s3 = Scale(master, from_=0, to=180, label="A3",orient=HORIZONTAL)
s3.pack()

master2 = Tk()
master2.title('B')
b1 = IntVar()
c4 = Checkbutton(master2, text="Modo tiempo real", variable=b1)
c4.pack()
s4 = Scale(master2, from_=0, to=180, label="B1",orient=HORIZONTAL)
s4.pack()
b2 = IntVar()
c5 = Checkbutton(master2, text="Modo tiempo real", variable=b2)
c5.pack()
s5 = Scale(master2, from_=0, to=180, label="B2",orient=HORIZONTAL)
s5.pack()
b3 = IntVar()
c6 = Checkbutton(master2, text="Modo tiempo real", variable=b3)
c6.pack()
s6 = Scale(master2, from_=0, to=180, label="B3",orient=HORIZONTAL)
s6.pack()

while True:

		
	master3 = Tk()
	master3.title('C')
	cc1 = IntVar()
	c7 = Checkbutton(master3, text="Modo tiempo real", variable=cc1)
	c7.pack()
	s7 = Scale(master3, from_=0, to=180, label="C1",orient=HORIZONTAL)
	s7.pack()
	cc2 = IntVar()
	c8 = Checkbutton(master3, text="Modo tiempo real", variable=cc2)
	c8.pack()
	s8 = Scale(master3, from_=0, to=180, label="C2",orient=HORIZONTAL)
	s8.pack()
	cc3 = IntVar()
	c9 = Checkbutton(master3, text="Modo tiempo real", variable=cc3)
	c9.pack()
	s9 = Scale(master3, from_=0, to=180, label="C3",orient=HORIZONTAL)
	s9.pack()
	cc4 = IntVar()
	c10 = Checkbutton(master3, text="Modo tiempo real", variable=cc4)
	c10.pack()
	s10 = Scale(master3, from_=0, to=180, label="C4",orient=HORIZONTAL)
	s10.pack()
	cc5 = IntVar()
	c11 = Checkbutton(master3, text="Modo tiempo real", variable=cc5)
	c11.pack()
	s11 = Scale(master3, from_=0, to=180, label="C5",orient=HORIZONTAL)
	s11.pack()

	master4 = Tk()
	master4.title('D')
	d1 = IntVar()
	c12 = Checkbutton(master4, text="Modo tiempo real", variable=d1)
	c12.pack()
	s12 = Scale(master4, from_=0, to=180, label="D1",orient=HORIZONTAL)
	s12.pack()
	d2 = IntVar()
	c13 = Checkbutton(master4, text="Modo tiempo real", variable=d2)
	c13.pack()
	s13 = Scale(master4, from_=0, to=180, label="D2",orient=HORIZONTAL)
	s13.pack()
	d3 = IntVar()
	c14 = Checkbutton(master4, text="Modo tiempo real", variable=d3)
	c14.pack()
	s14 = Scale(master4, from_=0, to=180, label="D3",orient=HORIZONTAL)
	s14.pack()
	d4 = IntVar()
	c15 = Checkbutton(master4, text="Modo tiempo real", variable=d4)
	c15.pack()
	s15 = Scale(master4, from_=0, to=180, label="D4",orient=HORIZONTAL)
	s15.pack()
	d5 = IntVar()
	c16 = Checkbutton(master4, text="Modo tiempo real", variable=d5)
	c16.pack()
	s16 = Scale(master4, from_=0, to=180, label="D5",orient=HORIZONTAL)
	s16.pack()


	root = Tk()
	root.title('Servos')
	# CAMPO 1 : Nombre archivo
	nombre_label = Label(root,text="Nombre txt: ")
	nombre_label.grid(row=1,column=1)
	nombre_str = StringVar()
	nombre_entry = Entry(root,textvariable=nombre_str)
	nombre_entry.grid(row=1,column=2)

	nombre_label2 = Label(root,text="Nombre rutina: ")
	nombre_label2.grid(row=2,column=1)
	nombre_str2 = StringVar()
	nombre_entry2 = Entry(root,textvariable=nombre_str2)
	nombre_entry2.grid(row=2,column=2)

	# CAMPO 2 : boton ejecutar
	ejecutar = Button(root,text="Ejecutar movimiento de servos",command=valores_servos,relief=FLAT)
	ejecutar.grid(row=3,column=1)
	# CAMPO 3 : boton ejecutar
	agregar = Button(root,text="Agregar rutina de valores al archivo",command=agregar_datos,relief=FLAT)
	agregar.grid(row=4,column=1)
	# CAMPO 4 : boton ejecutar
	crear = Button(root,text="Crear un nuevo archivo",command=crear_archivo,relief=FLAT)
	crear.grid(row=5,column=1)
	#CAMPO 5: boton modo real
	real = Button(root,text="Ejecutar Archivo",command=modo_real,relief=FLAT,state=ACTIVE, repeatdelay=1, repeatinterval=1)
	real.grid(row=6,column=1)
	real = Button(root,text="Cambiar valores (introducir archivo y rutina)",command=boton_cambiarValores,relief=FLAT,state=ACTIVE, repeatdelay=1, repeatinterval=1)
	real.grid(row=7,column=1)
	home()
	mainloop()

