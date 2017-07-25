import sys

q=[]

for i in range(1,10,1):
    x=int(input('Enter Op for Q:\n 1)Push-1\n2)Pop-2\n3)Pop from first\n4)View\n5)Reversal\n'))
    if(x==1):
        y=int(input('Enter element into Q'))
        q.append(y)
        print(q)
    else:
        pass
    if(x==2):
        if(len(q)==0):
            print('Q empty')
        else:
            print(q.pop())
            print('Removed from behind')
            print('Q is')
            print(q[:])
    else:
        pass
    if(x==3):
        if(len(q)==0):
            print('Q is empty')
        else:
            print('First element removed')
            print(q[1:])
    else:
        pass
    if(x==4):
        print(q[:])
    else:
        pass
    if(x==5):
        print(q[::-1])
    else:
        pass
