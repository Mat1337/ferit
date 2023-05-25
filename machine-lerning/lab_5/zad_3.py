import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
from sklearn.cluster import KMeans

# ucitaj sliku
img = image.imread("../assets/images/example_grayscale.png")
(h, w) = img.shape

# prikazi sliku
plt.figure()
plt.title('Original image')
plt.imshow(img, cmap='gray')
plt.show()

# TODO: predstavi sliku kao vektor
X = img.reshape(h * w, 1)

img_clusters = 3
km = KMeans(n_clusters = img_clusters, random_state=0).fit(X)

# TODO: zamijeni svjetlinu svakog piksela s najblizim centrom
img_approx = km.predict(X)
img_approx = img_approx.astype(np.float32)

for i in range(0, img_clusters):
    img_approx[img_approx == i] = km.cluster_centers_[i]

img_approx = img_approx.reshape(h, w)

# TODO: prikazi dobivenu aproksimaciju (sliku)
plt.figure()
plt.subplot(1, 2, 1)
plt.title("image")
plt.imshow(img, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("compressed image")
plt.imshow(img_approx, cmap='gray')

plt.show()