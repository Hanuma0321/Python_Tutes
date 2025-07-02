'''
Method	Description
lis.append(element or list)	Adds an element at the end of the list
lisclear()	Removes all the elements from the list
lis.copy()	Returns a copy of the list
lis.count(item)	Returns the number of elements with the specified value
lis.extend(anoter list)	Add the elements of a list (or any iterable), to the end of the current list
lis.index(item)	Returns the index of the first element with the specified value
lis.insert(index,item)	Adds an element at the specified position
pop(index or empty -removes last element)	Removes the element at the specified position
remove(item)	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

lis = [4,6,6,4,6,5,8]
print(lis)

lis.append(10)
print(lis)
lis.append([30,40])
print(lis)

lis.extend([50,60])
print(lis)

lis.insert(0,9)
print(lis)

lis.pop()
print(lis)
lis.pop(9)
print(lis)

print(lis.index(6))

print(lis.count(6))

lis.sort()
print(lis)

lis.sort(reverse = True)
print(lis)

lis2 = [5,654,543,6,6]
lis2.reverse()
print(lis2)
