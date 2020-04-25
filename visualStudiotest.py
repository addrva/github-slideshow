print('home')
print('hello')
print('hi')
#test

import pandas as pd
from pandas import Series, DataFrame
import os
csv = pd.read_csv('/Users/positivitea/Desktop/data/Energy_Usage_2010.csv')
df = DataFrame(csv)
df.head(10)
df.iloc[1,5]
df.loc[1:5,'BUILDING TYPE']

os.listdir(os.chdir('/Users/positivitea/Desktop/data'))