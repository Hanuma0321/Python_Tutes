import sys
f = open('hi.txt', 'r')
#print(f.read())
for line in f :
    #sys.stdout.write(f)
    #print(line)
    sys.stdout.write(line)
