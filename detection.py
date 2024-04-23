import math

from ultralytics import YOLO
import cv2

VIDEO_PATH = "Assets/Videos/"


class Detector:
    def __init__(self, video="road.mp4", verbose=False):
        self.video = cv2.VideoCapture(VIDEO_PATH + video)
        self.model = YOLO("yolov8n.pt")
        self.verbose = verbose

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
        return self.model.predict(source=sel_frame, verbose=self.verbose)

    def get_count(self, sec, show=False):
        count = {cls: 0 for cls in self.classnames.values()}

        sel_frame = self.get_frame(sec)

        sel_frame = cv2.resize(sel_frame, (1200, 600))

        if len(sel_frame) > 0:
            prediction = self.predict_for_frame(sel_frame)[0]

            for box in prediction.boxes:
                conf = math.ceil(box.conf[0] * 100) / 100
                clsname = self.classnames.get(int(box.cls[0]), None)

                if clsname is None or conf < .3:
                    continue

                count[clsname] += 1

                if show:
                    x1, y1, x2, y2 = [int(x) for x in box.xyxy[0].tolist()]

                    cv2.rectangle(sel_frame, (x1, y1), (x2, y2), (0, 255, 0))
                    cv2.imshow(str(sel_frame[0]), sel_frame)
                    cv2.waitKey(1)

        return count


if __name__ == "__main__":
    import TLmanager

    tlmanager = TLmanager.TLmanager()

    detector = Detector("Road_vid3.mp4")
    for i in range(0, 20):
        cnt2 = detector.get_count(i, show=0)

    detector.set_vid("Road_vid.mp4")
    for i in range(20, 30):
        cnt = detector.get_count(i, show=1)

    cv2.waitKey(0)
