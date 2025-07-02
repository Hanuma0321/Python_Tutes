
import pandas as pd
data = pd.read_csv("C:\\Users\\10731126\\Downloads\\student_marks.csv")
df = pd.DataFrame(data)

#just like dictionaries, we add new column by it's name and one default value
df['total'] = 0

print(df)

df['total'] = df['telugu'] + df['english'] + df['maths']

print(df)

df['avg'] = df['total']/3
print(df)

df['percentange(%)'] = df['total']/300*100
print(df)