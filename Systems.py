import numpy as np
import cv2
import imutils
import time

def System1_Funct(frame):

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    plastic = np.array([[0,12,114],[179,76,178]])
    cntsPlastic = imutils.grab_contours(cv2.findContours(cv2.inRange(hsv,plastic[0],plastic[1]),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE))
    for c in cntsPlastic:
        area1 = cv2.contourArea(c)
        if area1>200:
            cv2.drawContours(frame,[c],-1,(255,0,0),3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
            cv2.putText(frame,"Plasti: "+str(area1),(cx-20,cy-20),cv2.FONT_ITALIC,2,(255,255,255),2)
            return True

def System2_Funct(window,cap,model,port,min):
    
    end = time.time() + 60*min
    while time.time() >= end:
        ret, frame = cap.read()
        detect = model(frame)
        coord = detect.xyxy[0].numpy()
        if coord.size != 0:
            coord = [round(e) for e in coord [0][0:4]]
            crop = frame[coord[1]:coord[3],coord[0]:coord[2]]
            hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
            percen = 0.1 #Variable para determinar la cantidad de area a mostrar según el area del frame de entrada
            #Crear los rangos de color
            yellow = np.array([[0,12,114],[179,76,178]])
            red = np.array([[0,50,160],[10,255,255]])
            green = np.array([[40,78,80],[70,255,255]])
            blue = np.array([[90,60,0],[121,255,255]])
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
                if area1>frame.size*percen:
                    cv2.drawContours(frame,[c],-1,(30,255,255),3)
                    port.write(b'a')
                    print("Plastico Amarillo Detectado")
            for c in cntrsRed:
                area2 = cv2.contourArea(c)
                if area2>frame.size*percen:
                    cv2.drawContours(frame,[c],-1,(0,0,255),3)
                    port.write(b'b')
                    print("Plastico Rojo Detectado")
            for c in cntrsGreen:
                area3 = cv2.contourArea(c)
                if area3>frame.size*percen:
                    cv2.drawContours(frame,[c],-1,(255,0,0),3)
                    port.write(b'c')
                    print("Plastico Verde Detectado")
            for c in cntrsBlue:              
                area4 = cv2.contourArea(c)
                if area4>frame.size*percen:
                    cv2.drawContours(frame,[c],-1,(255,0,0),3)
                    port.write(b'd')
                    print("Plastico Azul Detectado")                    
            for c in cntrsTrans:              
                area5 = cv2.contourArea(c)
                if area5>frame.size*percen:
                    cv2.drawContours(frame,[c],-1,(170,165,170),3)
                    port.write(b'e')
                    print("Plastico Transparente Detectado")                   
            for c in cntrsBlack:                
                area6 = cv2.contourArea(c)
                if area6>frame.size*percen:
                    cv2.drawContours(frame,[c],-1,(170,165,170),3)
                    port.write(b'f')
                    print("Plastico Negro Detectado")                   
            for c in cntrsMalt:               
                area7 = cv2.contourArea(c)
                if area7>frame.size*percen:
                    cv2.drawContours(frame,[c],-1,(3,48,131),3)
                    port.write(b'g')
                    print("Plastico Malta Detectado")                    
            cv2.imshow('Detection',crop); window = True           
        elif window:           
            cv2.destroyWindow('Detection'); window = False