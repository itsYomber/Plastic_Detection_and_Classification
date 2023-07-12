import cv2
import torch
import Systems
import serial
import time

#port = serial.Serial('COM9', 9600, timeout=1)
model = torch.hub.load('ultralytics/yolov5','custom',path='C:/Users/sergi/OneDrive/Documentos/Sergio/Universidad/Tesis/Tesis_Codes/code_model/model/plastic_3.pt')
class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0  # Índice de la posición actual para insertar nuevos elementos
        self.is_full = False
        
    def start(self, item):
        self.buffer = [item] * self.size
        self.is_full = True
        self.head = 0

    def insert(self, item):
        self.buffer[self.head] = item
        self.head = (self.head + 1) % self.size  # Avanza al siguiente índice de forma circular

        if self.head == 0:
            self.is_full = True

    def get_elements(self):
        if self.is_full:
            return self.buffer[self.head:] + self.buffer[:self.head]
        else:
            return self.buffer[:self.head]
register = CircularBuffer(5)
register.start(0)
#Captura del vídeo
window=False

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(2)

while True:
    ret, crop = cap0.read()
    ret2, frame = cap1.read()
    frame2 = crop[0:480,0:580]
    register.insert(Systems.PruebaSystem1(frame2,model))
    elements = register.get_elements()
    promedio = sum(elements)/len(elements)
    if promedio >= 200:
        print('----Plástico detectado----')
    else:
        print('****No hay plástico****')
        #Systems.System2_Funct(window,cap1,port,model,10)
    Systems.PruebaSystem2(frame,model,promedio)
    #port.write(b'')
    k = cv2.waitKey(1)
    if k==27:
        break
cap0.release()
cap1.release()
cv2.destroyAllWindows
#port.close()
