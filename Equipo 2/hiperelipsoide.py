""""
Integrantes:

Arce Montoya José Antonio
Garcia Gutierrez Josue Ramón
Navarrete Solano Cristian Osbaldo
Segoviano Sanchez Miguel Angel

"""

import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import math
import matplotlib.patches as pc
from win32api import GetSystemMetrics

theta = np.linspace(0, 2*math.pi, 100)
a = 2
b = 3
n = 4
m = 2

x = np.linspace(0, 2*math.pi, 100)
y = np.linspace(0, 2*math.pi, 100)

ar = [1,3,1,3]
br = [1,2,1,3]
nr = [4,3.5,2.5,5]
mr = [1,2,3,3]

umin = [GetSystemMetrics(0)/2,0,GetSystemMetrics(0)/2,0]
vmin = [0,GetSystemMetrics(1)/2,GetSystemMetrics(1)/2,0]
umax = [GetSystemMetrics(0),GetSystemMetrics(0)/2,GetSystemMetrics(0),GetSystemMetrics(0)/2]
vmax = [GetSystemMetrics(1)/2,GetSystemMetrics(1),GetSystemMetrics(1), GetSystemMetrics(1)/2]

def hiperelisoide(theta, a, b, n):
    for i in range (theta.size):
        x[i] = a*abs(math.cos((theta[i])))**(2/n)*sign(math.cos((theta[i])))
        y[i] = b*abs(math.sin((theta[i])))**(2/m)*sign(math.sin((theta[i])))
    fig = plt.figure()
    plt.plot(x,y)
    fig.set_size_inches(11, 7)
    plt.show()

def hiperelipsoideVP(x, y, theta, ar, br, nr, mr, umin, umax, vmin, vmax):
    fig, axs = plt.subplots(2, 2)
    for j in range (4):
        for i in range (theta.size):
            x[i] = ar[j]*abs(math.cos((theta[i])))**(2/nr[j])*sign(math.cos((theta[i])))
            y[i] = br[j]*abs(math.sin((theta[i])))**(2/mr[j])*sign(math.sin((theta[i])))

        xmax = np.max(x)
        ymax = np.max(y)

        xmin = np.min(x)
        ymin = np.min(y)

        sx = (umax[j]-umin[j])/(xmax-xmin)
        sy = (vmax[j]-vmin[j])/(ymax-ymin)

        tx = -sx*xmin+umin[j]
        ty = -sy*ymin+vmin[j]

        M = [[sx, 0, tx], [0, sy, ty],  [0, 0, 1] ]
        M = np.array(M)

        I = np.row_stack((x, y))

        ones = np.ones(shape = (1, np.size(x)))

        I2 = np.row_stack((I, ones))

        Iv = np.dot(M,I2)

        u = Iv[0]
        v = Iv[1]

        if j == 1:
            axs[0, 0].plot(u, v)
            axs[0, 0].set_title("Elipse 1")
        elif j == 2:
            axs[0, 1].plot(u, v)
            axs[0, 1].set_title("Elipse 2")
        elif j == 3:
            axs[1, 0].plot(u, v)
            axs[1, 0].set_title("Elipse 3")
        else:
            axs[1, 1].plot(u, v)
            axs[1, 1].set_title("Elipse 4")
    fig.set_size_inches(11, 7)
    plt.show()



def hiperelisoide4(theta, a, b, n):
    fig, axs = plt.subplots(2, 2)
    for j in range (4):
        for i in range (theta.size):
            x[i] = ar[j]*abs(math.cos((theta[i])))**(2/nr[j])*sign(math.cos((theta[i])))
            y[i] = br[j]*abs(math.sin((theta[i])))**(2/mr[j])*sign(math.sin((theta[i])))
        if j == 1:
            axs[0, 0].plot(x, y)
            axs[0, 0].set_title("Elipse 1")
        elif j == 2:
            axs[0, 1].plot(x, y)
            axs[0, 1].set_title("Elipse 2")
        elif j == 3:
            axs[1, 0].plot(x, y)
            axs[1, 0].set_title("Elipse 3")
        else:
            axs[1, 1].plot(x, y)
            axs[1, 1].set_title("Elipse 4")
    fig.set_size_inches(11, 7)
    plt.show()


def sign(a):
    if a < 0:
        return -1
    elif a == 0:
        return 0
    else:
        return 1


hiperelisoide(theta, a, b, n)
hiperelipsoideVP(x,y,theta,ar,br,nr,mr,umin,umax,vmin,vmax)