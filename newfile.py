import sys
from sys import *
from token import *
import re

f=open("myfile.py","r")
print("Name of the file:",f.name)
#f.readline()
line=f.readlines()
print("Read Line: %s" %(line))
#line=fo.readlines(2)
#print("Read Line: %s" %(line))
f.close()
#for i in f:
    #f.read()
   # print(i)
    #f.read()

a='Beautiful, is; better*than\nugly'
re.split(';|,',str)
