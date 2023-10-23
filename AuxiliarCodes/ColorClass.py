import numpy as np
import cv2

def nada(x):
    pass

cv2.namedWindow('Parámetros',cv2.WINDOW_GUI_NORMAL)
cv2.resizeWindow('Parámetros', 640, 300)
cv2.createTrackbar('Tonalidad Mínima','Parámetros', 0,255,nada)
cv2.createTrackbar('Tonalidad Máxima','Parámetros', 0,255,nada) #Parámetro H
cv2.createTrackbar('Pureza Mínima','Parámetros',0,255,nada)
cv2.createTrackbar('Pureza Máxima','Parámetros',0,255,nada) #Parámetro S
cv2.createTrackbar('Luminosidad Mínima','Parámetros',0,255,nada) 
cv2.createTrackbar('Luminosidad Máxima','Parámetros',0,255,nada)#Parámetro V
cv2.createTrackbar('Kernel X', 'Parámetros', 1,30,nada)
cv2.createTrackbar('Kernel Y','Parámetros',1,30,nada) #Filtro

#Captura del vídeo
cap = cv2.VideoCapture(2)

while(1):
    ret,frame = cap.read()
    #frame = frame_[0:480,0:580]
    if ret: 
        
        #Leemos los sliders
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        Rmin = cv2.getTrackbarPos('Tonalidad Mínima','Parámetros')
        Rmax = cv2.getTrackbarPos('Tonalidad Máxima','Parámetros')
        Gmin = cv2.getTrackbarPos('Pureza Mínima','Parámetros')
        Gmax = cv2.getTrackbarPos('Pureza Máxima','Parámetros')
        Bmin = cv2.getTrackbarPos('Luminosidad Mínima','Parámetros')
        Bmax = cv2.getTrackbarPos('Luminosidad Máxima','Parámetros')

        #Establecemos el rango minimo y máximo para la codificacion HSV
        color_oscuro = np.array([Rmin, Gmin, Bmin])
        color_brillante = np.array([Rmax, Gmax, Bmax])

        #Detectamos los pixeles que están dentro de los rangos
        mascara = cv2.inRange(frame,color_oscuro,color_brillante)

        #Leemos los sliders que definen las dimensiones del Kernel
        kernelx = cv2.getTrackbarPos('Kernel X', 'Parámetros')
        kernely = cv2.getTrackbarPos('Kernel Y', 'Parámetros')
        
        #Creamos el kernel para eliminar ruido
        kernel = np.ones((kernelx,kernely),np.uint8)
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE,kernel)
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN,kernel)

        #Dibujar el rectangulo de donde está el color
        #Contornos
        #contornos,_ = cv2.findContours(mascara, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        #RETR_LIST = Calcula los contornos sin jerarquia, detecte los colores que necesitamos 
        #CHAIN_APPROX_SIMPEAproximaxion de redundancia, quita pixeles redundantes

        #cv2.drawContours(frame,contornos,-1, (0,0,0),2)
        cantidad_pixeles_true = np.count_nonzero(mascara)
        print("Cantidad de píxeles True:", cantidad_pixeles_true)
        #cv2.imshow("camara 1", frame_)
        cv2.imshow("Cámara",frame)
        cv2.imshow("Máscara", mascara)
        #if cantidad_pixeles_true > 400:
        
        #    print('----Plástico detectado----')
        #else:
        
        #    print('****No Hay Plástico****')
        
        k = cv2.waitKey(5)
        if k == 27:
            cv2.destroyAllWindows()

cap.release()








