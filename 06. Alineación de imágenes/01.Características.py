import cv2
import numpy as np

img = cv2.imread("Image/cuaderno.jpg")
capture = cv2.VideoCapture(1)

while True:
    #Leer los fotogramas
    ret, frame = capture.read()
    #Convertir  a escala de grises
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    captureGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Número de puntos claves
    num_kpt = 500
    #Declaramos el objeto
    orb = cv2.ORB_create(num_kpt)
    #Extraer la información de la imagen
    keypoint1, descriptor1 = orb.detectAndCompute(imgGray, None)
    keypoint2, descriptor2 = orb.detectAndCompute(captureGray, None)

    print (descriptor1)

    #Dibujar los puntos claves
    imgDisplay = cv2.drawKeypoints(imgGray, keypoint1, outImage= np.array([]), color = (255,0,0), flags= cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    captureDisplay = cv2.drawKeypoints(captureGray, keypoint2, outImage= np.array([]), color = (255,0,0), flags= cv2.DRAW_MATCHES_FLAGS_DEFAULT)
                        
    cv2.imshow("Imagen", imgDisplay)
    cv2.imshow("Captura", captureDisplay)

    waitKey = cv2.waitKey(1)
    if waitKey == ord('q'): #Con la tecla q
        break

#Libera los recursos del objeto de captura de video
capture.release()
#Cerrar la ventana
cv2.destroyAllWindows()