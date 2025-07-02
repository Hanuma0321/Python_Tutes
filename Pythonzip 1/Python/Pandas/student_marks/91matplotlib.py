'''
matplotlib is low level visualisatiob libary in python
data visualisation
pip install matplotlib

import matplotlib.pyplot as plt

plt.plot()
plt.show()
'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\10731126\\Downloads\\student_marks_dups.csv")
df = pd.DataFrame(data)

df.plot()
plt.show()

plt.pie(df['total'])
plt.show()

plt.plot(df['total'],df['telugu'])
plt.show()