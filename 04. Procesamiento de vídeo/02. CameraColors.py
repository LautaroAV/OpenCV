import cv2

#Captura de vídeo
capture = cv2.VideoCapture(1)

#Ciclo para ejecutar los frames del vídeo
while True:
    #Leer los fotogramas
    ret, frame = capture.read()
    print (ret)
    
    #Convertir el frame en diferentes colores
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Mostrar los frames del vídeo
    cv2.imshow("Webcam Original", frame)
    cv2.imshow("Webcam HSV", frameHSV)
    cv2.imshow("Webcam Gray", frameGray)

    #Terminar la ejecucición con una tecla
    waitKey = cv2.waitKey(1)
    if waitKey == ord('q'): #Con la tecla q
        break

#Libera los recursos del objeto de captura de video
capture.release()
#Cerrar la ventana
cv2.destroyAllWindows()


