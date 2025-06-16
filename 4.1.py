import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Railway_info.csv')
day_counts = df['days'].value_counts().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], fill_value=0)
source_counts = df['Source_Station_Name'].value_counts().head(10)
source_day_pivot = df.pivot_table(index='Source_Station_Name', columns='days', aggfunc='size', fill_value=0)
top_stations_pivot = source_day_pivot.loc[source_counts.index]

plt.figure(figsize=(10, 6))
plt.bar(day_counts.index, day_counts.values, color='#1f77b4')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Trains')
plt.title('Number of Trains per Day')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(source_counts.index, source_counts.values, marker='o', color='#ff7f0e')
plt.xlabel('Source Station')
plt.ylabel('Number of Trains')
plt.title('Top 10 Source Stations by Number of Trains')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(top_stations_pivot, cmap='Blues', annot=True, fmt='d')
plt.title('Train Distribution by Day for Top 10 Source Stations')
plt.xlabel('Day of the Week')
plt.ylabel('Source Station')
plt.tight_layout()
plt.show()
