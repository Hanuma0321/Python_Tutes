lis = list(range(1,11))
print(lis)

newlis = [x for x in lis if x%2==0] #first x - is outcome, second x- iterate element for each loop, conditdion- filetring
print(newlis)

newlis2 = [x+2 for x in lis]
print(newlis2)