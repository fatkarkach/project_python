class A():
    def add(self,x,y):
        return x+y
class B():
    def mul(self,x,y):
        return x*y
class C(A,B):
    pass

c=C()
print(c.add(1,2))
print(c.mul(2,4))
