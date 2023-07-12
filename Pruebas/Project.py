import numpy as np
import cv2
import imutils
import torch

#Cam
cap = cv2.VideoCapture(0)
model = torch.hub.load('ultralytics/yolov5','custom',path='D:/Universidad/Proyecto de grado/YoloDetect3.0/plastic_2.pt')


while True:
    ret, frame = cap.read()

    #realizamos detección
    detect = model(frame)
    coord = detect.xyxy[0].numpy()
    porcent = coord[:,4]
    print(coord)
    print(porcent)

    if len(porcent)>1:
        maximo = max(porcent)
        ptx = porcent.tolist()
        pos = ptx.index(maximo)
        datoxy = coord[pos]
        print("El mayor porcentaje es: ", maximo)
        print("El coord de la botella: ", datoxy)
    else:
        maximo = porcent
        datoxy = coord
        print("El porcentaje: ", maximo)
        print("El coord es: ", datoxy)

                
    cv2.imshow('Detector de Botellas', np.squeeze(detect.render()))    
    k = cv2.waitKey(1)
    if k==27:
        break

cap.realese()
cv2.destroyAllWindows
        
