import sys
try:
    x=int(input('Enter number to be divided'))
    y=int(input('Enter denom'))
    print(x/y)
except ZeroDivisionError:
    print('Denom should not be zero')
else:
    print('Exception Handled')
