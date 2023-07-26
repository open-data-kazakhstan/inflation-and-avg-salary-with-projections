import pandas as pd
import numpy as np


file = ('data/predict.csv')
df = pd.read_csv(file)
df['year_exp'] = df['year']

print(df)
df_1 = df
df_1.index = df.index*8
last_idx = df_1.index[-1] + 1
df_expanded = df_1.reindex(range(last_idx))
df_1['year_exp'] = df_1['year']
df_expanded['year'] = df_expanded['year'].fillna(method='ffill')
df_expanded['inflation'] = df_expanded['inflation'].fillna(method='ffill')
# df_expanded['salary_increase'] = df_expanded['salary_increase'].fillna(method='ffill')
df_expanded['salary_avg'] = df_expanded['salary_avg'].fillna(method='ffill')
# df_expanded = df_expanded.interpolate()
df_expanded['inflation_growth'] = df['inflation_growth'].astype('float')
df_expanded['salary_depend'] = df['salary_depend'].astype('float')

df_expanded['year'] = df_expanded['year'].astype('int')
df_expanded['salary_avg'] = df_expanded['salary_avg'].astype('int')
df_expanded = df_expanded.interpolate()
print(df_expanded)
df_final = df_expanded[['year', 'inflation', 'salary_avg', 'inflation_growth', 'salary_depend', 'year_exp']]
print(df_final)



df_final.to_csv('data/csv_expanded.csv')