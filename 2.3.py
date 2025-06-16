import pandas as pd

df = pd.read_csv('Railway_info.csv')
df['day_category'] = df['days'].apply(lambda x: 'Weekend' if x in ['Saturday', 'Sunday'] else 'Weekday')
print(df.head(10))
