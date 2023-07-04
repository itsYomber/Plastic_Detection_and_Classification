import numpy as np
import cv2
import imutils 

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


def System1(cap,model):
    register = CircularBuffer(2)
    register.start(0)
    while True:
        ret, frame = cap.read()
        detection = model(frame)
        coord = detection.xyxy[0].numpy()
        porcent = coord[:,4]
        if len(porcent)>1:
            maximo = max(porcent)
        else:
            maximo = porcent
        register.insert(maximo)
        elements = register.get_elements()
        prom = sum(elements)/len(elements)
        if prom >= 0.45:
            print("----Botella Detectada----")
        else:
            print("#### Botella no Detectada ####")
            
        cv2.imshow('Detector de Botellas', np.squeeze(detection.render()))  
        k = cv2.waitKey(1)
        if k==27:
            break

    cap.release()
    cv2.destroyWindow('Detector de Botellas')
    
def SystemIR(cap):
    register = CircularBuffer(30)
    register.start(0)
    while True:
        ret, frame = cap.read()
        crop = frame[0:480,0:540]
        lab = cv2.cvtColor(crop,cv2.COLOR_BGR2LAB)
        plastic = np.array([[65,0,0],[110,255,255]])
        mask = cv2.inRange(lab,plastic[0],plastic[1])
        area = np.count_nonzero(mask)
        register.insert(area)
        elements = register.get_elements()
        prom = sum(elements)/len(elements)
        cv2.imshow('System IR',mask)        
        if prom >= 500:
            print('----Plastico Detectado----')
        else:
            print('****Plastico No Detectado****')
        k = cv2.waitKey(1)
        if k==27:
            break
    cap.release()
    cv2.destroyWindow('System IR')
    
def System2(cap,model):
    
    yellow = np.array([[0,12,114],[179,76,178]])
    red = np.array([[166,60,50],[214,255,255]])
    green = np.array([[40,39,54],[94,255,255]])
    blue = np.array([[40,99,128],[162,255,255]])
    trans = np.array([[34,34,56],[234,176,165]])
    black = np.array([[95,31,14],[117,92,93]])
    malt = np.array([[0,21,59],[44,252,205]])
    
    while True:
        ret, frame = cap.read()
        detection = model(frame)
        coord = detection.xyxy[0].numpy()
        size = coord.size
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        if size != 0:
            coord = [round(e) for e in coord[0][0:4]]
            crop = hsv[coord[1]:coord[3],coord[0]:coord[2]]
            countYellow = np.count_nonzero(cv2.inRange(crop,yellow[0],yellow[1]))
            countRed = np.count_nonzero(cv2.inRange(crop,red[0],red[1]))
            countGreen = np.count_nonzero(cv2.inRange(crop,green[0],green[1]))
            countBlue = np.count_nonzero(cv2.inRange(crop,blue[0],blue[1]))
            countTrans = np.count_nonzero(cv2.inRange(crop,trans[0],trans[1]))
            countBlack = np.count_nonzero(cv2.inRange(crop,black[0],black[1]))
            countMalt = np.count_nonzero(cv2.inRange(crop,malt[0],malt[1]))
            
            if (countYellow >= crop.size * 0.1):
                print('Plastico Amarillo Detectado')
            if (countRed >= crop.size * 0.1):
                print('Plastico Rojo Detectado')
            if (countGreen >= crop.size * 0.1):
                print('Plastico Verde Detectado')
            if (countBlue >= crop.size * 0.1):
                print('Plastico Azul Detectado')
            if (countTrans >= crop.size * 0.1):
                print('Plastico Transparente Detectado')        
            if (countBlack >= crop.size * 0.1):
                print('Plastico Negro Detectado')    
            if (countMalt >= crop.size * 0.1):
                print('Plastico Malta Detectado')
                
        cv2.imshow('Detector de Color', np.squeeze(detection.render())) 
        k = cv2.waitKey(1)
        if k==27:
            break
    cap.release()
    cv2.destroyWindow('Detector de Color')