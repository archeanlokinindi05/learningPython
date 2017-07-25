import sys
import string

alphas=['a'|'b']+'_'
nums=range(0,9,1)
myinput=input('Enter Id to check:')
if(len(myinput>1)):
    if(myinput[0] not in alphas):
       print('Invalid')
    else:
       for others in myinput[1:]:
           if(others not in alphas or others not in nums):
               print('invalid')
       #break
else:
       print('ok')
