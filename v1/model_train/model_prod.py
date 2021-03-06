import tensorflow as tf
import numpy as np
import nibabel as nib
from scipy import ndimage

# Reference: https://towardsdatascience.com/how-to-predict-an-image-with-keras-ca97d9cd4817


def load_model(img_path):
    model = tf.keras.models.load_model('v1/model_train/saved_model')

    volume = nib.load(img_path)                                 # load nii image
    volume = volume.get_fdata()
    min_size = 0
    max_size = 2500
    volume[volume < min_size] = min_size
    volume[volume > max_size] = max_size
    volume = (volume - min_size) / (max_size - min_size)
    volume = volume.astype("float32")
    desired_depth = 64
    desired_width = 128
    desired_height = 128

    # Get current depth
    current_depth = volume.shape[-1]
    current_width = volume.shape[0]
    current_height = volume.shape[1]

    # Compute depth factor
    depth = current_depth / desired_depth
    width = current_width / desired_width
    height = current_height / desired_height
    depth_factor = 1 / depth
    width_factor = 1 / width
    height_factor = 1 / height

    # Rotate
    img = ndimage.rotate(volume, 90, reshape=False)

    # Resize across z-axis
    img = ndimage.zoom(img, (width_factor, height_factor, depth_factor), order=1)
    img_array = np.array([img])
    #img = image.load_img(img_path, target_size=(128, 128, 64))              # Load image
    #img_array = image.img_to_array(img)                                 # Batching single image
    #img_batch = np.expand_dims(img_array, axis=0)

    #img_preprocessed = preprocess_input(img_batch)                      # Preprocess
    prediction = model.predict(np.expand_dims(img_array[0], axis=0))[0]
    scores = [1 - prediction, prediction]
    #prediction = model.predict(img_preprocessed)                        # Predict and convert to 0 or 1
    #prediction = tf.nn.softmax(prediction, axis=1)
    #prediction = tf.math.reduce_max(prediction, axis=1)

    return bool(int(prediction.numpy()[1]))
