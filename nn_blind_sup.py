import tensorflow as tf
import keras
import numpy as np
from tensorflow.python.keras.metrics import MeanSquaredError
import coordinates as coord
import matplotlib.pyplot as plot


def nn(_input):
    data = np.zeros(22, 'float32')

    match _input[0]:
        case 10:
            data[0] = 1
        case 11:
            data[1] = 1
        case 12:
            data[2] = 1
        case 13:
            data[3] = 1
        case 14:
            data[4] = 1
        case 15:
            data[5] = 1

    for i in range(8):
        if _input[1] == i * coord.RANK:
            data[6] = 1
        elif _input[1] == coord.FILE + i * coord.RANK:
            data[7] = 1
        elif _input[1] == 2 * coord.FILE + i * coord.RANK:
            data[8] = 1
        elif _input[1] == 3 * coord.FILE + i * coord.RANK:
            data[9] = 1
        elif _input[1] == 4 * coord.FILE + i * coord.RANK:
            data[10] = 1
        elif _input[1] == 5 * coord.FILE + i * coord.RANK:
            data[11] = 1
        elif _input[1] == 6 * coord.FILE + i * coord.RANK:
            data[12] = 1
        elif _input[1] == 7 * coord.FILE + i * coord.RANK:
            data[13] = 1

    if coord.a1 <= _input[1] <= coord.h1:
        data[14] = 1
    elif coord.a2 <= _input[1] <= coord.h2:
        data[15] = 1
    elif coord.a3 <= _input[1] <= coord.h3:
        data[16] = 1
    elif coord.a4 <= _input[1] <= coord.h4:
        data[17] = 1
    elif coord.a5 <= _input[1] <= coord.h5:
        data[18] = 1
    elif coord.a6 <= _input[1] <= coord.h6:
        data[19] = 1
    elif coord.a7 <= _input[1] <= coord.h7:
        data[20] = 1
    elif coord.a8 <= _input[1] <= coord.h8:
        data[21] = 1

    _data = tf.convert_to_tensor(data, 'float32')

    test = keras.ops.zeros(22)

    #print(data)

    model = keras.models.Sequential()

    model.add(keras.Input(shape=(32,)))
    model.add(keras.layers.Dense(50, activation="relu", name="layer1"))
    model.add(keras.layers.Dense(100, activation="relu", name="layer2"))
    model.add(keras.layers.Dense(50, activation="relu", name="layer3"))
    model.add(keras.layers.Dense(32, name="output"))

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.MeanSquaredError(),
                  metrics=[tf.keras.metrics.MeanSquaredError()])

    #probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

    #predictions = probability_model.predict(test)

    #print(predictions[0])


