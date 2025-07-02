#tuples are like arrays only
#LOOPING BY USING for each loop

tup1 = (456,'fg',6789)
print('USING for each loop')
for t in tup1 :
    print(t)

#by using for loop with range() and len()
tup2 =(2,4,6,3)
print('using for loop with range() and len()')
for i in range(len(tup2)) :
    print(tup2[i])

for i in range(0,len(tup2)) :
    print(tup2[i])

# bu isng while loop
i = 0
print('isng while loop')
while i < len(tup2) :
    print(tup2[i])
    i = i+1
