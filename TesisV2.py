import cv2
import torch
import Systems_V2
import serial

#port = serial.Serial('COM9', 9600, timeout=1)
model = torch.hub.load('ultralytics/yolov5','custom',path='D:/Universidad/Proyecto de grado/YoloDetec/model3/plastic_2.pt')

#Captura del vídeo
cap = [] ; window=False
cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(2)

while True:
    ret, crop = cap0.read()
    Plastico1 = Systems_V2.System1_Funct(crop,model)
    cv2.imshow('system1',crop)
    if Plastico1 is True:
        print("Plastic Detected")
        #Systems.System2_Funct(window,cap1,port,model,10)
    Systems_V2.System2_Funct(window,cap1,Plastico1)
    #port.write(b'')
    k = cv2.waitKey(1)
    if k==27:
        break
cap[0].realese()
cap[1].realese()
cv2.destroyAllWindows
#port.close()
