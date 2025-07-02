'''
dict1.pop('key_name') - specific item
dict1.popitem() - last item
del dict1['key_name']
del dict1 - deletes enitre dictionary
dict1.clear() - empties the dict'''

emp = {
    'id': 1126, 
    'Name': 'Manu', 
    'age': 22, 
    'dpmanin': 'data'}

print(emp)

emp.pop('age')
print(emp)

emp.popitem()
print(emp)

del emp['id']
print(emp)

emp.clear()
print(emp)

del emp
#print(emp) gives error because dict has deleted so