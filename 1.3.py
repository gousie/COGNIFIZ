import pandas as pd

df = pd.read_csv('Railway_info.csv')
df['Source_Station_Name'] = df['Source_Station_Name'].fillna('UNKNOWN').str.upper().str.strip()
df['Destination_Station_Name'] = df['Destination_Station_Name'].fillna('UNKNOWN').str.upper().str.strip()
df['days'] = df['days'].fillna('UNKNOWN').str.upper().str.strip()
df['Train_Name'] = df['Train_Name'].fillna('UNKNOWN').str.upper().str.strip()
df['Train_No'] = df['Train_No'].astype(str).str.zfill(5)
print(df.head(10))
print(df.isnull().sum())
