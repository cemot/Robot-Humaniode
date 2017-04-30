




#Version 1.4
#CODIGO COMENTADO
#Librerias necesarias
import cv2
import numpy as np

maxCirculos=6
maxCirculos=maxCirculos-1

#Seleccionamos la camara que vamos a ocupar
#Significa la primer camara o la seleccionada por default
video = cv2.VideoCapture(0)

while True:
	#Grabamos los frames en la varible ret, frame
    ret, frame = video.read()
    
    #Se aplica una escala de grises a la imagen que estamos grabando
    #En una siguiente version probablemente se aplique un filtro HSV
    framegrey1 = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    
    #mostramos lo que esta viendo la camara en escala de grises
    cv2.imshow("Original", framegrey1)
    
    #Informacion sobre las siguientes lineas:
    #http://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html
    """
    En el nucleo gaussiano se debe especificar el ancho y la altura del kernel que debe ser positivo y impar. 
    Tambien se debe especificar la desviacion estandar en direccion X e Y, sigmaX y sigmaY respectivamente. 
    Si solo se especifica sigmaX, sigmaY se toma igual que sigmaX. 
    Si ambos se dan como ceros, se calculan a partir del tamano del nucleo.
    Este metodo es muy eficaz en la eliminacion de ruido de la imagen.
    """
    #Python: cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]])
    gray = cv2.GaussianBlur(framegrey1, (1,1), 2)
    #cv2.imshow("GaussianBlur", gray)
    
    """
    La funcion cv2.medianBlur toma la mediana de todos los pixeles bajo el area del kernel y el elemento central se sustituye por este valor mediano. 
    Esto es muy eficaz contra el ruido en las imagenes.
    Lo interesante es que el elemento central es un valor recien calculado que puede ser un valor de pixel en la imagen o un nuevo valor.
    Pero en el desenfoque mediano, el elemento central siempre es reemplazado por algun valor de pixel en la imagen.
    Reduce el ruido de manera efectiva. Su tamano de nucleo debe ser un numero entero impar positivo.
    """
    
    gray = cv2.medianBlur(gray,5)
    #cv2.imshow("medianBlur", gray)
	
    # La funcion transforma la imagen en escala de grises a una imagen binaria
    #cv.AdaptiveThreshold(src, dst, maxValue, adaptive_method=CV_ADAPTIVE_THRESH_MEAN_C, thresholdType=CV_THRESH_BINARY, blockSize=3, param1=5) 
    gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
		        cv2.THRESH_BINARY,19,3)
    #cv2.imshow("adaptiveThreshold", gray)
    
    #Se crea el kernel que se utilizara para la funcion erode y dilate
    kernel = np.ones((2.6,2.7),np.uint8)
	#Erosion quita la estructura de pixeles de la capa mas externa
	#Dilation agrega pixeles a la estructura de la capa mas externa
    gray = cv2.erode(gray,kernel,iterations = 1) 
    gray = cv2.dilate(gray,kernel,iterations = 1)
    #cv2.imshow("ErodeAndDilate", gray)
    
    #DETECCION DE CIRCULOS
    """
    fuente: http://www.pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/
    
    image: 8-bit, single channel image. If working with a color image, convert to grayscale first.

	method: Defines the method to detect circles in images. Currently, the only implemented method is cv2.HOUGH_GRADIENT,
	which corresponds to the Yuen et al. paper.

	dp: This parameter is the inverse ratio of the accumulator resolution to the image resolution (see Yuen et al. for more details). 
	Essentially, the larger the dp gets, the 	smaller the accumulator array gets.
	
	minDist: Minimum distance between the center (x, y) coordinates of detected circles. If the minDist is too small, multiple circles in the same neighborhood as the original 	may be (falsely) detected. If the minDist is too large, then some circles may not be detected at all.

	param1: Gradient value used to handle edge detection in the Yuen et al. method.
	
	param2: Accumulator threshold value for the cv2.HOUGH_GRADIENT method. The smaller the threshold is, 
	the more circles will be detected (including false circles). The larger the threshold is, the more circles will potentially be returned.
	
	minRadius: Minimum size of the radius (in pixels).
	
	maxRadius: Maximum size of the radius (in pixels).
    """
    circles =  cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 10, np.array([]), 40, 80, 5, 100)
    
    #DIBUJAMOS LOS CIRCULOS EN LOS ENCONTRADOS EN FRAME
    #DIBUJARA SOLAMENTE EL MAXIMO DE CIRCULOS PERMITIDO
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
