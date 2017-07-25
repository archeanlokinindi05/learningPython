class Test:
    def __init__(self,name,phone,loc):
        self.name=name
        self.phone=phone
        self.loc=loc
    def uph(self,phone):
        self.phone=phone
        print('Updated phone for',self.name)
    def unm(self,name):
        self.name=name
        print('Updated name for',self.name)
    def loc(self,loc):
        self.loc=loc
        print('Updated',self.loc)
    
class Test1(Test):
    def __init__(self,name,phone,loc,zipc):
        #self.name=name
        #self.phone=phone
        Test.__init__(self,name,phone,loc)
        #self.loc=loc
        self.zipc=zipc
    def email(self,email):
        self.email=email


Bob=Test("Bob",806,'NewYork')
print (Bob.name)
print (Bob.phone)
print(Bob.loc)
Sam=Test("Sam",805,'Boston')
print (Sam.name)
print (Sam.phone)
print(Sam.loc)
Hec=Test("Hec",804,'California')
print (Hec.name)
print (Hec.phone)
print(Hec.loc)
f=Test("Arc",807,'Lubbock')
print (f.name)
print (f.phone)
print(f.loc)
f.uph(808)    
print(f.phone)
f.unm('Archean')
print(f.name)
Joe=Test1("Joe",808,'IND',530016)
print(Joe.name)
print(Joe.phone)
print(Joe.loc)
print(Joe.zipc)
Joe.email("Joe@gmail.com")
print(Joe.email)
