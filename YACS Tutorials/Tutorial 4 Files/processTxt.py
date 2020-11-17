import os,sys,re
import pandas as pd

pathToRes = os.path.join('/home/cyprien/Desktop/yacs-example','plate-res.txt')
pathToCsv = os.path.join('/home/cyprien/Desktop/yacs-example','mydata2.csv')

myfile = open(pathToRes,"r")

content = myfile.read()

dispRegex2 = re.compile(r'LA VALEUR (MAX|MIN)IMALE DE (DX|DY|DZ) {2,}EST {1,}(-?\d.\d{14}E-?\+?\d\d) ')

mo2 = dispRegex2.findall(content)

print(mo2)

mydata = pd.DataFrame(mo2,columns=["MIN/MAX","Component","Value"])

mydata.to_csv(pathToCsv)