import torch
import cv2
import threading
import NewFunctions as NF

model_3 = torch.hub.load('ultralytics/yolov5','custom',path='C:/Users/sergi/OneDrive/Documentos/Sergio/Universidad/Tesis/Tesis_Codes/code_model/model/plastic_3.pt')
model_v5l = torch.hub.load('ultralytics/yolov5','custom',path='C:/Users/sergi/OneDrive/Documentos/Sergio/Universidad/Tesis/Tesis_Codes/code_model/model/bestv5l.pt')

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)

hilo_S1 = threading.Thread(target=NF.System1, args=(cap1,model_3))
hilo_SIR = threading.Thread(target=NF.SystemIR, args=(cap0,))
hilo_S2 = threading.Thread(target=NF.System2, args=(cap2,model_v5l))
hilo_S1.start()
hilo_SIR.start()
hilo_S2.start()
hilo_S1.join()
hilo_SIR.join()
hilo_S2.join()

