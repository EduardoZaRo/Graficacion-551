'''
EQUIPO 3
Las superelipses generalizadas pueden ser descritas mediante las siguientes 
ecuaciones paramétricas: (0 representa theta en las ec.)
x = a|cos(0)|^(2/m) sgn(cos(0))
x = b|sin(0)|^(2/n) sgn(sin(0))
para 0<=0<2pi, a, b ∈ R, n,m ∈ Q (n,m>0)
Graficar (x,y) para distintos valores de a, b ∈ R y n, m ∈ Q (n,m>0). Utilizar la matriz de
transformación de Ventana-Marco para visualizar la grafica, usando 4 marcos para visualizar
las graficas con los distintos valores de n, m, a y b.

Gaxiola Ali
Ramirez Jorge
Zavala Irvin
'''

import ctypes
import matplotlib.pyplot as plt
import numpy as np 
import math

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

'''
           1080  _______________
                |       |       |
                |  4    |   3   |
            540 |---------------|
                |  1    |   2   |
                |_______|_______|
                0,0    960     1920
'''

def funcion(x,y,
            umin,umax,vmin,vmax,
            a,b,n,m,
            u,v):
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
    for i in uaux:
        u = np.append(u,i)
    for i in vaux:
        v = np.append(v,i)
    return u,v
theta = np.linspace(0, 2*math.pi, 100)
x = np.array([])
y = np.array([])

#1er marco
umin1 = 0
vmin1 = 0
umax1 = user32.GetSystemMetrics(0)/2
vmax1 = user32.GetSystemMetrics(1)/2
a1 = 1; b1 = 1; n1 = 4; m1 = 4
u1 = np.array([])
v1 = np.array([])
u1,v1 = funcion(x,y,umin1,umax1,vmin1,vmax1,a1,b1,n1,m1,u1,v1)
#2do marco
umin2 = user32.GetSystemMetrics(0)/2
vmin2 = 0
umax2 = user32.GetSystemMetrics(0)
vmax2 = user32.GetSystemMetrics(1)/2
a2 = 1; b2 = 1; n2 = 3/2; m2 = 3/2
u2 = np.array([])
v2 = np.array([])
u2,v2 = funcion(x,y,umin2,umax2,vmin2,vmax2,a2,b2,n2,m2,u2,v2)
#3er marco
umin3 = user32.GetSystemMetrics(0)/2
vmin3 = user32.GetSystemMetrics(1)/2
umax3 = user32.GetSystemMetrics(0)
vmax3 = user32.GetSystemMetrics(1)
a3 = 1; b3 = 1; n3 = 1/2; m3 = 1/2
u3 = np.array([])
v3 = np.array([])
u3,v3 = funcion(x,y,umin3,umax3,vmin3,vmax3,a3,b3,n3,m3,u3,v3)
#4to marco
umin4 = 0
vmin4 = user32.GetSystemMetrics(1)/2
umax4 = user32.GetSystemMetrics(0)/2
vmax4 = user32.GetSystemMetrics(1)
a4 = 1; b4 = 1; n4 = 8; m4 = 5
u4 = np.array([])
v4 = np.array([])
u4,v4 = funcion(x,y,umin4,umax4,vmin4,vmax4,a4,b4,n4,m4,u4,v4)

fig, axs = plt.subplots(2,2)
axs[1,0].plot(u1, v1)
axs[1,1].plot(u2, v2)
axs[0,1].plot(u3, v3)
axs[0,0].plot(u4, v4)
plt.show()

