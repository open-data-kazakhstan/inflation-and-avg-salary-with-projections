import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

file = 'data/csv_expanded.csv'
df = pd.read_csv(file)
plt.style.use('dark_background')
fig = plt.figure(figsize=(9,16))
axes = fig.add_subplot(1,1,1)
axes.set_ylim(0, 700)
axes.set_xlim(2007, 2025)
plt.style.use("seaborn")


x_1,y_1 = [], []
y2 = []
def animate(i):
    x_1.append(df['year_exp'][i])
    y_1.append(df['inflation_growth'][i])
    y2.append(df['salary_depend'][i])
    plt.plot(x_1, y_1, color='yellow', label = 'Рост инфляции')
    plt.plot(x_1, y2,color='#E6825D', label = 'Рост Зарплат')
    plt.legend(['Рост инфляции', 'Рост Зарплат'])
    for edge in ['top', 'right']:
        axes.spines[edge].set_visible(False)
    axes.tick_params(left = False)
    plt.title(f'''Прирост инфляции по сравнению с прошлым годом:{round(df['inflation'][i],2)}%
Средняя зарплата {df['salary_avg'][i]} тенге''', size=10, weight='bold')
    plt.suptitle(f"Рост инфлияции и средней зарплаты по сравнению с 2007 годом на {df['year'][i]} год", size= 12, weight='bold')
    
plt.legend()
plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
animation = FuncAnimation(fig,animate, frames=range(0, len(df)+1), interval = 30)
# plt.legend()
plt.show()



# plt.legend()
# plt.show()