import sys

class P1:
    def __init__(self):
        self.foo=100
    def foo(self):
        print('P1-foo')
class P2:
    def foo(self):
        print('P2-foo')
    def bar(self):
        print('P2-Bar')
class C1(P1,P2):
    pass
class C2(P1,P2):
    def bar(self):
      print('C2-Bar')
class GC(C1,C2):
    pass


gc=GC()
#gc.foo()
gc.bar()
P2.foo(gc)
P2.bar(gc)
f=issubclass(C1,P1)
print(f)
h=isinstance(gc,GC)
print(h)
p1=P1()
i=hasattr(p1,'foo')
print(i)
j=getattr(p1,'foo')
print(j)
