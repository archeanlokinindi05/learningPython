import sys
import os
try:
fobj=open('myfile.py','w')
except IOError, e:
           print("Error",e)
for eachline in fobj:
    print(eachline)
    fobj.close()
