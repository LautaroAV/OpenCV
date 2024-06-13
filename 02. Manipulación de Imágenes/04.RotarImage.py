import cv2

img = cv2.imread("Image\chowder.jpg")

imgRotate = cv2.flip(img, 0) #Voltear imagen
imgRotate2 = cv2.flip(img, 1) #Efecto espejo
imgRotate3 = cv2.flip(img, -1)

cv2.imshow('Imagen original',img)
cv2.imshow('Imagen Rotada 1', imgRotate)
cv2.imshow('Imagen Rotada 2', imgRotate2)
cv2.imshow('Imagen Rotada 3', imgRotate3)

cv2.waitKey(0)