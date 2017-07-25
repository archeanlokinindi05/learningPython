import sys
import math

money=float(input('Enter amount'))
x,y=divmod(money,25)
print(x)
print('Quarters')
a,b=divmod(y,10)
print(a)
print('dimes')
c,d=divmod(b,5)
print(c)
print('nickel')
print(d)
print('cents')

          
