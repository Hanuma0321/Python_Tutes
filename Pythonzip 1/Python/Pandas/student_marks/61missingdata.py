'''
when data containes empty places without values, we can fill with default values otherwise we can delete.
df.fillna(100)
df['telugu'].fillna(0)

df.dropna()
df.dropna(inplace = True)
'''

import pandas as pd
data = pd.read_csv("C:\\Users\\10731126\\Downloads\\student_marks_dups.csv")
df = pd.DataFrame(data)

#for filling missing data
print(df.fillna('no data'))
print(df['english'].fillna(0))

#for dropping
print(df.dropna())

#for permanent dropping
print(df.dropna(inplace=True))

print(df.loc[df['maths']>50])