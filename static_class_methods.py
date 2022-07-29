class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def make_emaile(self):
        if student.isChild(self.age):return "error"
        else : return self.name + '.'  + "@student.com"
    @staticmethod
    def isChild(age):
        if(age>20):return True
        else: return False
    @classmethod
    def birth(cls,name,year):
        return cls(name,2020-year)
# s1=student("fatma",23)
# s2=student("lhoussaine",12)
# print(s1.make_emaile())
# print(s2.make_emaile())
s3=student.birth("fatma",1998)
print(s3.age)
