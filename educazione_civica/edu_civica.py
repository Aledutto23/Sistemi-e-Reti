import matplotlib.pyplot as plt
import csv

mesi_n = []
giacca = []
scuola = []
temp = []
videogame = []
data_file = open("./dati.csv")
data_reader = csv.reader(data_file, delimiter=',')
for row in data_reader:
    mesi_n.append(int(row[0]))
    temp.append(int(row[1]))
    giacca.append(int(row[2]))
    scuola.append(int(row[3]))
    videogame.append(int(row[4]))

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle('Educazione Civica')

ax1.plot(mesi_n, temp, 'o-g')
ax1.set_xlabel('Mese')
ax1.set_ylabel('temperatura media')

ax2.plot(mesi_n, giacca, 'o-r')
ax2.set_xlabel('Mese')
ax2.set_ylabel('Media uso giacca')

ax3.plot(mesi_n, scuola, 'o-b')
ax3.set_xlabel('Mese')
ax3.set_ylabel('media scuola')

ax4.plot(mesi_n, videogame, 'o-y')
ax4.set_xlabel('Mese')
ax4.set_ylabel('Media videogame')

plt.show()