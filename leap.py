import sys
def leap():
    num=int(input('Enter year'))
    if(num%4==0 and num%100!=0):
        print('Year is leap year')
    else:
            print('not a leap year')
leap()
