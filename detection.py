import math

from ultralytics import YOLO
import cv2


class Detection:
    def __init__(self, video="road.mp4"):
        self.video = cv2.VideoCapture("Assets/Videos/" + video)
        self.model = YOLO("yolov8n.pt")

        self.classnames = {2: "car", 3: "motorcycle", 5: "bus", 7: "truck"}

    def set_vid(self, video):
        self.video = cv2.VideoCapture("Assets/Videos/" + video)

    def get_frame(self, sec):
        fps_vid = self.video.get(cv2.CAP_PROP_FPS)
        frame_id = int(fps_vid * sec)

        self.video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)

        success, sel_frame = self.video.read()

        return sel_frame if success else []

    def predict_for_frame(self, sel_frame):
        return self.model.predict(source=sel_frame, verbose=False)

    def get_count(self, sec, show=False):
        sel_frame = self.get_frame(sec)

        count = {cls: 0 for cls in self.classnames.values()}

        if len(sel_frame) > 0:
            prediction = self.predict_for_frame(sel_frame)[0]

            for box in prediction.boxes:
                conf = math.ceil(box.conf[0] * 100) / 100
                clsname = self.classnames.get(int(box.cls[0]), None)

                if clsname is None or conf < .5:
                    continue

                count[clsname] += 1

                if show:
                    cv2.imshow(str(sel_frame[0]), sel_frame)
                    cv2.waitKey(1)

                x1, y1, x2, y2 = [int(i) for i in box.xyxy[0].tolist()]

            print(count)
            return count


if __name__ == "__main__":
    detector = Detection("road.mp4")
    detector.get_count(3.5, show=True)
    detector.set_vid("surveillance.m4v")
    detector.get_count(45.1, show=True)

    cv2.waitKey(0)
