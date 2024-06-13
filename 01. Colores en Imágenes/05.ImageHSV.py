import cv2
import matplotlib.pyplot as plt

#H -> Matices de color
#S -> Saturación 
#V -> Valor del color


#Leer la imagen
img = cv2.imread("Image\chowder.jpg",1) #1 = 3 canales RGB (3 matríz)
#Pasar el color de BGR a RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#Pasar el color de RGB a HSV
imgHSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

#Comando que extrae los canales automáticamente
H,V,S = cv2.split(imgHSV)

#Mostrar canales
figura = plt.figure()

#Canal Rojo
ax1 = figura.add_subplot(2,2,1)
ax1.imshow(H, cmap='gray')
ax1.set_title('Canal H')
#Canal Verde
ax2 = figura.add_subplot(2,2,2)
ax2.imshow(V, cmap='gray')
ax2.set_title('Canal S')
#Canal Azul
ax3 = figura.add_subplot(2,2,3)
ax3.imshow(S, cmap='gray')
ax3.set_title('Canal V')

#Constructor
imgReconstruida = cv2.merge((H,V,S))

#Imagen original
ax4 = figura.add_subplot(2,2,4)
ax4.imshow(img)
ax4.set_title('Imagen original')

#Mostrar matríz
plt.show()