# Importar Librerias
import numpy as np
import cv2

# Declaración de clase CircularBuffer
class CircularBuffer:

    # Inicialización de clase
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0  # Índice de la posición actual para insertar nuevos elementos
        self.is_full = False

    # Establecimiento de primer estado
    def start(self, item):
        self.buffer = [item] * self.size
        self.is_full = True
        self.head = 0

    # Ingres de información a la clase
    def insert(self, item):
        self.buffer[self.head] = item
        self.head = (self.head + 1) % self.size  # Avanza al siguiente índice de forma circular

        if self.head == 0:
            self.is_full = True

    # Extracción de elementos dentro de la clase
    def get_elements(self):
        if self.is_full:
            return self.buffer[self.head:] + self.buffer[:self.head]
        else:
            return self.buffer[:self.head]

# Sistema de reconocimiento de botellas (captura de video, modelo Yolo, puerto serial)
def System1(cap,model,port):

    # Inicialización de Registro
    register = CircularBuffer(2)
    register.start(0)

    # Bucle para captura de video
    while True:
        ret, frame = cap.read()
        detection = model(frame)

        # Coordenadas y % de confianza de la detección
        coord = detection.xyxy[0].numpy()
        porcent = coord[:,4]
        
        # Selección de % de confianza mayor detectado en el caso de que se haya detectado mas de una botella
        if len(porcent)>1:
            maximo = max(porcent)
        else:
            maximo = porcent

        # Ingreso de % de confianza en registro
        register.insert(maximo)

        # Obtención de % de confianza promedio guardado en el registro
        elements = register.get_elements()
        prom = sum(elements)/len(elements)

        # Si el promedio de % es mayor de 0.40 se asume que es una botella y se envía información serial
        if prom >= 0.40:
            port.write(b'B')
        else:
            port.write(b'b')

        # Visualización de lo que observa la captura de video con modelo Yolo aplicado
        cv2.imshow('Detector de Botellas', np.squeeze(detection.render()))

        # Asignación de Tecla de finalización del modelo (Esc)
        k = cv2.waitKey(1)
        if k==27:
            break

    # Borrado de Ventana de Visualización
    cap.release()
    cv2.destroyWindow('Detector de Botellas')
    
def SystemIR(cap,port): #Sistema Detección de Plástico
    # Inicialización de Registro
    register = CircularBuffer(30)
    register.start(0)
    while True:
        #Captura de frame de videocam.
        ret, frame = cap.read()
        crop = frame[0:480,0:540]
        #Se establece el espacio de trabajar
        lab = cv2.cvtColor(crop,cv2.COLOR_BGR2LAB)
        #Agregamos el rango que valida si el objeto que se captura es de plástico
        plastic = np.array([[65,0,0],[110,255,255]])
        #Se toma todos los pixeles que se encuentran en el rango establecido.
        mask = cv2.inRange(lab,plastic[0],plastic[1])
        area = np.count_nonzero(mask)
        register.insert(area) #Los pixeles capturados se ingresan en el registro
        elements = register.get_elements()
        #Se toma el porcentaje de pixeles que se toman en el determinado tiempo que el objeto pasó por el sistema
        prom = sum(elements)/len(elements)
        cv2.imshow('System IR',mask)
        #Se realiza la validación de si el frame en el lapso capturado tiene pixeles del rango del plástico.
        if prom >= 500:
            port.write(b'p') #Se envía la orden a la comunicación serial de que el objeto es de plástico.
        else:
            port.write(b'P') #Se envía la orden a la comunicación serial de que el objeto no contiene plástico.
        k = cv2.waitKey(1)
        if k==27:
            break
    cap.release()
    cv2.destroyWindow('System IR')
    
def System2(cap,model,port): #Clasificación de Color

    #Se definen los rangos para la detección de color en cada frame de la videocámara.
    yellow = np.array([[19,83,211],[35,145,248]])#Checked
    red = np.array([[160,30,120],[179,255,255]]) #Checked
    green = np.array([[50,117,93],[101,247,240]])#Checked
    blue = np.array([[76,92,171],[188,255,255]])#Checked
    trans = np.array([[60,7,84],[220,29,174]])#Checked
    malt = np.array([[0,65,0],[11,240,150]]) #Checked
    white = np.array([[215,215,216],[252,255,240]]) #Checked

    while True:
        #Se lee los datos de cada frame de la videocámara a tiempo real
        ret, frame = cap.read()
        #Se inicializa el modelo YoloV5L para la detección del objeto en la detect box.
        detection = model(frame)
        coord = detection.xyxy[0].numpy() #Se captura las coordenadas de los objetos detectados
        size = coord.size #Se toma las coordenadas como el subframe para realizar la clasificación de color.
        porcent = coord[:,4]
        #Se trabaja con dos espacios de color, esto para que el Blanco no intervenga en iluminación para el HSV
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #Para la detección de los colores a excepción del blanco.
        rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #Para la detección de color blanco.
        if size != 0: #Si el modelo detectó botella
            print('botella')
            coord = [round(e) for e in coord[0][0:4]]
            #Las coordenadas tomadas generan el subframe, esto para que no tome espacios en donde no se encuentre la botella
            crop = hsv[coord[1]:coord[3],coord[0]:coord[2]]
            crop_ = rgb[coord[1]:coord[3],coord[0]:coord[2]]
            #Al realizar de esta forma, el sistema solo se basa en la caja de detección del modelo YoloV5L garantizando que solo se capture el color de la botella
            #También evita el problema de los diferentes tamaños de botellas y etiquetadas que pueden tener.

            #Se crea un diccionario en el que determina la cantidad de pixeles que se encuentran en el subframe para cada color a detectar
            diccionario_colores= {
            "countYellow": np.count_nonzero(cv2.inRange(crop,yellow[0],yellow[1])),
            "countRed" : np.count_nonzero(cv2.inRange(crop,red[0],red[1])),
            "countGreen" : np.count_nonzero(cv2.inRange(crop,green[0],green[1])),
            "countBlue" : np.count_nonzero(cv2.inRange(crop,blue[0],blue[1])),
            "countTrans" : np.count_nonzero(cv2.inRange(crop,trans[0],trans[1])),
            "countMalt" : np.count_nonzero(cv2.inRange(crop,malt[0],malt[1])),
            "countWhite" : np.count_nonzero(cv2.inRange(crop_,white[0],white[1]))
            }
            
            #Se captura el elemento del diccionario el cual tenga mayor pixeles.
            ArrayColor = max(diccionario_colores.items(),key=lambda x: x[1])
            Color = ArrayColor[0]

            #Se realiza la visualización del sistema dependiendo de la clave del elemento/valor con mayor cantidad de pixeles.
            if Color == "countYellow" or Color == "countRed" or Color == "countBlue":
                #Se realiza la validación de cuál clave es la clave para realizar la comunicación serial al arduino y dar visiblidad si pertenece al grupo de botellas.
                #Si se encuentra que la botella tiene mayor pixeles de Amarillo, Rojo o Azul, se considera en el grupo de botellas de color.
                print('Color')
                port.write(b'c')
            elif Color == "countGreen":
                #Si encuentra que la botella contiene una mayor cantidad de pixeles verdes, se considera en el grupo de botellas Verdes.
                print('Green')
                port.write(b'g')
            elif Color == "countTrans":
                #Si encuentra que la botella contiene una mayor cantidad de pixeles transaparentes, se considera en el grupo de botellas PET/Transparente
                print('Trans')
                port.write(b't')           
            elif Color == "countM alt":
                #Si encuentra que la botella contiene una mayor cantidad de pixeles malta, se considera en el grupo de botellas de malta.
                print('Malt')
                port.write(b'm')
            elif Color == "countWhite":
                #Si encuentra que la botella contiene una mayor cantidad de pixeles blancos, se considera en el grupo de botellas HDPE/Blancas
                print('White')
                port.write(b'w')
        else:
            port.write(b'o')    
        #Se visualiza el objeto que detectó el modelo de YoloV5L y la región a la que se le hará la detección y validación de pixeles de color.
        cv2.imshow('Detector de Color', np.squeeze(detection.render())) 
        k = cv2.waitKey(1)
        if k==27:
            break
    cap.release()
    cv2.destroyWindow('Detector de Color')
