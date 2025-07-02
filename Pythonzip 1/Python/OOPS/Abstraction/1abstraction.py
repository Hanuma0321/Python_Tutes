#for making abstract class
# we have to write 'ABC - means Absarct Base class' inside the () for a class
'''note : we cannot create objs forr abstarct class'''

from abc import ABC,abstractmethod
class Emp(ABC) :

    def __init__(self,name):
        self.name = name
    @abstractmethod
    def ename(self) :
        pass
class Manu(Emp) :
    def ename(self) :
        print(self.name)

m = Manu('Manikanta')
m.ename()