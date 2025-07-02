import pandas as pd
data = pd.read_csv("C:\\Users\\10731126\\Downloads\\student_marks.csv")
df = pd.DataFrame(data)

#before delete column will add a dummy column first
df['for_del'] = 'yes'
print(df)

#now will delete that dummmy column
print(df.drop(columns = 'for_del')) #from this we can no it deletes the column temporarily. not from original
print(df)

#for dleting from original dataframe
df.drop(columns = 'for_del',inplace=True)
print(df)