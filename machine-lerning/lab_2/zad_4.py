#####################
#     Zadatak 3     #
#####################

"""
    Napišite funkciju koja kao povratnu vrijednost daje sliku (polje) sa crno bijelim kvadratima jednake dimenzije koji se
    naizmjenično pojavljuju (vidi primjer slike ispod). Funkcija kao argumente prima veličinu kvadrata u pikselima, broj
    kvadrata po visini i broj kvadrata po širini slike. Za realizaciju ove funkcije koristite numpy funkcije zeros i ones
    kako biste kreirali crna i bijela polja. Kako bi ih složili u odgovarajući oblik, koristite numpy funkcije hstack i
    vstack. Za prikaz grayscale slike koristite naredbu:
        plt.imshow(img, cmap='gray', vmin=0, vmax=255)
"""

import matplotlib.pyplot as plt
import numpy as np

def checkboard(size, y_size, x_size):
    # define the black & white squares
    black = np.zeros((size, size))
    white = black + 255

    rows = []
    for i in range(y_size):
        row = []
        for j in range(x_size):
            if (i + j) % 2 == 0:
                row.append(black)
            else:
                row.append(white)
        rows.append(np.hstack(row))

    img = np.vstack(rows)
    return img

generated_img = checkboard(50, 4, 5)
plt.imshow(generated_img, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()