#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Hecho por
# Brian Ramiro Soto Elenes 1254563
# Amezquita Becerra Carlos Daniel 1262695
# Rivera Soto Karen Dayanara 1271872


# In[2]:


import matplotlib.pyplot as plt
import numpy as np

def elipsoide(a, b, n, limI,limS):
    t = np.linspace(limI, limS, 100)
    x = ((np.abs(np.cos(t))) ** (2 / n)) * a * np.sign(np.cos(t))
    y = ((np.abs(np.sin(t))) ** (2 / n)) * b * np.sign(np.sin(t))
    return (x,y)

def superElipse(a, b, n, m, limI, limS):
    t = np.linspace(limI, limS, 100)
    x = ((np.abs(np.cos(t))) ** (2 / m)) * a * np.sign(np.cos(t))
    y = ((np.abs(np.sin(t))) ** (2 / n)) * b * np.sign(np.sin(t))
    return(x,y)

def WindowtoViewport(x_w, y_w, x_wmax, y_wmax, x_wmin, y_wmin, x_vmax, y_vmax, x_vmin, y_vmin):
                            
    sx = (x_vmax - x_vmin) / (x_wmax - x_wmin)
    sy = (y_vmax - y_vmin) / (y_wmax - y_wmin)
 
    x_v = x_vmin + ((x_w - x_wmin) * sx)
    y_v = y_vmin + ((y_w - y_wmin) * sy)
 
    return(x_v, y_v)


# In[3]:


#Pantalla
x_wmax = 20
y_wmax = 20
x_wmin = 0
y_wmin = 0
 
# Viewport I
x0_vmax = 10
y0_vmax = 20
x0_vmin = 0
y0_vmin = 10

# Viewport II
x1_vmax = 20
y1_vmax = 20
x1_vmin = 10
y1_vmin = 10

# Viewport III
x2_vmax = 10
y2_vmax = 10
x2_vmin = 0
y2_vmin = 0

# Viewport IV
x3_vmax = 20
y3_vmax = 10
x3_vmin = 10
y3_vmin = 0

#Pruebas
print(WindowtoViewport(5, 5, x_wmax, y_wmax, x_wmin, y_wmin, x0_vmax, y0_vmax, x0_vmin, y0_vmin))
print(WindowtoViewport(1, 1, x_wmax, y_wmax, x_wmin, y_wmin, x1_vmax, y1_vmax, x1_vmin, y1_vmin))
print(WindowtoViewport(1, 1, x_wmax, y_wmax, x_wmin, y_wmin, x2_vmax, y2_vmax, x2_vmin, y2_vmin))
print(WindowtoViewport(1, 1, x_wmax, y_wmax, x_wmin, y_wmin, x3_vmax, y3_vmax, x3_vmin, y3_vmin))


# In[4]:


#Elipsoide en un Viewport 
(x,y) = elipsoide(1,1,4,0, 2 * np.pi)
plt.axis('equal')
plt.plot(x, y)

plt.show()


# In[5]:


#Cuatro Viewports
(x0,y0) = superElipse(1, 2, 0.25, 0.50, 0,2*np.pi)
(x1,y1) = superElipse(3, 4, 0.50, 0.75, 0,2*np.pi)
(x2,y2) = superElipse(5, 6, 0.75, 1.00, 0,2*np.pi)
(x3,y3) = superElipse(7, 8, 1.00, 1.25, 0,2*np.pi)

fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2, 2)
fig.suptitle("SuperElipse")

ax0.plot(x0,y0)
ax1.plot(x1,y1)
ax2.plot(x2,y2)
ax3.plot(x3,y3)

plt.show()


# In[6]:


# Cuatro Figuras en un viewport
(x0,y0) = WindowtoViewport(x0, y0, x_wmax, y_wmax, x_wmin, y_wmin, x0_vmax, y0_vmax, x0_vmin, y0_vmin)
(x1,y1) = WindowtoViewport(x1, y1, x_wmax, y_wmax, x_wmin, y_wmin, x1_vmax, y1_vmax, x1_vmin, y1_vmin)
(x2,y2) = WindowtoViewport(x2, y2, x_wmax, y_wmax, x_wmin, y_wmin, x2_vmax, y2_vmax, x2_vmin, y2_vmin)
(x3,y3) = WindowtoViewport(x3, y3, x_wmax, y_wmax, x_wmin, y_wmin, x3_vmax, y3_vmax, x3_vmin, y3_vmin)

plt.plot(x0, y0)
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)

plt.show()

