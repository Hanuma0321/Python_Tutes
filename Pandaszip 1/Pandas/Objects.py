#id() is used for printing refernce value of a object
#In pyhton everything is a object only
# when we use '==' operator it checks the value
# when we use 'is' operator it checks the reference

a = 10
print(id(a))
b = a
print(id(b))
print(a is b, a == b)
a = 20
print(id(a))
#-------------------------
x = 10
y = 10
print(id(x), id(y))
print(x==y, x is y)
#----------------------------
l1 = [1,2,3]
l2 = [1,2,3]
print(id(l1),id(l2))
print(l1 is l2, l1 == l2)