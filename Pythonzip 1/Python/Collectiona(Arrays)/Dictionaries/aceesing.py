'''
We can access the itemas in a dictionary in different ways
dict1['key_name']
dict1.get('key_name')
dict1.keys() - gives all the key list
dict1.values() - gives all the values'''

emp = {
    'id' : 1126,
    'name' : 'Manu',
    'Domain' : 'Data'
}

print(emp['name'])

print(emp.get('Domain'))

print(emp.keys())

print(emp.values())

print(emp.items())