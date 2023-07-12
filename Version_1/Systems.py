import numpy as np
import cv2
import imutils
import time

def PruebaSystem1(frame,model):
    lab = cv2.cvtColor(frame, cv2.COLOR_RGB2LAB)
    plastic = np.array([[65,0,0],[170,255,255]])
    mask = cv2.inRange(lab,plastic[0],plastic[1])
    area = np.count_nonzero(mask)
    #print('El area de plastico detectada es:', area)
    cv2.imshow('Systema 1',mask)
    detect = model(frame)
    coord = detect.xyxy[0].numpy()
    cv2.imshow('Detector de Botellas System1', np.squeeze(detect.render()))
    if coord.size != 0:
        return area
    else:
        return 0

def PruebaSystem2(frame, model, prom):
    #Crear los rangos de color
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    yellow = np.array([[0,12,114],[179,76,178]])
    red = np.array([[166,60,50],[214,255,255]])
    green = np.array([[40,39,54],[94,255,255]])
    blue = np.array([[40,99,128],[162,255,255]])
    trans = np.array([[34,34,56],[234,176,165]])
    black = np.array([[95,31,14],[117,92,93]])
    malt = np.array([[0,21,59],[44,252,205]])
    
    detection = model(frame)
    cv2.imshow('Detector de Botellas System2', np.squeeze(detection.render()))
    coord = detection.xyxy[0].numpy()
    size = coord.size
    if size != 0:
        coord = [round(e) for e in coord[0][0:4]]
        crop = hsv[coord[1]:coord[3],coord[0]:coord[2]]
        maskYellow = cv2.inRange(crop,yellow[0],yellow[1])
        countYellow = np.count_nonzero(maskYellow)
        maskRed = cv2.inRange(crop,red[0],red[1])
        countRed = np.count_nonzero(maskRed)
        maskGreen = cv2.inRange(crop,green[0],green[1])
        countGreen = np.count_nonzero(maskGreen)
        maskBlue = cv2.inRange(crop,blue[0],blue[1])
        countBlue = np.count_nonzero(maskBlue)
        maskTrans = cv2.inRange(crop,trans[0],trans[1])
        countTrans = np.count_nonzero(maskTrans)
        maskBlack = cv2.inRange(crop,black[0],black[1])
        countBlack = np.count_nonzero(maskBlack)
        maskMalt = cv2.inRange(crop,malt[0],malt[1])
        countMalt = np.count_nonzero(maskMalt)
        
        #cv2.imshow('Camara2',crop)
        
        if (countYellow >= crop.size * 0.1) & (prom >= 250):
            print('Plastico Amarillo Detectado')
        if (countRed >= crop.size * 0.1) & (prom >= 250):
            print('Plastico Rojo Detectado')
        if (countGreen >= crop.size * 0.1) & (prom >= 250):
            print('Plastico Verde Detectado')
        if (countBlue >= crop.size * 0.1) & (prom >= 250):
            print('Plastico Azul Detectado')
        if (countTrans >= crop.size * 0.1) & (prom >= 250):
            print('Plastico Transparente Detectado')        
        if (countBlack >= crop.size * 0.1) & (prom >= 250):
            print('Plastico Negro Detectado')    
        if (countMalt >= crop.size * 0.1) & (prom >= 250):
            print('Plastico Malta Detectado')

def System1_Funct(frame2):

    #print("**Bottle Detected**")
    hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
    plastic = np.array([[0,12,100],[179,76,190]])
    cntsPlastic = imutils.grab_contours(cv2.findContours(cv2.inRange(hsv,plastic[0],plastic[1]),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE))
    for c in cntsPlastic:
        area1 = cv2.contourArea(c)
        if area1>200:
            cv2.drawContours(frame2,[c],-1,(255,0,0),3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            cv2.circle(frame2,(cx,cy),7,(255,255,255),-1)
            cv2.putText(frame2,"Plasti: "+str(area1),(cx-20,cy-20),cv2.FONT_ITALIC,2,(255,255,255),2)
            return 1
        else:
            return 0

def System2_Funct(window,cap,model,seg):
#def System2_Funct(window,cap,cond):
    ret, frame = cap.read()
    if cond:
        #coord = [round(e) for e in coord [0][0:4]]
        #crop = frame[coord[1]:coord[3],coord[0]:coord[2]]
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #percen = 0.1 #Variable para determinar la cantidad de area a mostrar según el area del frame de entrada
        #Crear los rangos de color
        cant_cont = 3000
        yellow = np.array([[0,12,114],[179,76,178]])
        red = np.array([[0,50,160],[10,255,255]])
        green = np.array([[40,78,80],[70,255,255]])
        blue = np.array([[38,93,133],[179,255,255]])
        trans = np.array([[144,2,133],[179,28,255]])
        black = np.array([[95,31,14],[117,92,93]])
        malt = np.array([[0,21,59],[44,252,205]])
        #Encontrar Contornos
        cntrsYellow = imutils.grab_contours(cv2.findContours(cv2.inRange(hsv,yellow[0],yellow[1]),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE))
        cntrsRed = imutils.grab_contours(cv2.findContours(cv2.inRange(hsv,red[0],red[1]),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE))
        cntrsGreen = imutils.grab_contours(cv2.findContours(cv2.inRange(hsv,green[0],green[1]),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE))
        cntrsBlue = imutils.grab_contours(cv2.findContours(cv2.inRange(hsv,blue[0],blue[1]),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE))
        cntrsTrans = imutils.grab_contours(cv2.findContours(cv2.inRange(hsv,trans[0],trans[1]),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE))
        cntrsBlack = imutils.grab_contours(cv2.findContours(cv2.inRange(hsv,black[0],black[1]),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE))
        cntrsMalt = imutils.grab_contours(cv2.findContours(cv2.inRange(hsv,malt[0],malt[1]),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE))
        #Dibujar los contornos
        for c in cntrsYellow:
            area1 = cv2.contourArea(c)
            if area1>cant_cont:
                #cv2.drawContours(crop,[c],-1,(30,255,255),3)
                #port.write(b'a')
                print("Plastico Amarillo Detectado")
        for c in cntrsRed:
            area2 = cv2.contourArea(c)
            if area2>cant_cont:
                #cv2.drawContours(crop,[c],-1,(0,0,255),3)
                #port.write(b'b')
                print("Plastico Rojo Detectado")
        for c in cntrsGreen:
            area3 = cv2.contourArea(c)
            if area3>cant_cont:
                #cv2.drawContours(crop,[c],-1,(255,0,0),3)
                #port.write(b'c')
                print("Plastico Verde Detectado")
        for c in cntrsBlue:              
            area4 = cv2.contourArea(c)
            if area4>cant_cont:
                #cv2.drawContours(crop,[c],-1,(255,0,0),3)
                #port.write(b'd')
                print("Plastico Azul Detectado")                    
        for c in cntrsTrans:              
            area5 = cv2.contourArea(c)
            if area5>cant_cont:
                #cv2.drawContours(crop,[c],-1,(170,165,170),3)
                #port.write(b'e')
                print("Plastico Transparente Detectado")                   
        for c in cntrsBlack:                
            area6 = cv2.contourArea(c)
            if area6>cant_cont:
                #cv2.drawContours(crop,[c],-1,(170,165,170),3)
                #port.write(b'f')
                print("Plastico Negro Detectado")                   
        for c in cntrsMalt:               
            area7 = cv2.contourArea(c)
            if area7>cant_cont:
                #cv2.drawContours(crop,[c],-1,(3,48,131),3)
                #port.write(b'g')
                print("Plastico Malta Detectado")
        cv2.imshow('Detection',frame)                           
    elif window:           
        cv2.destroyWindow('Detection'); window = False
