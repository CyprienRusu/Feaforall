# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v8.5.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'/home/cy/Desktop/yacs-example')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Box_1 = geompy.MakeBoxDXDYDZ(500, 500, 4)
[ymin, zmax, volume] = geompy.Propagate(Box_1)
volume = geompy.CreateGroup(Box_1, geompy.ShapeType["SOLID"])
geompy.UnionIDs(volume, [1])
zmax = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(zmax, [33])
zmin = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(zmin, [31])
ymin = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(ymin, [23])
ymax = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(ymax, [27])
xmax = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(xmax, [13])
xmin = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(xmin, [3])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudyInFather( Box_1, ymax, 'ymax' )
geompy.addToStudyInFather( Box_1, zmin, 'zmin' )
geompy.addToStudyInFather( Box_1, ymin, 'ymin' )
geompy.addToStudyInFather( Box_1, zmax, 'zmax' )
geompy.addToStudyInFather( Box_1, volume, 'volume' )
geompy.addToStudyInFather( Box_1, xmax, 'xmax' )
geompy.addToStudyInFather( Box_1, xmin, 'xmin' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New(theStudy)
Mesh_1 = smesh.Mesh(Box_1)
Regular_1D = Mesh_1.Segment()
Local_Length_1 = Regular_1D.LocalLength(4,None,1e-07)
Quadrangle_2D = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Hexa_3D = Mesh_1.Hexahedron(algo=smeshBuilder.Hexa)
isDone = Mesh_1.Compute()
volume_1 = Mesh_1.GroupOnGeom(volume,'volume',SMESH.VOLUME)
zmax_1 = Mesh_1.GroupOnGeom(zmax,'zmax',SMESH.FACE)
zmin_1 = Mesh_1.GroupOnGeom(zmin,'zmin',SMESH.FACE)
ymin_1 = Mesh_1.GroupOnGeom(ymin,'ymin',SMESH.FACE)
ymax_1 = Mesh_1.GroupOnGeom(ymax,'ymax',SMESH.FACE)
xmax_1 = Mesh_1.GroupOnGeom(xmax,'xmax',SMESH.FACE)
xmin_1 = Mesh_1.GroupOnGeom(xmin,'xmin',SMESH.FACE)
smesh.SetName(Mesh_1, 'Mesh_1')
try:
  Mesh_1.ExportMED( r'/home/cy/Desktop/yacs-example/Plate.med', 0, SMESH.MED_V2_2, 1, None ,1)
  pass
except:
  print 'ExportToMEDX() failed. Invalid file name?'


## Set names of Mesh objects
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Local_Length_1, 'Local Length_1')
smesh.SetName(zmax_1, 'zmax')
smesh.SetName(zmin_1, 'zmin')
smesh.SetName(ymin_1, 'ymin')
smesh.SetName(ymax_1, 'ymax')
smesh.SetName(xmax_1, 'xmax')
smesh.SetName(xmin_1, 'xmin')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(volume_1, 'volume')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
