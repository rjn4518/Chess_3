import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plot

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Flatten(input_shape=(64,2)))
model.add(tf.keras.layers.Dense(50, activation="relu", name="layer1"))
model.add(tf.keras.layers.Dense(100, activation="relu", name="layer2"))
model.add(tf.keras.layers.Dense(50, activation="relu", name="layer3"))
model.add(tf.keras.layers.Dense(22, name="output"))

model.summary()