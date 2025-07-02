'''try - for testing error for block of ConnectionAbortedError
except - handle that TabError
else - whenno error it will be executed
finally - execute anyway'''


'''
#without exception handling
print(x)
'''
#with exception handling
#this 1 error coming due to x not defined
try :
    print(x)
except :
    print('variable not defined')