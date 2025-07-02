class Car :
    def action(self):
        print('move')

class Boat :
    def action(self) :
        print('sail')

class Bike :
    def action(self) :
        print('ride')

c= Car()
bt = Boat()
bk = Bike()

for x in (c,bt,bk) :
    x.action()