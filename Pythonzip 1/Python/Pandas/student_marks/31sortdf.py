'''
we can sort the dataframe in asc and desc. by default ascending.
i. df.sort_values(col_name) - asc
ii. df.sort_values(col_name,ascending=False)
'''
import pandas as pd

data = pd.read_csv("C:\\Users\\10731126\\Downloads\\student_marks.csv")
df = pd.DataFrame(data)

#asc of names
print(df.sort_values('name'))

#desc of telugu
print(df.sort_values('telugu',ascending = False))

#names in ascending and maths in desc
print(df.sort_values(['name','telugu'], ascending=[1,0]))