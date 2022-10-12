""""
Integrantes:

Arce Montoya José Antonio
Garcia Gutierrez Josue Ramón
Navarrete Solano Cristian Osbaldo
Segoviano Sanchez Miguel Angel

"""


import numpy as np
import cv2
import math

color = (255,0,0)
color2 = (0,0,0)


puntos = np.array([[500,100],[500,150],[550,150],[550,100]])
puntosR= np.array([[500,100],[500,150],[550,150],[550,100]])


isClosed = True

centro_de_rotacion = [500,100]

def rotacionImagen(angulo, centro_de_rotacion):

    imagen = np.zeros((1000,1000,3), np.uint8)

    for i in range(4):
        rectangleImage = cv2.polylines(imagen, [puntos], True, color2, 3)
        puntos[i][0] = (centro_de_rotacion[0]+((puntosR[i][0]-centro_de_rotacion[0])*math.cos(math.radians(angulo))))-(((puntosR[i][1]-centro_de_rotacion[1])*math.sin(math.radians(angulo))))
        puntos[i][1] = (centro_de_rotacion[1]+((puntosR[i][1]-centro_de_rotacion[1])*math.cos(math.radians(angulo))))+(((puntosR[i][0]-centro_de_rotacion[0])*math.sin(math.radians(angulo))))
        cv2.waitKey(1000)
        rectangleImage = cv2.polylines(imagen, [puntos], True, color, 3)
        cv2.imshow('Black Image', rectangleImage)
        print(puntos)


    cv2.waitKey(0)
    cv2.destroyAllWindows()

rotacionImagen(35, centro_de_rotacion)

