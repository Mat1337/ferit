import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
from sklearn.cluster import KMeans

# ucitaj sliku
img = image.imread("../assets/images/example.png")
print(img.shape)
(h, w, c) = img.shape

# prikazi sliku
plt.figure()
plt.title('Original image')
plt.imshow(img, cmap='gray')
plt.show()

# TODO: predstavi sliku kao vektor
X = img.reshape(h * w, c)

img_clusters = 4
km = KMeans(n_clusters = img_clusters, random_state=0).fit(X)

# TODO: zamijeni svjetlinu svakog piksela s najblizim centrom

img_approx = km.predict(X)
img_approx = img_approx.astype(np.float32)

for i in range(0, img_clusters):
    print( km.cluster_centers_[i])
    #img_approx[img_approx == i] = km.cluster_centers_[i]