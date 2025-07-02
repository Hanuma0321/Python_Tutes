#simple class and object creation.
class Emp :
    num = 100  #class variable
    def __init__(self) :
        self.num = 20   #instance variable

e1 = Emp()
e1.num = 10

print(e1.num)   #instant variable modification belong sto that variable only
print(Emp.num)   #class varaible doesn't modify through object

#modifying value of obj
e1.num = 55
print(e1.num)

del e1
#print(e1) - gives error because e1 deleted
'''---------------------------------------------------------------------------------------------------------------'''

class Company :
    def __init__(self, campus, location) :
        self.campus = campus
        self.location = location
    
lti = Company('Goapalan','Bengaluru')

mindtree = Company('stpi','Bengaluru')

print(lti)  #<__main__.Company object at 0x0000024C7D94ABD0>  without __str__()
print(mindtree) #<__main__.Company object at 0x0000024C7D94AD20> without __str__()

'''---------------------------------------------------------------------------------------------------------------'''
class Company :
    def __init__(self, campus, location) :
        self.campus = campus
        self.location = location
    
    def __str__(self) :
        return "office campus name is {} and location is {}.".format(self.campus,self.location)
lti = Company('Goapalan','Bengaluru')

mindtree = Company('stpi','Bengaluru')

print(lti)  #office campus name is Goapalan and location is Bengaluru. with __str__()
print(mindtree) #office campus name is stpi and location is Bengaluru. with __str__()

'''---------------------------------------------------------------------------------------------------------------'''
