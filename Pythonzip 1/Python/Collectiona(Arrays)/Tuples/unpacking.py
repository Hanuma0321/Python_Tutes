'''while unpacking number of variables count should be equal to number of iteams in tuple'''
tup = (4,5.6,True,'manu')
(id, height, status, name) = tup
print(id)
print(height)
print(status)
print(name)

'''we can use asterisk '*' when we dont know iteams count'''

tup2 = (1,6,False,'Hi')
(id1, *emp) = tup2

print(id1)
print(emp) #converted to list