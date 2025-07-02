'''
df.iloc[] : rows as indexes and columns also as indexes'''
'''note : doesnt include stop value'''
import pandas as pd

data = pd.read_csv('C:\\Users\\10731126\\Downloads\\student_marks.csv')
df = pd.DataFrame(data)

print(df.iloc[3])

print(df.iloc[7,1]) #firest  index column

print(df.iloc[7:12,2:4]) #2 to 3 column data

print(df.iloc[[1,4,5,7],[2,4]])