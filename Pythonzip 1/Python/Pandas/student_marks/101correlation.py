import pandas as pd

#reading data from the csv file, so mention the filepath correctly and add one more slash at slash
data = pd.read_csv('C:\\Users\\10731126\\Downloads\\student_marks.csv')

#creating dataframe for that data
#dataframe is 2d-data. Like tablura form of rows and columns
df = pd.DataFrame(data)

#to print entire dataframe
print(df)
