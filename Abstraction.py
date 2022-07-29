from abc import  ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class bird(Animal):
    def move(self):
        print("move from bird")
class cat(Animal):
    def move(self):
        print("move from cat")
        
a=cat()
a.move()
