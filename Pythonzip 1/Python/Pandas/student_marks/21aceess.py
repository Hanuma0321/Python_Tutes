import pandas as pd

data = pd.read_csv("C:\\Users\\10731126\\Downloads\\student_marks.csv")
df = pd.DataFrame(data)

#describe() method decribes the table such as
'''
          rollno     telugu    english      maths
count   20.00000  20.000000  18.000000  19.000000
mean   110.50000  34.000000  39.111111  32.526316
std      5.91608  23.242429  22.756741  22.952532
min    101.00000   2.000000   2.000000   2.000000
25%    105.75000   4.000000  32.250000   4.000000
50%    110.50000  34.500000  35.000000  34.000000
75%    115.25000  54.000000  55.500000  54.000000
max    120.00000  65.000000  87.000000  65.000000
'''

print(df.describe())

#df.shape gives the rows and coulmns as tuple
print(df.shape, type(df.shape))