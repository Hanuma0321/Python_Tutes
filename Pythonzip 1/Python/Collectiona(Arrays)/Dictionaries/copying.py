emp = {
    'id': 1126,
    'Name': 'Manu', 
    'age': 22, 
    'dpmanin': 'data'
    }

emp2 = emp.copy()

emp2 = dict(emp)

'''note : by '=' assigning, refrence is aggined. so modification in one dict causes to changes in anoter dict
these two methods avoid that
copy()
dict()'''