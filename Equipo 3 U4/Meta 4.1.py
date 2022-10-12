from re import U
import numpy as np
import math
import matplotlib.pyplot as plt

def viewProjMatrix(az, el, phi, target):
    if phi == None and target == None:
        phi = 0
    elif (phi != None and target == None) or (phi == None and target != None) or (phi != None and target != None):
        if phi > 0:
            d = (math.sqrt(2)/2)/(math.tan(phi*math.pi/360))
        else: phi = 0 
    el = ((((el+180)%360)+360)%360)-180
    
    if el > 90:
        el = 180 - el
        az = az + 180
    elif el < -90:
        el = -180 - el
        az = az + 180
    az = ((az%360)+360)%360
    
    az = (az * math.pi)/180
    el = (el * math.pi)/180

    if target != None:
        if len(target) != 3:
            print("ERROR")
    else:
        target1 = 0.5 + (math.sqrt(3)/2)*(math.cos(el)*math.sin(az))
        target2 = 0.5 + (math.sqrt(3)/2)*(-math.cos(el)*math.cos(az))
        target3 = 0.5 + (math.sqrt(3)/2)*(math.sin(el))
    T = np.array([[1,0,0,-target1],
                  [0,1,0,-target2],
                  [0,0,1,-target3],
                  [0,0,0,1]])

    R = np.array([[math.cos(az),math.sin(az),0,0],
                  [-math.sin(el)*math.sin(az),math.sin(el)*math.cos(az),math.cos(el), 0],
                  [math.cos(el)*math.sin(az),-math.cos(el)*math.cos(az),math.sin(el), 0],
                  [0,0,0,1]
                  ])
    if (phi == None and target == None) or phi == 0:
        return R
    f = d

    Mwc_vc = np.matmul(R,T)
    Tpers = np.array([[1,0,0,0],
                    [0,1,0,0],
                    [0,0,1,0],
                    [0,0,-1/f,d/f]])
    return np.matmul(Tpers, Mwc_vc)
def view3d_simple(path_1,path_2):
    #Cambiar por direccion de nuestra maquina
    verts = np.loadtxt('C:\\Users\\irvin\\Desktop\\Equipo 3 A4\\{}'.format(path_1))
    faces = np.loadtxt('C:\\Users\\irvin\\Desktop\\Equipo 3 A4\\{}'.format(path_2))
    faces_f = np.array(faces)
    faces = faces_f.astype(int)
    print(faces)
    
    verts = np.array(verts)
    alpha = -37.5
    beta = 30.0
    phi = 10.0
    M = viewProjMatrix(alpha,beta,phi,None)
    Ih = np.append(verts,np.ones((len(verts),1)),axis = 1)
    Vh = M.dot(Ih.transpose())
    Vx = Vh[0,:]/Vh[3,:]
    Vy = Vh[1,:]/Vh[3,:]
    Vz = Vh[2,:]/Vh[3,:]
    V = [Vx.transpose(),Vy.transpose(),Vz.transpose()]
    U = [V[0],V[1]]
    x = []
    y = []
    for k in range(len(faces)):
        idf = np.array([faces[k][0],faces[k][1],faces[k][2],faces[k][3], faces[k][0]])
        idf = idf.transpose()
        print(idf)
        for i in idf:
            x.append(U[0][i])
            y.append(U[1][i])

    plt.plot(x,y)
    plt.show()
view3d_simple("teapot_vertex.dat","teapot_faces.dat")
