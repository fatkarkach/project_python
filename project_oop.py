from abc import  ABC,abstractmethod
class Person():
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def __str__(self):
        return  self._name +' '+ str(self._age)
    @classmethod
    def from_birth(cls,name,year):
        return cls(name,2020-year)
class Employees(Person,ABC):
    def __init__(self,name,age,salaire):
        super().__init__(name,age)
        self._salaire=salaire
    @abstractmethod
    def show_salaire(self):
        pass
        # print("le salaire est " ,self._salaire)
class Manager(Employees):
    def show_salaire(self):
        print("le salaire est ", self._salaire)
p=Person("fatma",20)
print(p)
# e=Employees("lhoussaine",27,7000000)
# e.show_salaire()
m=Manager("fatma",24,600000)
m.show_salaire()
p2=Person.from_birth("mohamed",2004)
print(p2)