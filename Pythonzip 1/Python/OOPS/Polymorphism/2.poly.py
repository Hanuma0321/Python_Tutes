class Vehicle :
    def __init__(self,brand) :
        self.brand = brand
    def action(self) :
        print('move')

class Car(Vehicle) :
    pass 

class Bike(Vehicle) :
    def action(self) :
        print('ride')

c = Car('techmahi')
b = Bike('bullet')

print(c.brand)
c.action() #executed from parent class

print(b.brand)
b.action()  #ovverirde the parent method