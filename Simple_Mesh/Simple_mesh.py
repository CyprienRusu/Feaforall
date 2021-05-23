import numpy as np 
import matplotlib.pyplot as plt
import math

#0 - Define Paraneters
L = 0.1
h = 0.05
r = 0.02

nb_element = 20

#1-1 Create Nodes
#Nodes = np.array([[0,0],[0,1],[1,0],[1,1]])

Nodes = []

for x in np.linspace(0, L, num=nb_element):
    if(x<r):
        y0 = math.sqrt(r**2-x**2)
        for y in np.linspace(y0, h, num=nb_element):
            Nodes.append([x,y])
            
    else:
        for y in np.linspace(0, h, num=nb_element):
            Nodes.append([x,y])

#1-2 Display Nodes

points = np.array(Nodes)

plt.plot(points[:,0],points[:,1],'o')
plt.show()

#2-1 Create Elements
from scipy.spatial import Delaunay
tri = Delaunay(points)

#2-2 Display Elements
plt.triplot(points[:,0], points[:,1], tri.simplices)
plt.plot(points[:,0], points[:,1], 'o')
plt.show()

#2-3 Cleanup Mesh
#Create a set of points on a circle of diameter 0.0195
p = []
r2=0.0195
for x in np.linspace(0,r2,10):
    p.append([x,math.sqrt(r2**2-x**2)])

#Find the elements which contain those points
tri.find_simplex(p)

#Feed the result of the previous function to the np.delete method
#Create a new set of elements without the problematic elements
mesh = np.delete(tri.simplices,[0,153,154,21],0)

#3- Export into a file
nb_nodes = len(points)
nb_elements = len(mesh)

file = open("plate_mesh.dat","w")
file.write("{} {}\n".format(nb_nodes,nb_elements))
for i,node in enumerate(Nodes):
    file.write("{} {} {}\n".format(i,node[0],node[1])) 
for j,elem in enumerate(mesh):
    file.write("{} {} {} {}\n".format(j,elem[0],elem[1],elem[2]))
file.close()