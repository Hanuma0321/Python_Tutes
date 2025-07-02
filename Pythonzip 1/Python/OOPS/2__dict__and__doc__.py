'''
__str__(self) - method returns the desined format about object  to call   - print(obj_name)
__dict__ - returns all the attributes object  in the dictionary form   to call  print(obj.__dict__)
print(class_name.__dict__) - gives all objects
__doc__ - gives info about he things   to call - print(cls_name.__doc__)

'''
class Company :
    '''this class bout company's campus name and location'''
    def __init__(self, campus, location) :
        self.campus = campus
        self.location = location
    
    def __str__(self) :
        return "office campus name is {} and location is {}.".format(self.campus,self.location)
    
    def status(self) :
        '''transfer status'''
        return f"transfrered to {self.campus} - {self.location}"
    
lti = Company('Goapalan','Bengaluru')

mindtree = Company('stpi','Bengaluru')

print(lti)  #__str__() will be called
print(mindtree)

print(Company.__doc__)  #this class bout company's campus name and location
print(Company.status.__doc__)   #transfer status

print(lti.__dict__) #{'campus': 'Goapalan', 'location': 'Bengaluru'}
print(Company.__dict__)     #'__module__': '__main__', '__doc__': "this class bout company's campus name and location", '__init__': <function Company.__init__ at 0x000001A0AE3A9120>, '__str__': <function Company.__str__ at 0x000001A0AE3A91C0>, 'status': <function Company.status at 0x000001A0AE3A9260>, '__dict__': <attribute '__dict__' of 'Company' objects>, '__weakref__': <attribute '__weakref__' of 'Company' objects>}