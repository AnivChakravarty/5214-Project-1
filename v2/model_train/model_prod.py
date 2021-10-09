import os

import tensorflow as tf
import numpy as np

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input

# Reference: https://towardsdatascience.com/how-to-predict-an-image-with-keras-ca97d9cd4817


def load_model(img_path):
    cwd_current = os.getcwd()
    os.chdir("./v2/model_train")                                        # for loading from UI

    model = tf.keras.models.load_model('saved_model/my_model')          # Load model

    img = image.load_img(img_path, target_size=(160, 160))              # Load image
    img_array = image.img_to_array(img)                                 # Batching single image
    img_batch = np.expand_dims(img_array, axis=0)

    img_preprocessed = preprocess_input(img_batch)                      # Preprocess

    prediction = model.predict(img_preprocessed)                        # Predict
    prediction = tf.nn.softmax(prediction, axis=1)
    prediction = tf.math.reduce_max(prediction, axis=1)

    os.chdir(cwd_current)                                               # Go back to original working directory

    return bool(int(prediction.numpy()[0]))                             # Return 0 or 1
