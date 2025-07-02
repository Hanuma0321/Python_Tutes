'''
df.loc[] - for row number and for column use column name
'''
import pandas as pd

data = pd.read_csv("C:\\Users\\10731126\\Downloads\\student_marks.csv")
df = pd.DataFrame(data)
print(df.loc[5])

print(df.loc[5,['telugu']])

print(df.loc[1:6])

print(df.loc[5:10,['telugu']])

print(df.loc[1:20:2,['telugu','maths']])

print(df.loc[2:5,'telugu':'maths'])

print(df.loc[df['name'] == 'pavan'])