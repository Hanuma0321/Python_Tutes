'''
by using '=' assignement operator we assign the reference.
so if we modify one list it reflect to another list also.

by using copy() method it doesnt happen
'''
lis1 = [2,3,4,5]
lis2 = lis1
lis2[1] = 10
print(lis1,lis2)

lis3 = [2,3,4,5]
lis4 = lis3.copy()
lis4[1] = 10
print(lis3, lis4)