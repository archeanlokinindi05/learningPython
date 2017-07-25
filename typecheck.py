def numType(num):
    print (num, 'is')
    if isinstance(num, (int, float, long, complex)):
        print("number of type:")
        print(type(num).__name__)
        else:
            print("not a number at all")
    
