#nested dictionary
employees = {
    'emp1' : {
        'name' : 'manu',
        'id' : 26
    },
    'emp2' : {
        'name': 'suman',
        'id' : 44
    },
    'emp3' : {
        'name': 'geetha',
        'id' : 26
    }
}

#making multiple dicts into one nested dict
e1 = {
    'id' : 1126,
    'name' : 'manu',
    'domain' : 'data'
}

e2 = {
    'id' : 1344,
    'name' : 'suman',
    'domain' : 'data'
}

e3 = {
    'id' : 1826,
    'name' : 'geetha',
    'domain' : 'data'
}

e = {
    'e1':e1,
    'e2' : e2,
    'e3' : e3
}

print(e)

#accessing
print(e['e1']['id'])

print(e.items())

#accessing through for loop
for x,obj in e.items() :
    print(x)
    for y in obj :
        print(y, obj[y])