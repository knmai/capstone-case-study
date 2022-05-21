import numpy as np
import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\karln\iCloudDrive\DataScience Projects\GitHub repos\capstone-case-study\historical_data\BTC-USD.csv")


data.High.max()
data.sample(5)

#drop null value columns
data.dropna()


print(data)

#splitting date into year month day
new_data = data['Date'].str.split("-", expand = True)

print(new_data)

sep_date = pd.concat([data, new_data])

sep_date.drop(['Volume'], axis = 1, inplace = True)

may_movement = sep_date[sep_date['1'] == '06']
print(sep_date)
data.to_csv('set.csv')
#Extracting specific data
april = data[data['Date'] == '2020']

print(april)

#dropping columns from table
april.drop(['Volume', 'Low'], axis = 1, inplace=True)
print(april)