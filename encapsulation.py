class A():
    def __init__(self):
        # private attribute
        self.__number=10
        # protected attribute
        self._age=12

class B(A):
    pass