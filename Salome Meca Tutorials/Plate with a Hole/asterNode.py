import os, subprocess, sys

export = '/home/cyprien/Desktop/plate_hole/export'

appliPath = os.path.realpath('/home/cyprien/salome_meca2020/V2019.0.3_universal/tools/Code_aster_frontend-20190/bin')

proc = subprocess.Popen([os.path.join(appliPath, 'as_run')] + [export], close_fds=True)
out, err = proc.communicate()
