import pvsimple
pvsimple.ShowParaviewView()
# trace generated using paraview version 5.6.0-RC1

#### import the simple module from the paraview
from pvsimple import *
#### disable automatic camera reset on 'Show'
pvsimple._DisableFirstRenderCameraReset()

# create a new 'CSV Reader'
mesh_convergencetxt = CSVReader(FileName=['/home/cyprien/Desktop/plate_hole/mesh_convergence.txt'])

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024
# uncomment following to set a specific view size
# spreadSheetView1.ViewSize = [400, 400]

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(2, spreadSheetView1)

# show data in view
mesh_convergencetxtDisplay = Show(mesh_convergencetxt, spreadSheetView1)

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Plot Data'
plotData1 = PlotData(Input=mesh_convergencetxt)

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [766, 417]
lineChartView1.ChartTitleFontFile = ''
lineChartView1.LeftAxisTitleFontFile = ''
lineChartView1.LeftAxisLabelFontFile = ''
lineChartView1.BottomAxisTitleFontFile = ''
lineChartView1.BottomAxisLabelFontFile = ''
lineChartView1.RightAxisLabelFontFile = ''
lineChartView1.TopAxisTitleFontFile = ''
lineChartView1.TopAxisLabelFontFile = ''

# place view in the layout
layout1.AssignView(6, lineChartView1)

# show data in view
plotData1Display = Show(plotData1, lineChartView1)

# update the view to ensure updated data information
spreadSheetView1.Update()

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on lineChartView1
lineChartView1.BottomAxisTitle = 'mesh size (mm)'

# Properties modified on lineChartView1
lineChartView1.LeftAxisTitle = 'Max Von Mises Stress (MPa)'

# save screenshot
SaveScreenshot('/home/cyprien/Desktop/plate_hole/mesh_convergence2.png', lineChartView1, ImageResolution=[766, 417])

# set active view
SetActiveView(spreadSheetView1)

# set active source
SetActiveSource(mesh_convergencetxt)

#### saving camera placements for all active views


