import pandas as pd

file2 = 'archive/csv_wranged.csv'
df_org = pd.read_csv(file2)
df_org = df_org[['year', 'inflation', 'salary_increase', 'salary_avg', 'inflation_growth', 'salary_depend']]
print(df_org)

salary_avg = df_org['salary_avg'].values.tolist()
print(salary_avg)
salary_growth = [0]
for i in range(1,len(salary_avg)):
    x = (salary_avg[i]/salary_avg[i-1]-1)*100
    salary_growth.append(x)
print(salary_growth)

df_org['salary_growth'] = salary_growth

print(df_org)

df_org.to_csv('data/prediction.csv')