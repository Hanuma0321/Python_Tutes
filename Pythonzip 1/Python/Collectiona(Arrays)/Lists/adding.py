'''for adding elements there are 3 methods
1. append() : to add at the end of the list
2. extend() : to extend the list with another list or tuple or set
3. insert() : to add at particular inndex withour removing the element'''

lis1 = [1,2,3,4,5]
lis2 = [6,7,8,9,0]

lis1.append(67)
#lis2.extend(89) int object cant iterable so we cant use this with extend
lis2.extend([89])
lis2.insert(0,3)
print(lis1)
print(lis2)