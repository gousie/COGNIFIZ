import pandas as pd

df = pd.read_csv('Railway_info.csv')
trains_per_source = df.groupby('Source_Station_Name').size().reset_index(name='train_count')
trains_per_day = df.groupby(['Source_Station_Name', 'days']).size().groupby('Source_Station_Name').mean().reset_index(name='avg_trains_per_day')
print(trains_per_source.head(10))
print(trains_per_day.head(10))
