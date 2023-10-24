# Plastic_Detection_and_Classification
#Readme.
#/AuxiliarCodes
  ColorClass.py: Detección a tiempo real de colores en diferentes espacios, en donde trabaja de forma dinámica con Trackbards máximos y mínimos para encontrar los   
                 rangos necesarios.
  CordinatesAndCofidenceDetection: Script para la manipulación de los modelos creados en Yolo y la lógica para capturar los datos obtenidos del tensorflow e 
                                   interactuar con ellos para capturar las coordenadas y el % de confianza de los  objetos detectados a tiempo real.
  Registros.py: Script para generar un registro lógico para la información obtenida a tiempo real, esto para poder procesar y validar los datos considerados del 
                objeto.
  data_augmentation.py: Script para generar imagenes de otras imagenes cambiando y ajustanado sus propias características.

#/ArduinoTesis
  ArduinoTesis.ino: Script en arduino para la comunicación entre los scripts de python y la tarjeta arduino, esto para enviar los mandos de visualización con  
                    respecto a las validacioens de Selección de Botella, Detección de Plástico y Clasificación de Color.
#/main
  NewFunctions.py: Script en donde se encuentran los sistemas para cada etapa de la tesis, los cuales se procesan en paralelo y así capturar todo a tiempo real y 
                   disminuyendo la latencia al ejecutar las diferentes funciones.
  main.py: Script central el cual realiza el funcionamiento de las funciones del Script "NewFunctions.py" de forma paralela y tomando los variables y parámetros 
           necesarios para la ejecución en paralela de todos los scripts de este proceso.

