'''for removing items from set we use
remove("item")
discard("item")
pop() - removes random because set is  unoredred'''

set1 = {1,2,3,4,5,6,7,8,8}
set1.pop()
print(set1)
set1.remove(7)
set1.discard(5)
print(set1)