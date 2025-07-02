emp = {
    'id': 1126,
    'Name': 'Manu', 
    'age': 22, 
    'dpmanin': 'data'
    }

for x in emp :
    print(x) #gives all keys

for x in emp :
    print(emp[x]) #values

for x in emp.values() : 
    print(x) #values

for x in emp.keys() :
    print(x) #keys

for x,y in emp.items() :
    print(x,y) #keys nd values