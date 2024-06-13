import cv2
import numpy as np
import sys

#Modos de ejecución
#captureVideo = 0--> #Captura de vídeo
#filtroDesenfoque = 1--> #Filtro de desenfoque
#filtroEsquinas = 2--> #Filtro de detector de esquinas
#filtroBordes = 3--> #Filtro de bordes

#Parametros esquinas
paramEsquinas = dict(maxCorners= 500, #Máximo de números de esquinas por detectar
                     qualityLevel = 0.2, #Umbral mínimo para la detección
                     minDistance = 15, #Distancia entre pixeles
                     blockSize = 9) #Área de pixeles

Modo = ord('0')

#Captura de vídeo
capture = cv2.VideoCapture(1)

while True:
    ret, frame = capture.read()

    #Elegir el modo
    if Modo == ord('0'):
        resultado = frame
    #Desenfoque
    elif Modo == ord('1'):
        resultado = cv2.blur(frame, (13,13))
    #Bordes
    elif Modo == ord('2'):
        resultado = cv2.Canny(frame, 135, 150) #Umbral superior e inferior
    # #Esquinas
    elif Modo == ord('3'):
        resultado = frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        esquinas = cv2.goodFeaturesToTrack(gray, **paramEsquinas)

        #If para ver si detecta esquinas con las características pasadas a través del parametro
        if esquinas is not None:
            for x,y in np.float32(esquinas).reshape(-1,2):
                #Convertir en entero
                x,y = int(x),int(y)
                #Dibujar la ubicación de las esquinas
                cv2.circle(resultado, (x,y), 10, (0,0,255), 1)
    
    #Mostrar los frames del vídeo
    cv2.imshow("Webcam", resultado)

    #Terminar la ejecucición con una tecla
    waitKey = cv2.waitKey(1)
    if waitKey == ord('q'): #Con la tecla q
        break
    elif waitKey != -1:
        Modo = waitKey

#Libera los recursos del objeto de captura de video
capture.release()
#Cerrar la ventana
cv2.destroyAllWindows()
 