import pvsimple
pvsimple.ShowParaviewView()
#### import the simple module from the paraview
from pvsimple import *
#### disable automatic camera reset on 'Show'
pvsimple._DisableFirstRenderCameraReset()

# create a new 'MED Reader'
plateresrmed = MEDReader(FileName='/home/cyprien/Desktop/yacs-example/plate-res.rmed')

# Properties modified on plateresrmed
plateresrmed.AllArrays = ['TS0/mesh/ComSup0/reslin__DEPL@@][@@P1', 'TS0/mesh/ComSup0/reslin__SIEF_ELGA@@][@@GAUSS', 'TS0/mesh/ComSup0/reslin__SIEQ_ELGA@@][@@GAUSS', 'TS0/mesh/ComSup0/reslin__SIEQ_ELNO@@][@@GSSNE', 'TS0/mesh/ComSup0/reslin__SIEQ_NOEU@@][@@P1']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1364, 605]

# show data in view
plateresrmedDisplay = Show(plateresrmed, renderView1)

# trace defaults for the display properties.
plateresrmedDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(plateresrmedDisplay, ('POINTS', 'reslin__DEPL', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
plateresrmedDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
plateresrmedDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'reslin__DEPL'
reslin__DEPLLUT = GetColorTransferFunction('reslin__DEPL')

# change representation type
plateresrmedDisplay.SetRepresentationType('Surface With Edges')

# current camera placement for renderView1
renderView1.CameraPosition = [343.92459395072444, -376.25237564687177, 447.2095724060549]
renderView1.CameraFocalPoint = [261.0108588956484, 233.67288593478395, -17.39878436508249]
renderView1.CameraViewUp = [-0.040012234163000995, 0.6020305232950466, 0.7974699180147033]
renderView1.CameraParallelScale = 353.6042986164054

# save screenshot
SaveScreenshot('/home/cyprien/Desktop/yacs-example/DEPL.png', renderView1, ImageResolution=[1364, 605])

# set scalar coloring
ColorBy(plateresrmedDisplay, ('POINTS', 'reslin__SIEQ_NOEU', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(reslin__DEPLLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
plateresrmedDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
plateresrmedDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'reslin__SIEQ_NOEU'
reslin__SIEQ_NOEULUT = GetColorTransferFunction('reslin__SIEQ_NOEU')

# Rescale transfer function
reslin__SIEQ_NOEULUT.RescaleTransferFunction(391.919, 800.0)

# get opacity transfer function/opacity map for 'reslin__SIEQ_NOEU'
reslin__SIEQ_NOEUPWF = GetOpacityTransferFunction('reslin__SIEQ_NOEU')

# Rescale transfer function
reslin__SIEQ_NOEUPWF.RescaleTransferFunction(391.919, 800.0)

# Properties modified on reslin__SIEQ_NOEULUT
reslin__SIEQ_NOEULUT.ColorSpace = 'Lab/CIEDE2000'

# Properties modified on reslin__SIEQ_NOEULUT
reslin__SIEQ_NOEULUT.NumberOfTableValues = 12

# current camera placement for renderView1
renderView1.CameraPosition = [343.92459395072444, -376.25237564687177, 447.20957240605503]
renderView1.CameraFocalPoint = [261.0108588956484, 233.67288593478395, -17.39878436508249]
renderView1.CameraViewUp = [-0.040012234163000995, 0.6020305232950466, 0.7974699180147033]
renderView1.CameraParallelScale = 353.6042986164054

# save screenshot
SaveScreenshot('/home/cyprien/Desktop/yacs-example/SIEQ_NOEU.png', renderView1, ImageResolution=[1364, 605])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [343.92459395072444, -376.25237564687177, 447.20957240605503]
renderView1.CameraFocalPoint = [261.0108588956484, 233.67288593478395, -17.39878436508249]
renderView1.CameraViewUp = [-0.040012234163000995, 0.6020305232950466, 0.7974699180147033]
renderView1.CameraParallelScale = 353.6042986164054
