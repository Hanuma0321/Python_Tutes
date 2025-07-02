'''                             Tuple
1. Tuple is collection data type. it is ordered and immutable.
2. We cant add, delete and change items in tuple
3. we can tuple to tuple
4. If we want to add or delete into tuple, first we need to convert into list then again to tuple
5. we can delete duple byusing "del" keyword'''


#tuple is acollection data types and itemas are immutable
tup = (1,4.5,'Manu')
print(tup)
print(tup[1])

for t in tup :
    print(t)

#we can only concate tuple only, cant int
#print(tup + 4) : error
print(tup + (4,)) #single value tuple has to be like this. Otherwise it would be integer

print(tup * 3)

#we cannot change thee tuple
'''tup[1] = 4
print(tup) : error''' 

#first we needto convert into list then convert into tuple
tup = list(tup)
tup[1] = 4
tup = tuple(tup)
print(tup)

#but we can add tuple to tuple
tup = tup + (4,6,'suman')
print(tup)