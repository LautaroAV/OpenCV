import cv2
import numpy as np
import matplotlib.pyplot as plt

img = 100 * np.ones((10,10,3), np.uint8) 
img2 = 100 * np.ones((10,10,3), np.uint8)

#Modificar canal Rojo
img[4,5,0] = 255
img[4,4,0] = 0
img[5,5,0] = 255
img[5,5,0] = 0
#Modificar canal Verde
img[4,5,1] = 0
img[4,4,1] = 255
img[5,5,1] = 0
img[5,5,1] = 255
#Modificar canal Azul
img[4,5,2] = 255
img[4,4,2] = 255
img[5,5,2] = 0
img[5,5,2] = 0

#Recorte
#El primer valor corresponde a las columnas (Vertical)
#El segundo valor corresponde a las filas (Horizontal)
imgRecortada = img[4:8, 4:6]

#Mostrar canales
figura = plt.figure()

#Imagen Original
ax1 = figura.add_subplot(2,2,1)
ax1.imshow(img, cmap='gray')
ax1.set_title('Imagen original')

#Imagen Recortada
ax2 = figura.add_subplot(2,2,2)
ax2.imshow(imgRecortada, cmap='gray')
ax2.set_title('Imagen Recortada')

#Mostrar matríz
plt.show()