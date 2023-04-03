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
    black = np.zeros((size, size, 3))
    black[:, :, 2] = 255

    white = np.zeros((size, size, 3))
    white[:, :, 0] = 255


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
plt.imshow(generated_img, vmin=0, vmax=255)
plt.show()

def show(img):
    plt.figure()
    plt.imshow(img)
    plt.show()

# read the image into a buffer
img = plt.imread("../assets/images/tiger.png", "png")

# copy the image into a gray-scale buffer
img = img[:, :].copy()

# show the base image
show(img)

def bright(v, s):
    n = v * s
    if (n > 1):
        n = 1
    return n

# increasing the brightness
for i in range(0, len(img)):
    for j in range(0, len(img[i])):
        img[i][j][0] = bright(img[i][j][0], 1.75)
        img[i][j][1] = bright(img[i][j][1], 1.75)
        img[i][j][2] = bright(img[i][j][2], 1.75)