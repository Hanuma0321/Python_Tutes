age = input()

if not age.isdigit() :
    raise ValueError('Enter nuber not strings')

elif not int(age) >= 18 :
    raise ValueError('Not suitable age')

else :
    print("{} age is suitable for voting.".format(age))

