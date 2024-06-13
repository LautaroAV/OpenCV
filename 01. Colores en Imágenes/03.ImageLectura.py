import cv2
import numpy as np
import matplotlib.pyplot as plt

#Leer las imágenes
imgGray = cv2.imread("Image\chowder.jpg",0) #0 = 1 canal BN (1 matríz)
imgColor = cv2.imread("Image\chowder.jpg",1) #1 = 3 canales RGB (3 matríz)
img = cv2.imread("Image\chowder.jpg")

#Información sobre la imagen
tamañoImagen = imgColor.shape
tipoDato = imgColor.dtype
print ("El tamaño de la imagen es: " + str(tamañoImagen))
print ("El tipo de dato de la imagen es: " + str(tipoDato))

#Mostrar imágenes
cv2.imshow("Gris",imgGray)
cv2.imshow("RGB", imgColor)
cv2.imshow("Img", img)

#Corregir el color
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Mostrar matríz
plt.imshow(img,cmap='gray')
plt.show()