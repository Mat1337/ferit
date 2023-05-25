import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image 
from sklearn.cluster import KMeans

# ucitaj sliku
img = image.imread("example_grayscale.png") 

# prikazi sliku
plt.figure()
plt.title('Original image')
plt.imshow(img, cmap='gray')
plt.show() 


# TODO: predstavi sliku kao vektor



# TODO: primijeni K-means na vektor (sliku)



# TODO: zamijeni svjetlinu svakog piksela s najblizim centrom



# TODO: prikazi dobivenu aproksimaciju (sliku)
