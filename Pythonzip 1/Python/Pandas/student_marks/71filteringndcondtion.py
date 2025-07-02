import pandas as pd
data = pd.read_csv("C:\\Users\\10731126\\Downloads\\student_marks_dups.csv")
df = pd.DataFrame(data)

df['total'] = df['telugu'] + df['english'] + df['maths']

df['avg'] = df['total']/3

df['percentange(%)'] = df['total']/300*100

df['status'] = 'pass/fail'
print(df)
#simple condition
print(df.loc[df['english']>50])

#compound condtion
print(df.loc[(df['maths']>50) & (df['maths']<80)])

#we can use any string methods
print(df.loc[df['name'].str.contains('m')])

df.loc[df['percentange(%)']<30,['status']]= 'fail'

print(df)

df.loc[(df['percentange(%)']>=30) & (df['percentange(%)']<40),['status']]='pass'

print(df)

df.loc[(df['percentange(%)']>=40) & (df['percentange(%)']<50),['status']] = 'first class'
print(df)


df.loc[df['percentange(%)']>=50,['status']] = 'distinction'
print(df)