'''
Challenges :
1. have missing data
2. duplicate values
3. add total and percentage columns
4. give pass/fail/first class/distoinction status
5. save these changes in original file'''
import pandas as pd
import matplotlib as mp
data = pd.read_csv("C:\\Users\\10731126\\Downloads\\student_marks_dups.csv")
df = pd.DataFrame(data)

print('------------------------------------------\n',df)


df.fillna(0,inplace=True)   #for filling empty places with default value
df.drop_duplicates(inplace=True)    #dropping duplicates in orginal df
print('------------------------------------------\n',df)

df['total'] = df['telugu'] + df['english'] + df['maths']    #adding total column
df['percentage'] = df['total']/300*100  #adding percentage column
print('------------------------------------------\n',df)

df.loc[(df['percentage']<30),'status'] = 'fail' #adding status column and adding fail if percentage < 30
print('------------------------------------------\n',df)

df.loc[(df['percentage'] >=30) & (df['percentage'] <40),'status'] = 'pass' #adding pass if percentage > 30 and <40
df.loc[(df['percentage'] >= 40) & (df['percentage']<=50), 'status'] = 'First class'#adding pass if percentage >40 30 and <50
df.loc[df['percentage']>=50, 'status'] = 'distinction' #add distinction > =50

print(df)

#with index,saving changes in original file
#df.to_csv("C:\\Users\\10731126\\Downloads\\student_marks_dups.csv")

#without index
df.to_csv("C:\\Users\\10731126\\Downloads\\student_marks_dups.csv",index=False)

print(df.loc[df['status'] == 'fail'])

print(df.loc[(df['status'] == 'pass')])

df.plot()
mp.pyplot.show()