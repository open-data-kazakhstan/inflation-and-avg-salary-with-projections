import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file = 'data/csv_infl.csv'
df = pd.read_csv(file)

print(df)

inflation_list = df['inflation'].values.tolist()
print(inflation_list)

val = 22433

print(inflation_list[15])

x = 0
k = 15
product = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,26400,0]
for i in range(0,15):
    y = inflation_list[k]
    product[k-1] = val/((y/100) +1)
    val = product[k-1]
    k = k-1

    print(product)
