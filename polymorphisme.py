class humain():
    count=0
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.fullname=self.firstname+" "+self.lastname
        humain.count+=1
    def make_emaile(self):
        self.email=self.firstname+'.'+self.lastname+"@gmail.com"
        return self.email
    def add_age(self):
        self.age+=1
class student(humain):
    def __init__(self,firstname,lastname,age,field):
        super().__init__(firstname,lastname,age)
        self.field=field
    def make_emaile(self):
        self.email=self.firstname+'.'+self.lastname+"@student.com"
        return self.email
    def __str__(self):
        return self.firstname+" "+self.lastname
    def __gt__(self,other):
        return self.age > other.age
s1=student("fatma","karkach",20,"france")
s2=student("lhoussaine","hssini",24,"dubai")

print(s1>s2)