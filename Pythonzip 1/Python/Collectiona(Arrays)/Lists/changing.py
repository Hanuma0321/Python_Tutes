#changing single value
lis = [34,4,5,3,5,65,4,556,6,55,555,5,4]
lis[1] = 54
print(lis)

#changing range of values
#equal count as range
lis[2:4] = [87,65]
print(lis)

#more count than range
lis[2:4] = [12,23,3,34]
print(lis) #then those extra elements added 

#less count than range
lis[0:3] = [1]
print(list) # those 3 elemets replaced with this single value

''''when we use insert(index,value) method, then no items will be removed'''

lis1 = [6,5,4,4]
lis1.insert(1,7)
print(lis1) #1th index element not removed, it moves to 2nd