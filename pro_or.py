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

# h1=humain("fatma","karkach",20)
# h2=humain("lhoussaine","hssini",20)
# # print(h1.make_emaile())
# # print(h2.make_emaile())
# # print(h1.age)
# # h1.add_age()
# # print(h1.age)
# print(humain.count)
class student(humain):
    def __init__(self,firstname,lastname,age,field):
        super().__init__(firstname,lastname,age)
        self.field=field
s1=student("fatma","karkach",23,"maroc")
print(s1.field)
print(s1.make_emaile())
class student_university(student):
    pass