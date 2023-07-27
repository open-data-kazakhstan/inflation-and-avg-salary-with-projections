import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

def formate_salary(salary):
    salary_str = str(salary)
    if len(salary_str)> 6:
        res = salary_str[0] + ' ' +salary_str[1:]
        res = res[:-3] + ' ' + res[-3:]
    else: 
        res = salary_str[:-3] + ' ' + salary_str[-3:]
    return res

file = 'data/csv_expanded2.csv'
df = pd.read_csv(file)
df['salary_avg'] = df['salary_avg'].astype('int')
plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(2, figsize=(9,16))
# ax1 = fig.add_subplot(1,1,1)
ax1.set_ylim(0, 30)
ax1.set_xlim(2008, 2023)

ax2.set_ylim(50000, 360000)
ax2.set_xlim(2008, 2023)
plt.style.use("seaborn")

x_1,y_1 = [], []
y2 = []
y3 = []
def animate(i):
    x_1.append(df['year_exp'][i])
    y_1.append(df['inflation'][i])
    y2.append(df['salary_growth'][i])


    ax1.plot(x_1, y_1, color='yellow', label = 'Рост инфляции(%)')
    ax1.plot(x_1, y2,color='#E6825D', label = 'Рост Зарплат(%)')


    ax1.plot([], [], ' ', label=f"Год: {df['year'][i]}")
    ax1.plot([], [], ' ', label=f"Рост инфляции: {round(df['inflation'][i],2)}%")
    ax1.legend(['Рост инфляции(%)', 'Рост Зарплат(%)', f"Год: {df['year'][i]}", f"Рост инфляции: {round(df['inflation'][i],2)}%"], loc ="upper left")
    for edge in ['top', 'right']:
        ax1.spines[edge].set_visible(False)
    ax1.tick_params(left = False)
    ax1.set_title('Прирост зарплаты и инфляции по годам', size=17, weight='bold')

    y3.append(df['salary_avg'][i])

    ax2.plot(x_1, y3,color='blue', label = 'Средняя зарплата')
    ax2.plot([], [], ' ', label=f"Средняя зарплата: {formate_salary(df['salary_avg'][i])} тенге")
    ax2.legend(['Средняя зарплата в тенге', f"Средняя зарплата: {formate_salary(round(df['salary_avg'][i],-2))}"], loc ="upper left")
    ax2.set_title('Средняя зарплата в Казахстане', size=17, weight='bold')
    
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