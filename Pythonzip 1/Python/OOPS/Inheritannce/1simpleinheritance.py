class Emp :
    def __init__(self,fname,lname) :
        self.fname = fname
        self.lname = lname

    def fullname(self) :
        print(self.fname,self.lname) 

e1 = Emp('Manikanta','Datti')
e1.fullname()

class E(Emp) :
    pass 

emp1 = E('Ramireddy','Sumanth Reddy')
print(emp1.fullname()) 

'''note :
we didn't mention __init__() in child class.
so ot will go to parent's __init__() when we create object
'''
'''------------------------------------------------------------------------------------------'''

class Emp :
    def __init__(self,fname,lname) :
        self.fname = fname
        self.lname = lname

    def fullname(self) :
        print(self.fname,self.lname) 

e1 = Emp('Manikanta','Datti')
e1.fullname()

class E(Emp) :
    def __init__(self,fname,lname) :
        #Emp.__init__(self,fname,lname)  one way
        super().__init__(fname,lname)  #anoter way

emp1 = E('Ramireddy','Sumanth Reddy')
print(emp1.fullname()) 