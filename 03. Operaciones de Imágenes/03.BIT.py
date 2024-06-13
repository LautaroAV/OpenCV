import cv2
import numpy as np
import matplotlib.pyplot as plt

#4 TIPOS
#cv2.bitwise_and(img, img2, mask), cv2.bitwise_or(), cv2.bitwise_xor(), cv2.bitwise_not()


img = cv2.imread("Image/mitad.png", 0)
img2 = cv2.imread("Image/circulo.png", 0)

#Operación and
imgAnd = cv2.bitwise_and(img, img2, mask=None)
#Operación or
imgOr = cv2.bitwise_or(img, img2, mask=None)
#Operación xor
imgXor = cv2.bitwise_xor(img, img2, mask=None)
#Operación not
imgNot = cv2.bitwise_not(img, mask=None)

figura = plt.figure()

ax1 = figura.add_subplot(2,4,1)
ax1.imshow(img, cmap="gray")
ax1.set_title("Imagen mitad")

ax2 = figura.add_subplot(2,4,2)
ax2.imshow(img2, cmap="gray")
ax2.set_title("Imagen circulo")

ax3 = figura.add_subplot(2,4,3)
ax3.imshow(imgAnd, cmap="gray")
ax3.set_title("Imagen and")

ax4 = figura.add_subplot(2,4,4)
ax4.imshow(imgOr, cmap="gray")
ax4.set_title("Imagen or")

ax5 = figura.add_subplot(2,4,5)
ax5.imshow(imgXor, cmap="gray")
ax5.set_title("Imagen xor")

plt.show()
