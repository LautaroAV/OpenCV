import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Image\chowder.jpg")

#Para redimensionar -> cv2.resize (imagen, outimg, fx, fy, interpolation)

#Redimensionar1
red = cv2.resize(img, None, fx=1.5, fy=1.5)
#Redimensionar2
red2 = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA) #Interpolación en área
#Redimensionar3
red3 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC) #Interpolación cúbica
#Redimensionar4
altura = 500
ancho = 500
tam = (altura, ancho)
red4 = cv2.resize(img, tam, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

cv2.imshow('Imagen original',img)
cv2.imshow('Redimensionamiento 1', red)
cv2.imshow('Redimensionamiento 2', red2)
cv2.imshow('Redimensionamiento 3', red3)
cv2.imshow('Redimensionamiento 4', red4)

cv2.waitKey(0)
