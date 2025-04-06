import cv2
import os
from utils import get_parking_spots_bboxes, empty_or_not
import numpy as np

def calc_img(img1, img2):
    return np.abs(np.mean(img1) - np.mean(img2))

base_path = os.path.dirname(__file__)
mask_path = os.path.join(base_path, "data", "mask_1920_1080.png")
video_path = os.path.join(base_path, "data", "parking_1920_1080_loop.mp4")

mask = cv2.imread(mask_path, 0)
cap = cv2.VideoCapture(video_path)

connected_components = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32F)

spots = get_parking_spots_bboxes(connected_components)

step = 30
frame_nmr = 0
spots_status = [None for j in spots]
previous_frame = None
diffs = [None for j in spots]

while True:
    ret, frame = cap.read()
    if not ret: break

    if frame_nmr % step == 0 and previous_frame is not None:
        for spot_idx, spot in enumerate(spots):
            x1,y1,w,h = spot
            spot_drop = frame[y1:y1+h,x1:x1+w]
            diffs[spot_idx] = calc_img(spot_drop, previous_frame[y1:y1+h,x1:x1+w])

        print(diffs)

    if frame_nmr % step == 0:
        if previous_frame is None:
            arr_ = range(len(spots))
        else:
            arr_ = [j for j in np.argsort(diffs) if diffs[j] / np.amax(diffs) > 0.4 ]
        for spot_idx in arr_:
            x1,y1,w,h = spots[spot_idx]
            spot_drop = frame[y1:y1+h,x1:x1+w]
            spot_status = empty_or_not(spot_drop)
            spots_status[spot_idx] = spot_status

    if frame_nmr % step == 0:
        previous_frame = frame.copy()

    for spot_idx, spot in enumerate(spots):
        spot_status = spots_status[spot_idx]
        x1, y1, w, h = spots[spot_idx]

        if spot_status:
            frame = cv2.rectangle(frame,(x1,y1),(x1+w,y1+h),(0, 0, 255), 2)
        else:
            frame = cv2.rectangle(frame,(x1,y1),(x1+w,y1+h),(0, 255, 0), 2)

    cv2.rectangle(frame, (80,20), (550, 80), (0, 0, 0), -1)
    cv2.putText(frame, 'Available spots: {} / {}'.format(str(sum(spots_status)),
                str(len(spots_status))), (100, 60), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 255, 255), 2)

    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

    frame_nmr += 1

cap.release()
cv2.destroyAllWindows()
