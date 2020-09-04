#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.3.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'C:/Users/cypri/Desktop/concrete')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS
import random


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Box_1 = geompy.MakeBoxDXDYDZ(200, 200, 200)
Vertex_1 = geompy.MakeVertex(3, 4, 5)

Spheres = []

for i in range(1000):
	x = random.uniform(0,200)
	y = random.uniform(0,200)
	z = random.uniform(0,200)
	r = random.uniform(0,6)
	Sphere_1 = geompy.MakeSphere(x,y,z,r)
	Spheres.append(Sphere_1)


Partition_1 = geompy.MakePartition([Box_1], Spheres, [], [], geompy.ShapeType["SOLID"], 0, [], 0)


geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )

geompy.addToStudy( Partition_1, 'Concrete' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
