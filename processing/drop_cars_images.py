import cv2
import os

output_dir = "../data/data_train_test/empty"
os.makedirs(output_dir, exist_ok=True)

mask_path = "../data/mask_1920_1080.png"
video_path = "../data/parking_1920_1080.mp4"

mask = cv2.imread(mask_path,0)
cap = cv2.VideoCapture(video_path)

numlabels, _, stats, _ = cv2.connectedComponentsWithStats(mask, cv2.CV_32S)

slots = []

for i in range(1, numlabels):
    x1 = int(stats[i, cv2.CC_STAT_LEFT])
    y1 = int(stats[i, cv2.CC_STAT_TOP])
    w = int(stats[i, cv2.CC_STAT_WIDTH])
    h = int(stats[i, cv2.CC_STAT_HEIGHT])
    slots.append([x1, y1, w, h])

frame_nmr = 0

while True:
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_nmr)
    ret, frame = cap.read()
    if not ret: break

    frame = cv2.resize(frame, (mask.shape[1], mask.shape[0]))

    selected_slots = [133, 148, 165, 181, 345, 361, 378, 386, 342, 361, 180, 132, 107,
                        92, 62, 5, 90, 130, 162, 186, 202, 225, 272, 304, 320, 336, 352,
                        390, 30, 13, 33, 73, 282, 281, 158, 224, 27] #empty

    # selected_slots = [19, 32, 47, 77, 121, 120, 149, 164, 189, 188, 233, 230, 279, 259,
    #                     278, 254, 296, 313, 327, 328, 371, 379, 385, 393, 392, 6, 17, 14,
    #                     106, 146, 179, 147, 128, 161, 176, 185, 201, 200, 177, 160, 145,
    #                     129, 18, 15, 29, 42, 57, 56, 86, 116, 117, 126, 143, 220, 222,
    #                     68, 357, 359, 66, 244, 271, 4, 8] #not empty

    for slot_num, slot in enumerate(slots, start=1):
        if slot_num in selected_slots:
            x, y, w, h = slot
            slot_img = frame[y:y+h, x:x+w]

            if slot_img.shape[0] > 0 and slot_img.shape[1] > 0:
                file_name = f"{str(frame_nmr).zfill(4)}_{str(slot_num).zfill(4)}.jpg"
                cv2.imwrite(os.path.join(output_dir, file_name), slot_img)

    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break
    frame_nmr += 10

cap.release()

cv2.destroyAllWindows()



