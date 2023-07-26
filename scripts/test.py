import pandas as pd

file = 'data/csv_infl.csv'
df = pd.read_csv(file)

print(df)

inflation_list = df['inflation'].values.tolist()
print(inflation_list)

price = [100]

x = 100 
k = 0
for i in range(1, len(inflation_list)):
    k = (inflation_list[i]+100)/100*(x)
    price.append(k)
    x = k 

print(price)

j_list = []
for i in price:
    if i == 100:
        j_list.append(0)
    else:
        j_list.append(((i/price[0])-1)*100)
print(j_list)

df['inflation_growth'] = j_list
print(df)

salary = df['salary_avg'].values.tolist()

sal_incr = []
for i in salary:
    if i == 50910:
        sal_incr.append(0)
    else:
        sal_incr.append(((i/salary[0])-1)*100)

print(sal_incr)

df['salary_depend'] = sal_incr
print(df)

df.to_csv('data/csv_wranged')