#Leer o abrir un vídeo
import cv2

#Captura de vídeo
capture = cv2.VideoCapture("Video/puertasadentro1.mp4") #Se coloca la ruta del vídeo
#Obtener la velocidad de fotogramas del video
fps = capture.get(cv2.CAP_PROP_FPS)

#Ciclo para ejecutar los frames del vídeo
while True:
    #Leer los fotogramas
    ret, frame = capture.read()
    #print (ret)
    
    #Mostrar los frames del vídeo
    cv2.imshow("Webcam", frame)
    
    # Ajustar el tiempo de espera en función de la velocidad de fotogramas
    waitKey = cv2.waitKey(int(1000/fps))
    if waitKey == ord('q'): #Con la tecla q
        break

#Libera los recursos del objeto de captura de video
capture.release()
#Cerrar la ventana
cv2.destroyAllWindows()


