''' Strings also collection data type same as tuple only.'''
name = ''.join(['1','2','3','4','5','6'])
print(name)

#formatting string

emp = 'manu'
print(f"hi, {emp}")

print('hi {}'.format(emp))

print('hi {1}, {0}'.format(name,emp))

print('hi {emp}, {name}'.format(name = 'm', emp = 's'))