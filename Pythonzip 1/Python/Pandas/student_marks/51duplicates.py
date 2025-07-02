import pandas as pd
data = pd.read_csv("C:\\Users\\10731126\\Downloads\\student_marks_dups.csv")
df = pd.DataFrame(data)

#for checking duplicates are there or not
print(df.duplicated())

#for deleting duplicates
print(df)
print(df.drop_duplicates())