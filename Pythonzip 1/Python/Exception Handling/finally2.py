global f 
try :
    f = open('msg.txt', 'x')
    print(f.read())
except :
    print('no file found')
else :
    print('data printed')