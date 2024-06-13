import cv2
import numpy as np
import matplotlib.pyplot as plt

#Imagen Negra
img = np.zeros((10,10,1), np.uint8) 

#Modificar elementos matríz
img[0,1] = 30
img[6,5] = 255
img[7,4] = 150
img[8,3] = 200

#Mostrar matríz
plt.imshow(img,cmap='gray')
plt.show()