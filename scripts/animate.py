import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

file = 'data/csv_expanded.csv'
df = pd.read_csv(file)
plt.style.use('dark_background')
fig = plt.figure(figsize=(9,16))
axes = fig.add_subplot(1,1,1)
axes.set_ylim(0, 4200)
axes.set_xlim(2007, 2050)
plt.style.use("seaborn")


x_1,y_1 = [], []
y2 = []

def formate_salary(salary):
    salary_str = str(salary)
    if len(salary_str)> 6:
        res = salary_str[0] + ' ' +salary_str[1:]
        res = res[:-3] + ' ' + res[-3:]
    else: 
        res = salary_str[:-3] + ' ' + salary_str[-3:]
    return res


def animate(i):
    x_1.append(df['year_exp'][i])
    y_1.append(df['inflation_growth'][i])
    y2.append(df['salary_depend'][i])
    plt.plot(x_1, y_1, color='yellow', label = 'Рост инфляции(%)')
    plt.plot(x_1, y2,color='#E6825D', label = 'Рост Зарплат(%)')
    plt.plot([], [], ' ', label=f"Год: {df['year'][i]}")
    plt.plot([], [], ' ', label=f"Рост инфляции: {round(df['inflation'][i],2)}%")
    plt.plot([], [], ' ', label=f"Средняя зарплата: {formate_salary(df['salary_avg'][i])} тенге")
    plt.legend(['Рост инфляции(%)', 'Рост Зарплат(%)', f"Год: {df['year'][i]}", f"Рост инфляции: {round(df['inflation'][i],2)}%", f"Средняя зарплата: {formate_salary(df['salary_avg'][i])}"], loc ="upper left")
    for edge in ['top', 'right']:
        axes.spines[edge].set_visible(False)
    axes.tick_params(left = False)
    plt.suptitle('Показатели инфляции и средней зарплаты с 2007 по 2050', size=17, weight='bold')
    #plt.suptitle(f"Рост инфлияции и средней зарплаты по сравнению с 2007 годом на {df['year'][i]} год", size= 14, weight='bold')
    #plt.text(2010, 3500, f"Год: {df['year'][i]}", bbox = {'facecolor': 'black', 'alpha': 0.5, 'pad': 8,  'ec': 'black'}, fontsize= 15)
    
#plt.legend(fontsize = '10', loc ="upper left")
plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'grey'
plt.rcParams['ytick.color'] = 'grey'
animation = FuncAnimation(fig,animate, frames=range(0, len(df)+1), interval = 5)
# animation.save('inflation_gif.gif', dpi=100, writer=PillowWriter(fps=150)) # Script for saving
# plt.legend()
plt.show()



# plt.legend()
# plt.show()