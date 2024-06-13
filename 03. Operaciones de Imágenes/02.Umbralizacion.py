import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Image/chowder.jpg")
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
#Convertimos a escala de grises
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Crear matríz
matriz = np.ones(imgGray.shape, dtype='uint8') * 50

#Brillo
brilloGray = cv2.add(imgGray, matriz)

#Threshold Brillante
_, imgThreshold = cv2.threshold(brilloGray, 160, 255, cv2.THRESH_BINARY) #Valores que no superen 160 se convierten en 0 y los que lo superan se convierten en 255
_, imgThreshold2 = cv2.threshold(brilloGray, 160, 255, cv2.THRESH_BINARY_INV) #Valores que superen 160 se convierten en 0 y los que no lo superan se convierten en 255

#Threshold Adaptative Brillante
imgThresholdAdaptiveBrillante = cv2.adaptiveThreshold(brilloGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,7)

#Threshold Oscuro
oscuroGray = cv2.subtract(imgGray, matriz)
_, imgThreshold3 = cv2.threshold(oscuroGray, 160, 255, cv2.THRESH_BINARY) #Valores que no superen 160 se convierten en 0 y los que lo superan se convierten en 255
_, imgThreshold4 = cv2.threshold(oscuroGray, 160, 255, cv2.THRESH_BINARY_INV) #Valores que superen 160 se convierten en 0 y los que no lo superan se convierten en 255

#Threshold Adaptative
imgThresholdAdaptiveOscuro = cv2.adaptiveThreshold(oscuroGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11,7)

#Figura
fig = plt.figure()
ax1 = fig.add_subplot(2,4,1)
ax1.imshow(brilloGray, cmap='gray')
ax1.set_title('Brillo')

ax2 = fig.add_subplot(2,4,2)
ax2.imshow(imgThreshold, cmap='gray')
ax2.set_title('Brillante Threshold')

ax3 = fig.add_subplot(2,4,3)
ax3.imshow(imgThreshold2, cmap='gray')
ax3.set_title('Brillante Threshold Inv')

ax4 = fig.add_subplot(2,4,4)
ax4.imshow(imgThresholdAdaptiveBrillante, cmap='gray')
ax4.set_title('Brillante Adaptive')

ax5 = fig.add_subplot(2,4,5)
ax5.imshow(oscuroGray, cmap='gray')
ax5.set_title('Oscuro')

ax6 = fig.add_subplot(2,4,6)
ax6.imshow(imgThreshold3, cmap='gray')
ax6.set_title('Oscuro Threshold')

ax7 = fig.add_subplot(2,4,7)
ax7.imshow(imgThreshold4, cmap='gray')
ax7.set_title('Oscuro Threshold Inv')

ax8 = fig.add_subplot(2,4,8)
ax8.imshow(imgThresholdAdaptiveOscuro, cmap='gray')
ax8.set_title('Oscuro Adaptive')

plt.show()
