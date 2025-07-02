'''
slicing :
this as list. when we are giving multiple paramters give as a list'''

'''
Note : this slicing main works on rows'''

import pandas as pd

data = pd.read_csv("C:\\Users\\10731126\\Downloads\\student_marks.csv")
df = pd.DataFrame(data)

print(df[2:5]) #gives 2 to 4 indexed row of all values

print(df[1:11:2]) 

print(df['telugu'])

#when passing multiple column names as list
print(df[['telugu','english']])

print(df['name'][5])

print(df['name'][0:5])