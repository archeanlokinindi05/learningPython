import os
#ls=os.linesep
while True:
    if os.path.exists(maketextfile.py):
        print("Error: '%s'" %fname)
        #break
        else:
           break
        all=[]
        print("\n Enter lines\n")
        while True:
            entry=input('>')
            if entry == '.':
                break
            else:
                all.append(entry)
                fobj=open(fname,'w')
                fobj.writelines(['%s%s'%(x,ls) for x in all])
                fobj.close()
                
              
