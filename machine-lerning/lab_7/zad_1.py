from tensorflow.keras.preprocessing import image_dataset_from_directory
from keras import Sequential
from keras.layers import Dense
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
from sklearn.metrics import confusion_matrix

train_ds = image_dataset_from_directory(
    directory='../assets/gtsrb/Train/',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(48, 48)
)
test_ds = image_dataset_from_directory(
    directory='../assets/gtsrb/Test/',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(48, 48)
)

# Create the model
model = Sequential()

model.add(layers.Conv2D(32, padding='same', kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 3)))
model.add(layers.Conv2D(32, kernel_size=(3, 3), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Dropout(0.2))

model.add(layers.Conv2D(64, padding='same', kernel_size=(3, 3), activation='relu'))
model.add(layers.Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Dropout(0.2))

model.add(layers.Conv2D(128, padding='same', kernel_size=(3, 3), activation='relu'))
model.add(layers.Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Dropout(0.2))

model.add(layers.Flatten())
model.add(layers.Dense(512, activation="relu"))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(43, activation="softmax"))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(train_ds, epochs=1, batch_size=32)

loss_and_metrics = model.evaluate(test_ds, verbose=0)
print("Test Loss: ", loss_and_metrics[0])
print("Test accuracy: ", loss_and_metrics[1])

# TODO: spremi model
model.save("../StreetSignData/")
model.summary()
