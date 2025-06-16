import pandas as pd

df = pd.read_csv('Railway_info.csv')
saturday_trains = df[df['days'] == 'Saturday']
specific_station = 'PUNE JN.'
pune_trains = df[df['Source_Station_Name'] == specific_station]
print(saturday_trains.head(10))
print(pune_trains.head(10))
