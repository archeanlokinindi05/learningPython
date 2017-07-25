import sys

try:
    x=int(input('Enter num'))
    y=int(input('Enter num2'))
    x/y
finally:
    print('Exception')
    except ZeroDivisionError:
        print('denom shouldnt be zero')
    else:
        pass
