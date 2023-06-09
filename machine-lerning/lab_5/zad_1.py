import matplotlib.pyplot as plt
import funkcija_5_1 as fn
from sklearn.cluster import KMeans

X = fn.generate_data(500, 1)

km = KMeans(
    n_clusters = 3, init = 'random',
    n_init = 10, max_iter = 300
)

y_km = km.fit_predict(X)

# plot the 3 clusters
plt.scatter(
    X[y_km == 0, 0], X[y_km == 0, 1],
    s=50, c='lightgreen',
    marker='s', label='cluster 1'
)

plt.scatter(
    X[y_km == 1, 0], X[y_km == 1, 1],
    s=50, c='orange',
    marker='o', label='cluster 2'
)

plt.scatter(
    X[y_km == 2, 0], X[y_km == 2, 1],
    s=50, c='lightblue',
    marker='v', label='cluster 3'
)

# plot the centroids
plt.scatter(
    km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
    s=250, marker='.',
    c='red', label='centroids'
)

plt.legend(scatterpoints=1)
plt.grid()
plt.show()