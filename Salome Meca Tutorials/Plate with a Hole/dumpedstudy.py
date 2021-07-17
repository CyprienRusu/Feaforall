#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.3.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/cyprien/Desktop/plate_hole')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Face_1 = geompy.MakeFaceHW(50, 100, 1)
geompy.TranslateDXDYDZ(Face_1, 25, 50, 0)
Disk_1 = geompy.MakeDiskR(20, 1)
platehole = geompy.MakeCutList(Face_1, [Disk_1], True)
edge_x = geompy.CreateGroup(platehole, geompy.ShapeType["EDGE"])
geompy.UnionIDs(edge_x, [10])
edge_y = geompy.CreateGroup(platehole, geompy.ShapeType["EDGE"])
geompy.UnionIDs(edge_y, [3])
load_edge = geompy.CreateGroup(platehole, geompy.ShapeType["EDGE"])
geompy.UnionIDs(load_edge, [6])
[edge_x, edge_y, load_edge] = geompy.GetExistingSubObjects(platehole, True)
[edge_x, edge_y, load_edge] = geompy.GetExistingSubObjects(platehole, True)
exported = geompy.ExportXAO(platehole, [edge_x, edge_y, load_edge], [], "", "/home/cyprien/Desktop/plate_hole/plate_hole2.xao", "")
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Disk_1, 'Disk_1' )
geompy.addToStudy( platehole, 'platehole' )
geompy.addToStudyInFather( platehole, edge_x, 'edge_x' )
geompy.addToStudyInFather( platehole, edge_y, 'edge_y' )
geompy.addToStudyInFather( platehole, load_edge, 'load_edge' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_1 = smesh.Mesh(platehole)
NETGEN_1D_2D = Mesh_1.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize( 6 )
NETGEN_2D_Parameters_1.SetMinSize( 3.13836 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetChordalError( -1 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 22029 )
NETGEN_2D_Parameters_1.SetUseDelauney( 0 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 64 )
isDone = Mesh_1.Compute()
edge_x_1 = Mesh_1.GroupOnGeom(edge_x,'edge_x',SMESH.EDGE)
edge_y_1 = Mesh_1.GroupOnGeom(edge_y,'edge_y',SMESH.EDGE)
load_edge_1 = Mesh_1.GroupOnGeom(load_edge,'load_edge',SMESH.EDGE)
edge_x_2 = Mesh_1.GroupOnGeom(edge_x,'edge_x',SMESH.NODE)
edge_y_2 = Mesh_1.GroupOnGeom(edge_y,'edge_y',SMESH.NODE)
load_edge_2 = Mesh_1.GroupOnGeom(load_edge,'load_edge',SMESH.NODE)
smesh.SetName(Mesh_1, 'Mesh_1')
try:
  Mesh_1.ExportMED(r'/home/cyprien/Desktop/plate_hole/platehole2.med',auto_groups=0,minor=40,overwrite=1,meshPart=None,autoDimension=1)
  pass
except:
  print('ExportMED() failed. Invalid file name?')
[ edge_x_1, edge_y_1, load_edge_1, edge_x_2, edge_y_2, load_edge_2 ] = Mesh_1.GetGroups()
smesh.SetName(Mesh_1, 'Mesh_1')
try:
  Mesh_1.ExportMED(r'/home/cyprien/Desktop/plate_hole/plate_hole2_Files/RunCase_1/Result-Stage_1/_ExportedFromSalomeObject_0_1_2_3.med',auto_groups=0,minor=-1,overwrite=1,meshPart=None,autoDimension=1)
  pass
except:
  print('ExportMED() failed. Invalid file name?')
smesh.SetName(Mesh_1, 'Mesh_1')
try:
  Mesh_1.ExportMED(r'/home/cyprien/Desktop/plate_hole/plate_hole2_Files/RunCase_2/Result-Stage_1/_ExportedFromSalomeObject_0_1_2_3.med',auto_groups=0,minor=-1,overwrite=1,meshPart=None,autoDimension=1)
  pass
except:
  print('ExportMED() failed. Invalid file name?')


## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(edge_x_1, 'edge_x')
smesh.SetName(load_edge_1, 'load_edge')
smesh.SetName(edge_y_1, 'edge_y')
smesh.SetName(edge_y_2, 'edge_y')
smesh.SetName(load_edge_2, 'load_edge')
smesh.SetName(edge_x_2, 'edge_x')

###
### ASTERSTUDY component
###

###
### PARAVIS component
###

import pvsimple
pvsimple.ShowParaviewView()
# trace generated using paraview version 5.6.0-RC1

#### import the simple module from the paraview
from pvsimple import *
#### disable automatic camera reset on 'Show'
pvsimple._DisableFirstRenderCameraReset()

CreateLayout('Layout #2')

# set active view
SetActiveView(None)

# Create a new 'Render View'
asterStudyResultsView = CreateView('RenderView')
asterStudyResultsView.ViewSize = [1839, 904]
asterStudyResultsView.AxesGrid = 'GridAxes3DActor'
asterStudyResultsView.StereoType = 0
asterStudyResultsView.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
asterStudyResultsView.AxesGrid.XTitleFontFile = ''
asterStudyResultsView.AxesGrid.YTitleFontFile = ''
asterStudyResultsView.AxesGrid.ZTitleFontFile = ''
asterStudyResultsView.AxesGrid.XLabelFontFile = ''
asterStudyResultsView.AxesGrid.YLabelFontFile = ''
asterStudyResultsView.AxesGrid.ZLabelFontFile = ''

# get layout
asterStudyResultsLayout = GetLayout()

# place view in the layout
asterStudyResultsLayout.AssignView(0, asterStudyResultsView)

# reset view to fit data
asterStudyResultsView.ResetCamera()

# create a new 'MED Reader'
mEDReader1 = MEDReader(FileName='/home/cyprien/Desktop/plate_hole/platehole_res.rmed')

# create a new 'MED Reader'
mEDReader1_1 = MEDReader(FileName='/tmp/tmp6xczr_u0.med')

# create a new 'Extract Group'
extractGroup1 = ExtractGroup(Input=mEDReader1_1)

# show data in view
extractGroup1Display = Show(extractGroup1, asterStudyResultsView)

# trace defaults for the display properties.
extractGroup1Display.Representation = 'Surface'

HideAll(asterStudyResultsView)

# destroy extractGroup1
Delete(extractGroup1)
del extractGroup1

# reset view to fit data
asterStudyResultsView.ResetCamera()

HideAll(asterStudyResultsView)

# set active source
SetActiveSource(mEDReader1)

# create a new 'Calculator'
calculator1 = Calculator(Input=mEDReader1)

# show data in view
calculator1Display = Show(calculator1, asterStudyResultsView)

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'

# hide data in view
Hide(calculator1, asterStudyResultsView)

# create a new 'Extract Components'
extractComponents1 = ExtractComponents(Input=calculator1)

# create a new 'Warp By Vector'
warpByVector1 = WarpByVector(Input=extractComponents1)

# show data in view
warpByVector1Display = Show(warpByVector1, asterStudyResultsView)

# trace defaults for the display properties.
warpByVector1Display.Representation = 'Surface'

# set scalar coloring
ColorBy(warpByVector1Display, ('POINTS', 'result__DEPL:MAGTRAN'))

# rescale color and/or opacity maps used to exactly fit the current data range
warpByVector1Display.RescaleTransferFunctionToDataRange(False, True)

# show color bar/color legend
warpByVector1Display.SetScalarBarVisibility(asterStudyResultsView, True)

# get color transfer function/color map for 'result__DEPLMAGTRAN'
result__DEPLMAGTRANLUT = GetColorTransferFunction('result__DEPLMAGTRAN')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
result__DEPLMAGTRANLUT.ApplyPreset('jet', True)

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=mEDReader1)

# show data in view
extractSurface1Display = Show(extractSurface1, asterStudyResultsView)

# trace defaults for the display properties.
extractSurface1Display.Representation = 'Surface'

# reset view to fit data
asterStudyResultsView.ResetCamera()

# reset view to fit data
asterStudyResultsView.ResetCamera()

HideAll(asterStudyResultsView)

# set active source
SetActiveSource(mEDReader1)

# hide data in view
Hide(extractSurface1, asterStudyResultsView)

# show data in view
mEDReader1Display = Show(mEDReader1, asterStudyResultsView)

# trace defaults for the display properties.
mEDReader1Display.Representation = 'Surface'

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'result__SIEQ_NOEU', 'VMIS'))

# rescale color and/or opacity maps used to exactly fit the current data range
mEDReader1Display.RescaleTransferFunctionToDataRange(False, True)

# show color bar/color legend
mEDReader1Display.SetScalarBarVisibility(asterStudyResultsView, True)

# get color transfer function/color map for 'result__SIEQ_NOEU'
result__SIEQ_NOEULUT = GetColorTransferFunction('result__SIEQ_NOEU')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
result__SIEQ_NOEULUT.ApplyPreset('jet', True)

# get opacity transfer function/opacity map for 'result__SIEQ_NOEU'
result__SIEQ_NOEUPWF = GetOpacityTransferFunction('result__SIEQ_NOEU')

HideAll(asterStudyResultsView)

# show data in view
mEDReader1Display = Show(mEDReader1, asterStudyResultsView)

# set scalar coloring
ColorBy(mEDReader1Display, ('POINTS', 'result__SIEQ_NOEU', 'VMIS'))

# rescale color and/or opacity maps used to exactly fit the current data range
mEDReader1Display.RescaleTransferFunctionToDataRange(False, True)

# show color bar/color legend
mEDReader1Display.SetScalarBarVisibility(asterStudyResultsView, True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
result__SIEQ_NOEULUT.ApplyPreset('jet', True)

# find view
renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1839, 904]

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(None)

#### saving camera placements for all active views

# current camera placement for asterStudyResultsView
asterStudyResultsView.CameraPosition = [-33.970193758308945, -45.62102248310446, 102.90485164575323]
asterStudyResultsView.CameraFocalPoint = [30.02998299750334, 42.68116449712005, -5.049405746046945]
asterStudyResultsView.CameraViewUp = [0.3232660193367281, 0.6295053572013249, 0.7065564988003566]
asterStudyResultsView.CameraParallelScale = 58.14851674806526

# current camera placement for renderView1

###
### YACS component
###


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
