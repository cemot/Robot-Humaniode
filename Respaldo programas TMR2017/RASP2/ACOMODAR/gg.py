import serial


arduino = serial.Serial('/dev/ttyUSB0', 9600)

print("COMUNICACION SERIAL!")

while True:
      print("VALOR DE ARDUINO: ")
      txt=arduino.readline()
      print(txt)
      comando = raw_input('Introduce un comando: ') #Input
      arduino.write(comando) #Mandar un comando hacia Arduino
      if comando == '15':
            print('LED ENCENDIDO')
      elif comando == '250':
            print('LED APAGADO')

arduino.close() #Finalizamos la comunicacion
