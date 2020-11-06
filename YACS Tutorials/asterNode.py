import os, subprocess, sys

export = '/home/cy/Desktop/plate-tester/platepressure.export'

appliPath = os.path.realpath('/home/cy/salome_meca/V2018.0.1_public/tools/Code_aster_frontend-201801/bin')

proc = subprocess.Popen([os.path.join(appliPath, 'as_run')] + [export], close_fds=True)
out, err = proc.communicate()
