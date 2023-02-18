import numpy as np
import matplotlib.pyplot as plt

years = ['2018','2019','2020','2021','2022']
nuclear = [8.2,8.8,9.5,9.6,10.5]
wind = [6.5,7.0, 6.3, 6.08, 6.0]

fig, ax = plt.subplots()
ax.plot(years, nuclear, linestyle='--', color='b', label="Coût d'électricité par Kw/h pour l'énergie nucléaire")
ax.plot(years, wind, linestyle='-', color='r', label="Coût d'électricité par Kw/h pour l'énergie éolienne")

for i in range(len(years)):
    ax.annotate(str(nuclear[i]), xy=(years[i], nuclear[i]), xytext=(years[i], nuclear[i]+0.05), ha='center')
    ax.annotate(str(wind[i]), xy=(years[i], wind[i]), xytext=(years[i], wind[i]+0.15), ha='center')

ax.set_xlabel("Année")
ax.set_ylabel("Coût en ¢")
ax.legend()
plt.title("Coût d'électricité aux québécois")

plt.show()