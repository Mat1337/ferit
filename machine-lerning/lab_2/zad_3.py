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

# read the image into a buffer
img = plt.imread("../assets/images/tiger.png", "png")

# copy the image into a gray-scale buffer
img = img[:,:,0].copy()

# get the width & the height of the image
height, width = img.shape

# show the base image
show(img)

# increasing the brightness
for i in range(0, len(img)):
    for j in range(0, len(img[i])):
        img[i][j] = img[i][j] * 1.75
        if (img[i][j] > 1.0):
            img[i][j] = 1.0
show(img)

# rotate the image 90deg clockwise
rotated_img = np.zeros((width, height))
for y in range(height):
    rotated_img[:, height - 1 - y] = img[y, :]
show(rotated_img)

# mirror the image
rotated_img = np.zeros((height, width))
for y in range(height):
    rotated_img[y] = img[height - 1 - y]
show(rotated_img)

# scaled down the image
show(img[::10, ::10])

# clip the image
clipped_img = np.zeros((height, width))
clip_size = width // 4
clipped_img[:, clip_size : clip_size * 2] = img[:, clip_size : clip_size * 2]
show(clipped_img)