import pandas as pd

df = pd.read_csv('Railway_info.csv')
print(df.head(10))
print(df.info())
print(df.isnull().sum())
