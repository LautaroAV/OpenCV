import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Image/chowder.jpg")
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
#Convertimos a escala de grises
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Crear Matríz
matriz = np.ones(imgGray.shape, dtype='uint8') * 50
matrizRGB = np.ones(img.shape, dtype='uint8') * 50

#Aumentar el brillo RGB
brilloBGR = cv2.add(img, matrizRGB)
brilloRGB = cv2.cvtColor(brilloBGR, cv2.COLOR_BGR2RGB)

#Disminuir brillo RGB
oscuroBGR = cv2.subtract(img, matrizRGB)
oscuroRGB = cv2.cvtColor(oscuroBGR, cv2.COLOR_BGR2RGB)

#Aumentar brillo grises
brilloGray = cv2.add(imgGray, matriz)

#Disminuir brillo grises
oscuroGray = cv2.subtract(imgGray, matriz)

#Mostrar imágenes
fig = plt.figure()
#Imagen Original
ax1 = fig.add_subplot(2,3,1)
ax1.imshow(img)
ax1.set_title('Imagen Original')
#Brillo RGB
ax2 = fig.add_subplot(2,3,2)
ax2.imshow(brilloRGB)
ax2.set_title('Brillo RGB')
#Oscuro RGB
ax3 = fig.add_subplot(2,3,3)
ax3.imshow(oscuroRGB)
ax3.set_title('Oscuro RGB')
#Imagen gray
ax4 = fig.add_subplot(2,3,4)
ax4.imshow(imgGray, cmap='gray')
ax4.set_title('Imagen Gray')
#Brillo gray
ax5 = fig.add_subplot(2,3,5)
ax5.imshow(brilloGray, cmap='gray')
ax5.set_title('Brillo Gray')
#Oscuro gray
ax6 = fig.add_subplot(2,3,6)
ax6.imshow(oscuroGray, cmap='gray')
ax6.set_title('Oscuro Gray')

plt.show()