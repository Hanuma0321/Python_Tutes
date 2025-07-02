'''
There are several ways to join two or more sets in Python.

union()/ update()/ | join all items.

intersection() / & joins the commom items.

difference() / - gives items of set which are not in oter.

symmetric_difference() / ^  gives which are not common.'''

set1 = {1,2,3,4,5,9}
set2 = {0,6,7,8,9,3}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)