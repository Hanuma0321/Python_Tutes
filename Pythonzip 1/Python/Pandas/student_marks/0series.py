#series is 1d - data. iit is single coulmun of values
import pandas as pd

data = pd.read_csv('C:\\Users\\10731126\\Downloads\\student_marks.csv')

#ser = pd.Series(data[]) we can't create series for entire data. why because it is 1D
#so specify any single column name

ser = pd.Series(data['name'])
print(ser)

#labelling
#usually when we crete it gives indexes starts from 0. if we want we can customise labels


# l = [1,23,4]
# ser3 = pd.Series(l,index=['one','two','three'])
# print(ser3)

# '''
# Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.

# Example
# Create a simple Pandas Series from a dictionary:

# '''
# #keys as index and 
# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories)

# print(myvar)

# '''
# To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.

# Example
# Create a Series using only data from "day1" and "day2":
# '''

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories, index = ["day1", "day2"])

# print(myvar)