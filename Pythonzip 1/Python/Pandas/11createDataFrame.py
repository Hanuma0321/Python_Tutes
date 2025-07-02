import pandas as pd

data = pd.read_csv('C:\\Users\\10731126\\Downloads\\netflix_shows.csv')


df = pd.DataFrame(data)
print(df)

for rec in df.iterrows() :
    print(rec)