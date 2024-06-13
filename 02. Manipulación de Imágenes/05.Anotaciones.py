import cv2

img = cv2.imread("Image/anime.png")

#Redimensionar
red = cv2.resize(img, None, fx=1.5, fy=1.5)

#Línea
# cv2.line(imagen, punto1(x,y), punto2(x,y), color, grosorLinea(thickness), tipolinea(linetype))
Linea = cv2.line(red, (int(663), int(959)), (int(1149),int(959)), (0,255,0), thickness=2, lineType=cv2.LINE_AA)

#Circulo
# cv2.circle(imagen, punto1(x,y), radio, color, grosorLinea(thickness), tipolinea(linetype))
Circulo = cv2.circle(red, (int(1479), int(550)), 100, (0,0,255), thickness=3, lineType=cv2.LINE_AA)

#Rectángulo
# cv2.rectangle(imagen, punto1(x,y), punto2, color, grosorLinea(thickness), tipolinea(linetype))
Rectangulo = cv2.rectangle(red, (687,289,250,180), (255,0,0), thickness=6, lineType=cv2.LINE_AA)

#Texto
# cv2.putText(img, texto, punto(x,y), tipoLetra, tamañoLetra, color, grosorLinea(thickness), tipolinea(linetype))
Texto = cv2.putText(red,"Prueba de texto", (770,100), cv2.FONT_ITALIC, 1.1, (255,255,255), thickness=2, lineType=cv2.LINE_AA)

cv2.imshow('Imagen original',red)
cv2.waitKey(0)

