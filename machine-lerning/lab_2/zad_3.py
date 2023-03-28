#####################
#     Zadatak 3     #
#####################

"""
    Na temelju primjera 2.6. učitajte sliku 'tiger.png'. Manipulacijom odgovarajuće numpy matrice pokušajte:
        a) posvijetliti sliku (povećati brightness),
        b) zarotirati sliku za 90 stupnjeva u smjeru kazaljke na satu,
        c) zrcaliti sliku,
        d) smanjiti rezoluciju slike x puta (npr. 10 puta),
        e) prikazati samo drugu četvrtinu slike po širini, a prikazati sliku cijelu po visini; ostali dijelovi slike trebaju biticrni.
"""

import matplotlib.pyplot as plt
import numpy as np

def show(img):
    plt.figure()
    plt.imshow(img, cmap="gray")
    plt.show()

img = plt.imread("../assets/images/tiger.png", "png")
img = img[:,:,0].copy()
show(img)

# increasing the brightness
for i in range(0, len(img)):
    for j in range(0, len(img[i])):
        img[i][j] = img[i][j] * 1.75
        if (img[i][j] > 1.0):
            img[i][j] = 1.0
show(img)

# rotate the image 90deg clockwise
show(np.rot90(img, axes = (1, 0)))

# mirror the image
show(np.flip(img))