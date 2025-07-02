'''Sort() method is used for sorting the data. it changes in the original variable.
sorting order - only number digits first
                - alphanumeric( upper, lower)
default : ascending order
for desc : sort(reverse = True)'''



lis = ['mnb','wertyu','rtyu','mki','m56']
lis.sort()
print(lis) #o/p : ['m56', 'mki', 'mnb', 'rtyu', 'wertyu']

lis1 = ['Mnb','wertyu','rtyu','mki','m56']
lis.sort(reverse = True)
print(lis1) #o/p : ['Mnb', 'wertyu', 'rtyu', 'mki', 'm56']


lis3 = ['M','m','3','M3']
lis3.sort(reverse = True)
print(lis3)

lis4 = ['M','m','3','M3']
lis4.reverse()
print(lis4)