import pandas as pd

df = pd.read_csv('Railway_info.csv')
print(f"Number of trains = {len(df)}")
print(f"Number of unique source stations = {len(df['Source_Station_Name'].unique())}")
print(f"Number of unique destination stations = {len(df['Destination_Station_Name'].unique())}")
print(f"Most common source station = {df['Source_Station_Name'].value_counts().idxmax()}")
print(f"Most common destination station = {df['Destination_Station_Name'].value_counts().idxmax()}")


