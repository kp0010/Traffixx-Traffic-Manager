from ultralytics import YOLO
import cv2
import cvzone
import math

cap = cv2.VideoCapture('Assets/Videos/road.mp4')

model = YOLO('yolov8n.pt')

classNames = ["car", "motorbike", "bus", "truck"]

while True:
    success, img = cap.read()
    results = model("Assets/Videos/road.mp4", show=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img, (x1, y1), (x2,y2),(255,0,255),3)
            w, h =x2-x1, y2-y1

            # Confidance
            conf = math.ceil((box.conf[0] * 100)) / 100
            # Class Name
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if currentClass == "car" or currentClass == "truck" or currentClass == "bus" or currentClass == "motorbike" and conf > 0.3:
                cvzone.putTextRect(img, f'{currentClass} {conf}', (max(0, x1), max(35,y1)), scale=0.6, thickness=1, offset=3)
                cvzone.cornerRect(img, (x1, y1, w, h), l=9)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
    