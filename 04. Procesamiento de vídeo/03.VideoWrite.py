#GUARDAR VIDEOS
import cv2

capture = cv2.VideoCapture(1)
ancho = int(capture.get(3))
alto = int(capture.get(4))

print ("El ancho es: " + str(ancho) + " y el alto es: " + str(alto))

#CV2 WRITER
#cv2.VideoWriter(Nombre, Codificación, FPS, Tamaño)
outAVI = cv2.VideoWriter(("VideoGuardado.avi"), cv2.VideoWriter_fourcc('M','J','P','G'), 30, (ancho,alto)) #.AVI
outMP4 = cv2.VideoWriter("VideoGuardado.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30, (ancho, alto)) #.MP4


while True:
    #Leer los fotogramas
    ret, frame = capture.read()
    #print (ret)

    #Convertir el frame en diferentes colores
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Guardar el vídeo
    outAVI.write(frameHSV) 
    outMP4.write(frame)

    #Mostrar los frames del vídeo
    cv2.imshow("Webcam Original", frame)

    #Terminar la ejecucición con una tecla
    waitKey = cv2.waitKey(1)
    if waitKey == ord('q'): #Con la tecla q
        break

#Libera los recursos del objeto de captura de video
capture.release()
#Cerrar la ventana
cv2.destroyAllWindows()