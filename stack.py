import sys

stack=[]

for i in range(1,100,1):
    
    x=int(input('Enter operations:\n1) Push-1 \n2)Pop-2\n3)View- 3\n'))
    if(x == 1):
        y=int(input('Enter element'))
        stack.append(y)
        print(stack)
    else:
        pass   
    if(x == 2):
        if(len(stack)==0):
            print('empty stack')
        else:
            print(stack.pop())
            print('Removed from stack')
            print('Stack is')
            print(stack[:])
    else:
        pass
    if(x==3):
        print(stack[:])
    else:
            pass
