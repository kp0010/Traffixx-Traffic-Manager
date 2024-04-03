import time

import cvzone
from ultralytics import YOLO
import cv2
import math


start = time.time()
print(start)

cap = cv2.VideoCapture('Assets/Videos/rush.mp4')

model = YOLO('yolov8n.pt')

print(f"Time after Model {time.time() - start}")

classNames = {2: "car", 3: "motorcycle", 5: "bus", 7: "truck"}

for i in range(60):
    cap.read()

print(f"Time after Iter {time.time() - start}")

suc, img = cap.read()

print(f"Time after Read {time.time() - start}")

result = model.predict(img)

print(f"Time after Predict {time.time() - start}")

for box in result[0].boxes:
    conf = math.ceil((box.conf[0] * 100)) / 100
    cls = int(box.cls[0])
    if conf < .5 or cls not in classNames.keys():
        continue

    x1, y1, x2, y2 = box.xyxy[0].tolist()
    x1, y1, x2, y2 = [int(i) for i in [x1, y1, x2, y2]]
    w, h = x2 - x1, y2 - y1

    if cls in classNames.keys():
        currentClass = classNames[cls]
        cvzone.putTextRect(img, f"{currentClass} {conf}", (max(0, x1), max(35, y1)), scale=1, thickness=1, offset=10)
        cvzone.cornerRect(img, (x1, y1, w, h), l=2)


cv2.imshow("1", img)

print(f"Time to Show {time.time() - start}")

cv2.waitKey(0)

