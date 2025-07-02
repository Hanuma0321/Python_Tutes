'''
dictionaries are used to store the data in the "key-value" pairs.
mutable
ordered
no duplicates allowed'''

emp = {
    'id' : 1126,
    'name' : 'Manu',
    'Domain' : 'Data'
}

print(emp)

#print(emp[0]) we can nly access by key only. no index
print(emp['id'])

#dict constructor
newemp = dict(id = 1126, name = 'manu', domain = 'Data')
print(newemp)

#converting list into dict
lis6 = [['id',1], ['name','manu']]
dict = dict(lis6)

print(dict)