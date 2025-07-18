import cv2

mask_path = "../data/mask_1920_1080.png"
video_path = "../data/parking_1920_1080.mp4"

mask = cv2.imread(mask_path, 0)
cap = cv2.VideoCapture(video_path)

numlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)

while True:
    ret, frame = cap.read()
    if not ret: break

    frame = cv2.resize(frame, (mask.shape[1], mask.shape[0]))

    for i in range(1, numlabels):
        x, y, w, h, area = stats[i]

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, str(i), (x+10, y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()