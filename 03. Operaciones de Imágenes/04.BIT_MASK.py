import cv2
import numpy as np
import matplotlib.pyplot as plt

imgLogo = cv2.imread("Image/logo.png")
imgFondo = cv2.imread("Image/fondo.png")

#Corrección de color
imgLogo = cv2.cvtColor(imgLogo, cv2.COLOR_BGR2RGB)
imgFondo = cv2.cvtColor(imgFondo, cv2.COLOR_BGR2RGB)

#Crear máscara
logoGray = cv2.cvtColor(imgLogo, cv2.COLOR_BGR2GRAY)
_, imgThresholdGray = cv2.threshold(logoGray, 160, 255, cv2.THRESH_BINARY) #Valores que no superen 160 se convierten en 0 y los que lo superan se convierten en 255
_, imgThresholdGrayInvertido = cv2.threshold(logoGray, 160,255, cv2.THRESH_BINARY_INV)

#AND de imágenes
imgAndThr = cv2.bitwise_and(imgLogo, imgFondo, mask=imgThresholdGray)
imgAndThrInv = cv2.bitwise_and(imgLogo, imgLogo, mask=imgThresholdGrayInvertido)

figura = plt.figure()

ax1 = figura.add_subplot(2,4,1)
ax1.imshow(imgFondo)
ax1.set_title("Imagen Fondo")

ax2 = figura.add_subplot(2,4,2)
ax2.imshow(imgLogo)
ax2.set_title("Imagen Logo")

ax3 = figura.add_subplot(2,4,3)
ax3.imshow(imgThresholdGray, cmap='gray')
ax3.set_title("Imagen Mascara")

ax4 = figura.add_subplot(2,4,4)
ax4.imshow(imgThresholdGrayInvertido, cmap='gray')
ax4.set_title("Imagen Mascara Invertida")

ax5 = figura.add_subplot(2,4,5)
ax5.imshow(imgAndThr)
ax5.set_title("Imagen AND")

ax6 = figura.add_subplot(2,4,6)
ax6.imshow(imgAndThrInv)
ax6.set_title("Imagen AND Invertida")

plt.show()