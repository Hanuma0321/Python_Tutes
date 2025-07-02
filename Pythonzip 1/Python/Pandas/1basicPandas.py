import pandas as pd

employees = {
    'psid':[1126,1826,1344],
    'empName' : ['manu','getha', 'suman']
}


dataset = pd.DataFrame(employees)
print(dataset['psid'][0])
