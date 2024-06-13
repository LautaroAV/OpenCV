import cv2
import numpy as np
import matplotlib.pyplot as plt

#Leer la imagen
img = cv2.imread("Image\chowder.jpg") #1 = 3 canales RGB (3 matríz)

#Recortar imagen
#El primer valor corresponde a las columnas (Vertical)
#El segundo valor corresponde a las filas (Horizontal)
imgRecortada = img[130:243, 88:320]

#Mostrar recorte
cv2.imshow("Imagen original", img)
cv2.imshow("Imagen recortada", imgRecortada)

#Mostrar matríz
plt.imshow(img,cmap='gray')
plt.show()

