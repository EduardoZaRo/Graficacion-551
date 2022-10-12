'''
EQUIPO 3
Las superelipses pueden ser descritas mediante las siguientes ecuaciones paramétricas: (0 representa theta en las ec.)
x = a|cos(0)|^(2/n) sgn(cos(0))
x = b|sin(0)|^(2/n) sgn(sin(0))
para 0<=0<2pi
Graficar (x,y) para los siguientes distintos valores de a, b ∈ R y n ∈ Q (n>0). Utilizar la
matriz de transformación de Ventana-Marco para visualizar la grafica.
Equipo 3. Un hipoelipse con n=1/2 y a=b=1. Use toda la resolución de la pantalla.

Gaxiola Ali
Ramirez Jorge
Zavala Irvin
'''

import ctypes
import matplotlib.pyplot as plt
import numpy as np 
import math



umin = 0
vmin = 0 
#Se obtiene la resolucion de la pantalla
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
umax = user32.GetSystemMetrics(0)
vmax = user32.GetSystemMetrics(1)

a = 1; b = 1; n = 1/2; m = 1/2

theta = np.linspace(0, 2*math.pi, 100)



x = ((np.abs(np.cos(theta))) ** (2 / m))*a * np.sign(np.cos(theta))
y = ((np.abs(np.sin(theta))) ** (2 / n))*b * np.sign(np.sin(theta))

xmin = min(x)
xmax = max(x)
ymin = min(y)
ymax = max(y)

sx = (umax-umin)/(xmax-xmin)
sy = (vmax-vmin)/(ymax-ymin)
tx = -sx*xmin+umin
ty = -sy*ymin+vmin

M = np.array([[sx,0,tx],
             [0,sy,ty],
             [0,0,1]])

I = np.array([[x],
              [y],
              [1]],dtype=object)
Iv = np.matmul(M,I)

#Artificio de copiar las filas de Iv a otros vectores con fors porque sino no sale
uaux = Iv[0]
vaux = Iv[1]
u = np.array([])
v = np.array([])
for i in uaux:
    u = np.append(u,i)
for i in vaux:
    v = np.append(v,i)
plt.plot(u,v)
plt.title("viewport")
plt.grid()
plt.show()
plt.plot(x,y)
plt.title("mundial")
plt.grid()
plt.show()
