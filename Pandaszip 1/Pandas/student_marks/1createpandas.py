#importing pandas with alias na me as pd
import pandas as pd

#reading data from the csv file, so mention the filepath correctly and add one more slash at slash
data = pd.read_csv('C:\\Users\\10731126\\Downloads\\student_marks.csv')

#creating dataframe for that data
#dataframe is 2d-data. Like tablura form of rows and columns
df = pd.DataFrame(data)

#to print entire dataframe
print(df)

#to print specific column

print(df['rollno'])
#print(df['name','telugu'])  gives error why because it takes only one argument. so we have to give as list
print(df[['name','telugu']])

#for the df we can't specify like this. for thsi we have methods like loc[] or iloc[]
#print(df[0:3,'telugu']) error

#print(df[0]['telugu']) error
print(df.to_string()) #it gives enitire data without hiding