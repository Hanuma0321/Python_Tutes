''''We cant change the elements.
but we ca add new elelments into set'''

#for adding itemas
set1 = {1,2,3,4,5}
set1.add(8)
print(set1)

#set1.add({5,6,7,8,9})
#print(set1)                gives error

#adding one set to another set
set1.update({5,6,7,8,9,0})
print(set1)

set1.update({'i' : 'iron'})
print(set1)
'''Note :
we can add iterable item such as list, tuple,dict'''