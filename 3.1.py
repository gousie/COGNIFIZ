import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Railway_info.csv')
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_counts = df['days'].value_counts().reindex(day_order, fill_value=0)

plt.figure(figsize=(10, 6))
plt.bar(day_counts.index, day_counts.values, color='#4CAF50')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Train Journeys')
plt.title('Distribution of Train Journeys by Day')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

source_dest_counts = df.groupby(['Source_Station_Name', 'Destination_Station_Name']).size().reset_index(name='trip_count')
popular_routes = source_dest_counts.sort_values(by='trip_count', ascending=False).head(10)
print(popular_routes)
