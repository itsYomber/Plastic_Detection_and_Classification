import numpy as np
import cv2
#import imutils
import torch

#Cam
cap = cv2.VideoCapture(0)
model = torch.hub.load('ultralytics/yolov5','custom',path='C:/Users/sergi/OneDrive/Documentos/Sergio/Universidad/Tesis/Tesis_Codes/code_model/model/plastic_2.pt')


while True:
    ret, frame = cap.read()

    #realizamos detección
    detect = model(frame)
    coord = detect.xyxy[0].numpy()
    porcent = coord[:,4]
    print(coord)

    for data in porcent:
        if data>0.6:
            print('bottle detect')
            print(data)

    cv2.imshow('Detector de Botellas', np.squeeze(detect.render()))    
    k = cv2.waitKey(1)
    if k==27:
        break

cap.realese()
cv2.destroyAllWindows