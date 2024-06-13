import cv2
import matplotlib.pyplot as plt

#Leer la imagen
img = cv2.imread("Image\chowder.jpg",1) #1 = 3 canales RGB (3 matríz)
#Pasar el color de BGR a RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Comando que extrae los canales automáticamente
Red, Green, Blue = cv2.split(img)

#Mostrar canales
figura = plt.figure()

#Canal Rojo
ax1 = figura.add_subplot(2,2,1)
ax1.imshow(Red, cmap='gray')
ax1.set_title('Canal Rojo')
#Canal Verde
ax2 = figura.add_subplot(2,2,2)
ax2.imshow(Green, cmap='gray')
ax2.set_title('Canal Verde')
#Canal Azul
ax3 = figura.add_subplot(2,2,3)
ax3.imshow(Blue, cmap='gray')
ax3.set_title('Canal Azul')

#Constructor
imgReconstruida = cv2.merge((Red+100,Green,Blue))

#Imagen Modificada
ax4 = figura.add_subplot(2,2,4)
ax4.imshow(imgReconstruida, cmap='gray')
ax4.set_title('Imagen Modificada')

#Guardar Imagen
cv2.imwrite("NewImage.jpg", imgReconstruida)

#Mostrar matríz
plt.show()