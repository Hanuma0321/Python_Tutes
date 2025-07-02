x = y = z = 1
n = 2

#one way list comprension. it appends the genersted list in each iteration
lis = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(lis)

#manual append()
lis =[]
for i in range(x+1) :
    for j in range(y+1) :
        for k in range(z+1) :
            if i+j+k != n :
                lis.append([i,j,k])

print(lis)