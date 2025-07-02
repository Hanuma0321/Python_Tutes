'''
df.head() - gives top 5 rows
df.head(no.of.rows) - gives first n number pof rows
df.tail() - last 5 rows
df.tail(no.of.rows) - give n numberof rows from last
'''

import pandas as pd

data = pd.read_csv('C:\\Users\\10731126\\Downloads\\student_marks.csv')
df = pd.DataFrame(data)

print(df.head())
print("------------------------")
print(df.head(15))
print("------------------------")
print(df.tail())
print("------------------------")
print(df.tail(7))