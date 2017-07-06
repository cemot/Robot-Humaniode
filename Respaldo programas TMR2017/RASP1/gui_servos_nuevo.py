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


pwm.setPWMFreq(60)   

def modo_real():
        matrixServos = list()
	arch=str(nombre_entry.get())+".txt"
	numero=int(num_entry.get())
	tiempo=float(tiempo_entry.get())
	setMatrixServos(arch)
       	setPositionsFromFile(arch,numero,tiempo)
        
	

	
def cambiarValoresYEjecutar():
    boton_cambiarValores()
    valores_servos()

def boton_cambiarValores():
    arch2=str(nombre_entry.get())+".txt"
    setMatrixServos(arch2) 
    pos=str(nombre_entry2.get())
    posicion = getPositions(pos)
    print pos
    cambiarValores(posicion)
	
def home():			
	print "home"
	20,23,88,90,97,130,140,115,90
	#A
	s1.set(132)
	servo(2, 132)

	s2.set(50)
	servo(1,50)

	s3.set(90)
        servo(0,90)
	
        #B
	s4.set(61)
	servo(13,61)

	s5.set(111)
	servo(14, 111)

	s6.set(90)
        servo(15, 90)
	
	#C
	s7.set(90)
	servo(3, 90)

	s8.set(20)
	servo(4, 20)

	s9.set(23)
	servo(5, 23)

	s10.set(88)
	servo(6, 88)

	s11.set(90)
        servo(7, int(s11.get()))
	
	#D
	s12.set(90)
	servo(8, int(s12.get()))

	s13.set(109)
	servo(9, int(s13.get()))

	s14.set(180)
	servo(10, int(s14.get()))

	s15.set(121)
	servo(11, int(s15.get()))

	s16.set(90)
        servo(12, int(s16.get()))




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
    
def a3_onChange(value):
    servo(0,int(value) )

def a2_onChange(value):
    servo(1,int(value) )

def a1_onChange(value):
    servo(2,int(value) )

def c1_onChange(value):
    servo(3,int(value) )

def c2_onChange(value):
    servo(4,int(value) )

def c3_onChange(value):
    servo(5,int(value) )

def c4_onChange(value):
    servo(6,int(value) )

def c5_onChange(value):
    servo(7,int(value) )

def d1_onChange(value):
    servo(8,int(value) )

def d2_onChange(value):
    servo(9,int(value) )

def d3_onChange(value):
    servo(10,int(value) )

def d4_onChange(value):
    servo(11,int(value) )

def d5_onChange(value):
    servo(12,int(value) )

def b1_onChange(value):
    servo(13,int(value) )

def b2_onChange(value):
    servo(14,int(value) )

def b3_onChange(value):
    servo(15,int(value) )

def crearPasos():
    arch=str(file)
    setMatrixServos(arch)
    print arch

def setPositionsFromFile(file,num,tt):
    arch=str(file)
    print matrixServos
    for x in range(0,num):
      for i in matrixServos:
        posicion = i
        print posicion
        setPositionRobot2(posicion)
        time.sleep(tt)
    

def setPositionsFromFileAntiguo(file, t):
    arch=str(file)+".txt"
    setMatrixServos(arch)
    print matrixServos
    
    for i in matrixServos:
      posicion = i
      setPositionRobot2(posicion)
      time.sleep(t)
     

master = Tk()
master.title('SERVOS')

##	SERVOS A
a1 = IntVar()
s1 = Scale(master, from_=0, to=180, label="A1",  orient=HORIZONTAL, command=a1_onChange)
s1.grid(row=1,column=1)

a2 = IntVar()
s2 = Scale(master, from_=0, to=180, label="A2", orient=HORIZONTAL, command=a2_onChange)
s2.grid(row=2,column=1)

a3 = IntVar()
s3 = Scale(master, from_=0, to=180, label="A3",orient=HORIZONTAL, command=a3_onChange)
s3.grid(row=3,column=1)


##	SERVOS B
b1 = IntVar()
s4 = Scale(master, from_=0, to=180, label="B1",orient=HORIZONTAL, command=b1_onChange)
s4.grid(row=1,column=4)

b2 = IntVar()
s5 = Scale(master, from_=0, to=180, label="B2",orient=HORIZONTAL, command=b2_onChange)
s5.grid(row=2,column=4)

b3 = IntVar()
s6 = Scale(master, from_=0, to=180, label="B3",orient=HORIZONTAL, command=b3_onChange)
s6.grid(row=3,column=4)

##	SERVOS C	
cc1 = IntVar()
s7 = Scale(master, from_=0, to=180, label="C1",orient=HORIZONTAL, command=c1_onChange)
s7.grid(row=1,column=2)

cc2 = IntVar()
s8 = Scale(master, from_=0, to=180, label="C2",orient=HORIZONTAL, command=c2_onChange)
s8.grid(row=2,column=2)

cc3 = IntVar()
s9 = Scale(master, from_=0, to=180, label="C3",orient=HORIZONTAL, command=c3_onChange)
s9.grid(row=3,column=2)

cc4 = IntVar()
s10 = Scale(master, from_=0, to=180, label="C4",orient=HORIZONTAL, command=c4_onChange)
s10.grid(row=4,column=2)

cc5 = IntVar()
s11 = Scale(master, from_=0, to=180, label="C5",orient=HORIZONTAL, command=c5_onChange)
s11.grid(row=5,column=2)

##	SERVOS D
d1 = IntVar()
s12 = Scale(master, from_=0, to=180, label="D1",orient=HORIZONTAL, command=d1_onChange)
s12.grid(row=1,column=3)

d2 = IntVar()
s13 = Scale(master, from_=0, to=180, label="D2",orient=HORIZONTAL, command=d2_onChange)
s13.grid(row=2,column=3)

d3 = IntVar()
s14 = Scale(master, from_=0, to=180, label="D3",orient=HORIZONTAL, command=d3_onChange)
s14.grid(row=3,column=3)

d4 = IntVar()
s15 = Scale(master, from_=0, to=180, label="D4",orient=HORIZONTAL, command=d4_onChange)
s15.grid(row=4,column=3)

d5 = IntVar()
s16 = Scale(master, from_=0, to=180, label="D5",orient=HORIZONTAL, command=d5_onChange)
s16.grid(row=5,column=3)


while True:

	# CAMPO 1 : Nombre archivo
	nombre_label = Label(master,text="Nombre txt: ")
	nombre_label.grid(row=1,column=7)
	nombre_str = StringVar()
	nombre_entry = Entry(master,textvariable=nombre_str)
	nombre_str.set("izquierda");
	nombre_entry.grid(row=1,column=8)
        nombre_label2 = Label(master,text="Nombre rutina: ")
	nombre_label2.grid(row=2,column=7)
	nombre_str2 = StringVar()
	nombre_entry2 = Entry(master,textvariable=nombre_str2)
	nombre_str2.set("");
	nombre_entry2.grid(row=2,column=8)

	# CAMPO 2 : 
	real = Button(master,text="Cambiar valores GUI y ejecutar",command=cambiarValoresYEjecutar,relief=FLAT)
	real.grid(row=3,column=7)
	# CAMPO 3 : 
	agregar = Button(master,text="Agregar rutina de valores al archivo",command=agregar_datos,relief=FLAT)
	agregar.grid(row=4,column=7)
	#CAMPO 4: 	
	crear = Button(master,text="Crear un nuevo archivo",command=crear_archivo,relief=FLAT)
	crear.grid(row=5,column=7)
        crear = Button(master,text="Ejecutar archivo",command=modo_real,relief=FLAT)
	crear.grid(row=6,column=7)
        num_str = StringVar()
	num_entry = Entry(master,textvariable=num_str)
	num_str.set("40");
	num_entry.grid(row=6,column=8)
	tiempo_str = StringVar()
	tiempo_entry = Entry(master,textvariable=tiempo_str)
	tiempo_str.set("0.1");
	tiempo_entry.grid(row=7,column=8)
	crear = Button(master,text="OBTENER PASOS",command=crearPasos,relief=FLAT)
	crear.grid(row=8,column=7)
        rutina1 = StringVar()
	rutina1_entry = Entry(master,textvariable=rutina1)
	rutina1_entry.grid(row=8,column=8)
	rutina2 = StringVar()
	rutina2_entry = Entry(master,textvariable=rutina2)
	rutina2_entry.grid(row=9,column=8)
	
        
        time.sleep(2)
        modo_real()
        
        
        time.sleep(5)
        matrixServos = list()
        tiempo_str.set("0.2")
        num_str.set("1");
        nombre_str.set("home");
        modo_real()
        time.sleep(100000000)
        
        mainloop()
        
        
