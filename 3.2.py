import pandas as pd
from scipy.stats import chi2_contingency

df = pd.read_csv('Railway_info.csv')
day_counts = df['days'].value_counts().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], fill_value=0)
day_train_table = pd.DataFrame({'Day': day_counts.index, 'Train_Count': day_counts.values})
contingency_table = pd.crosstab(df['days'], df['Train_Name'])
chi2, p_value, _, _ = chi2_contingency(contingency_table)
print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p_value}")
print(day_train_table)

source_counts = df.groupby('Source_Station_Name').size().reset_index(name='train_count')
busy_stations = source_counts[source_counts['train_count'] > source_counts['train_count'].quantile(0.75)]
busy_station_days = df[df['Source_Station_Name'].isin(busy_stations['Source_Station_Name'])].groupby(['Source_Station_Name', 'days']).size().unstack(fill_value=0)
print(busy_station_days)
