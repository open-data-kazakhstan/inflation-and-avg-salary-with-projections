import pandas as pd

file1 = 'data/inflation_final.csv'
df_ml = pd.read_csv(file1)

print(df_ml)

file2 = 'archive/csv_wranged.csv'
df_org = pd.read_csv(file2)
df_org = df_org[['year', 'inflation', 'salary_increase', 'salary_avg', 'inflation_growth', 'salary_depend']]
print(df_org)

year = df_ml['year'].values.tolist()
inflation_growth = df_ml['inflation_growth'].values.tolist()
salary_depend = df_ml['salary_depend'].values.tolist()
salary_avg = [50910]
inflation = [10.846836]
price = [100]

for i in range(0,len(salary_depend)):
    x = ((salary_depend[i]/100+1))*salary_avg[0]
    salary_avg.append(x)


for i in range(0, len(inflation_growth)):
    x = ((inflation_growth[i]/100)+1)*price[0]
    price.append(x)
   

for i in range(1,len(price)):
    x = ((price[i]/price[i-1])-1)*100
    inflation.append(x)
year.insert(0,2007)
salary_depend.insert(0, 0)
inflation_growth.insert(0,0)

print('salary avg',salary_avg)
print('funny price = ', price)   
print('inflation =', inflation)
print('years', year)
print('infl_grow', inflation_growth)
print('salar_dep',salary_depend)

df_final = pd.DataFrame(list(zip(year, salary_avg, inflation, inflation_growth, salary_depend)),
               columns =[['year', 'salary_avg', 'inflation', 'inflation_growth', 'salary_depend']])
print(df_final)

df_final.to_csv('data/predict.csv')

# df_merged = pd.merge(df_ml, df_org, how='outer', on = ['year', 'inflation_growth', 'salary_depend'])

# print(df_merged)