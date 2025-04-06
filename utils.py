import cv2
import pickle
import numpy as np
from skimage.transform import resize

EMPTY = True
NOT_EMPTY = False

MODEL = pickle.load(open('model.pkl', 'rb'))

def empty_or_not(spot_bgr):
    flat_data = []
    img_reszied = resize(spot_bgr, (15, 15, 3))
    flat_data.append(img_reszied.flatten())
    flat_data = np.array(flat_data)

    y_output = MODEL.predict(flat_data)

    if y_output == 0:
        return NOT_EMPTY
    else:
        return EMPTY

def get_parking_spots_bboxes(connected_components):
    numlabels, labels, stats, centroids = connected_components
    slots = []
    coef = 1

    for i in range(1, numlabels):
        x1 = int(stats[i, cv2.CC_STAT_LEFT] * coef)
        y1 = int(stats[i, cv2.CC_STAT_TOP] * coef)
        w = int(stats[i, cv2.CC_STAT_WIDTH] * coef)
        h = int(stats[i, cv2.CC_STAT_HEIGHT] * coef)

        slots.append([x1, y1, w, h])

    return slots