import cv2
import numpy as np
import matplotlib.pyplot as plt

#Imagen RGB
img = 100 * np.ones((10,10,3), np.uint8) 

#Extraer Matrices (canales)
Red = img[:,:,0]
Green = img[:,:,1]
Blue = img[:,:,2]

#Modificar canales
Red[:,:] = 0


#Mostrar matríz
plt.imshow(img,cmap='gray')
plt.show()