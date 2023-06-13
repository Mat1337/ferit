from tensorflow import keras
from matplotlib import pyplot as plt
from skimage.transform import resize
from skimage import color
import matplotlib.image as mpimg
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image

img_path = '../assets/images/danger_sign.png'
img = image.load_img(img_path, target_size=(48, 48))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0

# TODO: ucitaj istreniranu neuronsku mrezu
model = keras.models.load_model('../StreetSignData/')

# TODO: napravi predikciju
prediction = model.predict(img_array)

# TODO: ispisi predikciju u terminal ili dodaj predikciju u title slike
print(np.argmax(prediction))