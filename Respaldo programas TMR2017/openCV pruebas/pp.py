import numpy as np
import cv2
 
def nothing(x):
    pass
# Creamos una variable de camara y asigamos la primera camara disponible con "0"
cap = cv2.VideoCapture(1)
cv2.namedWindow('Configuracion')
 
# Crearemos los controles para indicar el color que seguiremos
 
cv2.createTrackbar ('H min', 'Configuracion', 0,256,nothing)
cv2.createTrackbar ('H max', 'Configuracion', 0,256,nothing)
cv2.createTrackbar ('S min', 'Configuracion', 0,256,nothing)
cv2.createTrackbar ('S max', 'Configuracion', 0,256,nothing)
cv2.createTrackbar ('V min', 'Configuracion', 0,256,nothing)
cv2.createTrackbar ('V max', 'Configuracion', 0,256,nothing)
 
# Iniciamos el bucle de captura, en el que leemos cada frame de la captura
while(True):
	ret, frame = cap.read()
	if not ret: continue
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Convertimos imagen a HSV
	if not ret: continue
	# Asignamos las variables del rango de color que seguiremos
	Hmin = cv2.getTrackbarPos('H min', 'Configuracion')
	Hmax = cv2.getTrackbarPos('H max', 'Configuracion')
	Smin = cv2.getTrackbarPos('S min', 'Configuracion')
	Smax = cv2.getTrackbarPos('S max', 'Configuracion')
	Vmin = cv2.getTrackbarPos('V min', 'Configuracion')
	Vmax = cv2.getTrackbarPos('V max', 'Configuracion')

	# Aqui mostramos la imagen en blanco o negro segun el rango de colores.
	bn_img = cv2.inRange(hsv, np.array((Hmin,Smin,Vmin)), np.array((Hmax,Vmax,Smax)))

	# Limpiamos la imagen de imperfecciones con los filtros erode y dilate
	bn_img = cv2.erode (bn_img,cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)),iterations = 1)
	bn_img = cv2.dilate (bn_img,cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)),iterations = 1)
	# Localizamos la posicion del objeto
	M = cv2.moments(bn_img)
	if M['m00']>50000:
	    cx = int(M['m10']/M['m00'])
	    cy = int(M['m01']/M['m00'])
	# Mostramos un circulo verde en la posicion en la que se encuentra el objeto
	    cv2.circle (frame,(cx,cy),20,(0,255,0), 2)


	# Creamos las ventanas de salida y configuracion
	cv2.imshow('Salida', frame)
	cv2.imshow('inRange', bn_img)

	if cv2.waitKey(30) & 0xFF == ord('q'): # Indicamos que al pulsar "q" el programa se cierre
	    break
 
cap.release()
cv2.destroyAllWindows()