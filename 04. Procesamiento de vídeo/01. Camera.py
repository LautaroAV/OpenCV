import cv2

#Captura de vídeo
capture = cv2.VideoCapture(2)

#Ciclo para ejecutar los frames del vídeo
while True:
    #Leer los fotogramas
    ret, frame = capture.read()
    print (ret)
    
    #Mostrar los frames del vídeo
    cv2.imshow("Webcam", frame)
    
    #Terminar la ejecucición con una tecla
    waitKey = cv2.waitKey(1)
    if waitKey == ord('q'): #Con la tecla q
        break

#Libera los recursos del objeto de captura de video
capture.release()
#Cerrar la ventana
cv2.destroyAllWindows()


