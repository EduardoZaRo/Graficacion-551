import numpy as np
import math
import tkinter
import time
'''
Programa que rota una flecha con operaciones matriciales y punto fijo, basado en la diapositiva 22.

GAXIOLA GERARDO EDWISH ALI
RAMIREZ MALDONADO JOSE LUIS
ZAVALA ROMAN IRVIN EDUARDO
'''
def rotar(flecha, rotado):
    i = 0
    for elemento in flecha:
        p = ([elemento[0],elemento[1],1])
        multiplicacion = np.matmul(p, rotado)

        p_prima = [multiplicacion[0],multiplicacion[1]]
        flecha[:][i] = p_prima
        i+=1


top = tkinter.Tk()

C = tkinter.Canvas(top, bg="white", height=500, width=500)
C.pack()

flecha = np.array([ #SI NO SE USAN FLOAT LA PRECISION SE PIERDE EN LA ANIMACION
            [250.0,250.0], #PUNTO FIJO
            [375.0,375.0],
            [350.0,375.0],
            [375.0,350.0]
         ])
'''
flecha = np.array([ #SI NO SE USAN FLOAT LA PRECISION SE PIERDE EN LA ANIMACION
            [250,250], #PUNTO FIJO
            [375,375],
            [350,375],
            [375,350]
         ])
'''


angulo = 2
print("Flecha original:",flecha)
line_original = C.create_line(flecha[0][0], flecha[0][1], flecha[1][0], flecha[1][1], flecha[2][0], flecha[2][1],flecha[3][0], flecha[3][1], flecha[1][0], flecha[1][1],fill = "black")
line = 0#Solo para que el primer C.delete(line) funcione




rotado = np.array([
    [math.cos(math.radians(angulo)),math.sin(math.radians(angulo)),0],
    [-1*math.sin(math.radians(angulo)),math.cos(math.radians(angulo)),0],
    [(1-math.cos(math.radians(angulo)))*flecha[0][0] + flecha[0][1]*math.sin(math.radians(angulo)),(1-math.cos(math.radians(angulo)))*flecha[0][1] - flecha[0][0]*math.sin(math.radians(angulo)),1]
])



while(True):
    C.update()
    C.delete(line)
    line = C.create_line(flecha[0][0], flecha[0][1], flecha[1][0], flecha[1][1], flecha[2][0], flecha[2][1],flecha[3][0], flecha[3][1], flecha[1][0], flecha[1][1],fill = "red")
    rotar(flecha,rotado) 
    time.sleep(0.01)

 

