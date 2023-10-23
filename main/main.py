# importar librerias
import torch
import cv2
import threading
import NewFunctions as NF
import serial

# importar modelos yolo
model_3 = torch.hub.load('ultralytics/yolov5','custom',path='C:/Users/sergi/OneDrive/Documentos/Sergio/Universidad/Tesis/Tesis_Codes/code_model/model/plastic_3.pt')
model_v5l = torch.hub.load('ultralytics/yolov5','custom',path='C:/Users/sergi/OneDrive/Documentos/Sergio/Universidad/Tesis/Tesis_Codes/code_model/model/bestv5l.pt')

# apertura de puerto serial
uno = serial.Serial('COM3', 9600, timeout = 1)

# captura de video de las cámaras
cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)

# llamado de funciones utilizando threading
hilo_S1 = threading.Thread(target=NF.System1, args=(cap0,model_3,uno))
hilo_SIR = threading.Thread(target=NF.SystemIR, args=(cap1,uno))
hilo_S2 = threading.Thread(target=NF.System2, args=(cap2,model_v5l,uno))

# inicio de hilos asignados para cada funcion
hilo_S1.start()
hilo_SIR.start()
hilo_S2.start()

# finalización de hilos
hilo_S1.join()
hilo_SIR.join()
hilo_S2.join()

# cierre de puerto serial
uno.close()
