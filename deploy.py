import os
import pathlib
import io
import os
import scipy.misc
import numpy as np
import six
import time
import cv2 as cv

from six import BytesIO
from object_detection.utils import visualization_utils as viz_utils
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

import tensorflow as tf
from object_detection.utils import visualization_utils as viz_utils

# %matplotlib inline
     
def load_image_into_numpy_array(path):
    """Load an image from file into a numpy array.

    Puts image into numpy array to feed into tensorflow graph.
    Note that by convention we put it into a numpy array with shape
    (height, width, channels), where channels=3 for RGB.

    Args:
    path: a file path (this can be local or on colossus)

    Returns:
    uint8 numpy array with shape (img_height, img_width, 3)
    """
    img_data = tf.io.gfile.GFile(path, 'rb').read()
    image = Image.open(BytesIO(img_data))
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)
__category_index = {
    1: {'id': 1, 'name': 'Cone'},
    2: {'id': 2, 'name': 'Cube'},
    3: {'id': 3, 'name': 'tipped_Cone'},
}

start_time = time.time()
tf.keras.backend.clear_session()
detect_fn = tf.saved_model.load('content/new_testing_model/saved_model/')
end_time = time.time()
elapsed_time = end_time - start_time
print('Elapsed time: ' + str(elapsed_time) + 's')
     

cap = cv.VideoCapture(0)

while True:
    success, image = cap.read()
    if not success:
        continue
    input_tensor = tf.convert_to_tensor(image, dtype=tf.uint8)
    input_tensor = input_tensor[tf.newaxis, ...]
    detections = detect_fn(input_tensor)
    plt.rcParams['figure.figsize'] = [42, 21]
    image_np_with_detections = image.copy()
    viz_utils.visualize_boxes_and_labels_on_image_array(
        image_np_with_detections,
        detections['detection_boxes'][0].numpy(),
        detections['detection_classes'][0].numpy().astype(np.uint8),
        detections['detection_scores'][0].numpy(),
        __category_index,
        use_normalized_coordinates=True,
        max_boxes_to_draw=200,
        min_score_thresh=.40,
        agnostic_mode=False)
    cv.imshow('object detection', cv.resize(image_np_with_detections, (800, 600)))
    print("detected")
    if cv.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()