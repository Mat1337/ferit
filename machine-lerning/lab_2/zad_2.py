#####################
#     Zadatak 2     #
#####################

"""
    U direktoriju PSU_LV/LV2/ nalazi se datoteka mtcars.csv koja sadrži različita mjerenja provedena na 32
    automobila (modeli 1973-74). Opis pojedinih varijabli nalazi se u datoteci mtcars_info.txt.

        a) Učitajte datoteku mtcars.csv pomoću:
            data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
            delimiter=",", skiprows=1)
        b) Prikažite ovisnost potrošnje automobila (mpg) o konjskim snagama (hp) pomoću naredbe matplotlib.pyplot.scatter.
        c) Na istom grafu prikažite i informaciju o težini pojedinog vozila (npr. veličina točkice neka bude u skladu sa težinom wt).
        d) Izračunajte minimalne, maksimalne i srednje vrijednosti potrošnje (mpg) automobila.
        e) Ponovite zadatak pod d), ali samo za automobile sa 6 cilindara (cyl).
"""

#   #      0      1      2      3      4      5      6      7     8       9      10
# "car", "mpg", "cyl", "disp", "hp", "drat", "wt", "qsec", "vs", "am", "gear", "carb"

import numpy as np
import matplotlib.pyplot as plot

with open("../assets/mtcars.csv", "rb") as file:
    data = np.loadtxt(file, usecols = (1, 2, 3, 4, 5, 6), delimiter = ",", skiprows = 1)

    mpg = data[:, 0:1]
    hp = data[:, 3:4]
    wt = np.fromiter(data[:, 5:6], dtype=float)

    mpg_6L = []
    for entry in data[:, 0:2]:
        if (entry[1] == 6):
            mpg_6L.append(entry[0])

print("[**][MPG]: min=%.5f, max=%.5f, avg=%.5f" % (np.min(mpg), np.max(mpg), np.average(mpg)))
print("[6L][MPG]: min=%.5f, max=%.5f, avg=%.5f" % (np.min(mpg_6L), np.max(mpg_6L), np.average(mpg_6L)))

plot.scatter(mpg, hp, linewidths = wt)
plot.ylabel("hp")
plot.xlabel("mpg")
plot.show()