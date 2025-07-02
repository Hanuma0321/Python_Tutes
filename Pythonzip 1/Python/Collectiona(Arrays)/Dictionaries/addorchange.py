'''
for adding new values
for changing or updating existed values
we use these methods
1. dict1['key_name] = value
2. dict1.update({'key' : value})

note :
------
if those doesnt exist then it will add as new values'''

emp = {
    'id' : 1126,
    'Name' : 'Manu'
}
print(emp)

#adding new values
emp['age'] = 22
emp.update({'dpmanin' : 'data'})

print(emp)

#updating/modifying/changing exited values
emp['id'] = 10731126
emp.update({'Name' : 'manikanta'})

print(emp)