###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

import os

smesh = smeshBuilder.New(theStudy)
Mesh_1 = smesh.Mesh(Plate)
Regular_1D = Mesh_1.Segment()
Local_Length_1 = Regular_1D.LocalLength(meshSize,None,1e-07)
Quadrangle_2D = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Hexa_3D = Mesh_1.Hexahedron(algo=smeshBuilder.Hexa)
Regular_1D_1 = Mesh_1.Segment(geom=Compound_1)
Number_of_Segments_1 = Regular_1D_1.NumberOfSegments(elemThick)
isDone = Mesh_1.Compute()
Sub_mesh_1 = Regular_1D_1.GetSubMesh()


## Set names of Mesh objects
smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(Local_Length_1, 'Local Length_1')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
vol_10 = Mesh_1.GroupOnGeom(vol,'vol',SMESH.VOLUME)
zmax_10 = Mesh_1.GroupOnGeom(zmax,'zmax',SMESH.FACE)
zmin_10 = Mesh_1.GroupOnGeom(zmin,'zmin',SMESH.FACE)
ymin_10 = Mesh_1.GroupOnGeom(ymin,'ymin',SMESH.FACE)
ymax_10 = Mesh_1.GroupOnGeom(ymax,'ymax',SMESH.FACE)
xmax_10 = Mesh_1.GroupOnGeom(xmax,'xmax',SMESH.FACE)
xmin_10 = Mesh_1.GroupOnGeom(xmin,'xmin',SMESH.FACE)
Sub_mesh_1 = Regular_1D_1.GetSubMesh()



 # export the mesh in a MED file
import tempfile
medFile = os.path.join(savepath, "plate.med")
Mesh_1.ExportMED( medFile, 0 )
