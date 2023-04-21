import cv2
import torch
import Systems

model = torch.hub.load('ultralytics/yolov5','custom',path='D:/Universidad/Proyecto de grado/YoloDetec/model2/plastic_2.pt')

#Captura del vídeo
cap = []
cap[0] = cv2.VideoCapture(0)
cap[1] = cv2.VideoCapture(1)

while True:
    ret, frame = cap[0].read()
    Plastico1 = Systems.System1_Funct(frame)
    cv2.imshow("System 1",frame)
    if Plastico1 is True:
        print("Plastic Detected")
        Systems.System2_Funct(cap[1],model,5)
    k = cv2.waitKey(1)
    if k==27:
        break
cap[0].realese()
cap[1].realese()
cv2.destroyAllWindows