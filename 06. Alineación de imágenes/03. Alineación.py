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


    #Dibujar los puntos claves
    imgDisplay = cv2.drawKeypoints(img, keypoint1, outImage=np.array([]), color=(255, 0, 0), flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    captureDisplay = cv2.drawKeypoints(frame, keypoint2, outImage=np.array([]), color=(255, 0, 0), flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)

    #Coincidir los puntos claves
    #1. Crear un objeto comparador de descriptores
    if descriptor2 is not None:
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = matcher.match(descriptor1, descriptor2)
        #2. Ordenar la lista
        matches = sorted(matches, key=lambda x:x.distance, reverse=False)
        #3. Filtramos los resultados
        goodmatches = int(len(matches) * 0.1)
        matches = matches[:goodmatches]
        #4. Mostrar las coincidencias
        img_matches = cv2.drawMatches(img, keypoint1, frame, keypoint2, matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)


        #Calcular la homografía de la imagen
        #1. Crear listas con el tamaño total de keypoints
        if len(matches) >= 4:  # Verificar si hay suficientes coincidencias
            puntos1 = np.zeros((len(matches), 2), dtype=np.float32)
            puntos2 = np.zeros((len(matches), 2), dtype=np.float32)
            #2. Extraer los puntos
            for i, match in enumerate(matches):
                    #Puntos de imagen
                    puntos1[i, :] = keypoint1[match.queryIdx].pt
                    #Puntos de frame
                    puntos2[i, :] = keypoint2[match.trainIdx].pt
            #3. Extraer la homografía
            h, mask = cv2.findHomography(puntos2, puntos1, cv2.RANSAC)
            #4. Dibujuar la homografía
            alto, ancho, canales = img.shape
            imgPerspectiva = cv2.warpPerspective(frame, h, (ancho,alto))
        else:
             imgPerspectiva = frame
    else:
        imgPerspectiva = frame                  
    

    cv2.imshow("Imagen", imgDisplay)
    cv2.imshow("Captura", captureDisplay)
    cv2.imshow("Coincidencias", imgPerspectiva)

    waitKey = cv2.waitKey(1)
    if waitKey == ord('q'): #Con la tecla q
        break

#Libera los recursos del objeto de captura de video
capture.release()
#Cerrar la ventana
cv2.destroyAllWindows()