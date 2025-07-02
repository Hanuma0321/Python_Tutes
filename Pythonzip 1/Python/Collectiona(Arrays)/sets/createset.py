set1 = {}
print(type(set1)) #dict type

set2 = set()
print(type(set2)) #set type

set3 = {1,2,3,4,5,6,7}
print(set3)

set4 = {1,2,3,4,3,3,4,5,6}
print(set4) #doesnt accept duplicates

set5 = {True, 1}
print(set5) #both considered as True

set6 = {False,0}
print(set6) #both considered as False

#accesing throuhh for loop

for x in set4 :
    print(x)

'''Note : since it is unordered we cant access through index'''