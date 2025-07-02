global f
try :
    f = open('wish.txt','r')
    print(f.read())
except :
    print('no file found')

else :
    print('data prinited')
    