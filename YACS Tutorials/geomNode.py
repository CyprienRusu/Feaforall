# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v8.5.0 with dump python functionality
###

import sys
import salome

import tempfile, os

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'/home/cy/Desktop/plate-tester')
###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New(theStudy)

tmpdir = tempfile.mkdtemp()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Plate = geompy.MakeBoxDXDYDZ(a, b, t)
[Compound_1, Compound_2, Compound_3] = geompy.Propagate(Plate)
vol = geompy.CreateGroup(Plate, geompy.ShapeType["SOLID"])
geompy.UnionIDs(vol, [1])
zmax = geompy.CreateGroup(Plate, geompy.ShapeType["FACE"])
geompy.UnionIDs(zmax, [33])
zmin = geompy.CreateGroup(Plate, geompy.ShapeType["FACE"])
geompy.UnionIDs(zmin, [31])
ymin = geompy.CreateGroup(Plate, geompy.ShapeType["FACE"])
geompy.UnionIDs(ymin, [23])
ymax = geompy.CreateGroup(Plate, geompy.ShapeType["FACE"])
geompy.UnionIDs(ymax, [27])
xmax = geompy.CreateGroup(Plate, geompy.ShapeType["FACE"])
geompy.UnionIDs(xmax, [13])
xmin = geompy.CreateGroup(Plate, geompy.ShapeType["FACE"])
geompy.UnionIDs(xmin, [3])

# export sphere to the STEP file, using millimeters as length units
f_step = os.path.join(savepath, "plate.step")
geompy.ExportSTEP(Plate, f_step, GEOM.LU_MILLIMETER)
