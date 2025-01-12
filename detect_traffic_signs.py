from send_data import send_udp_message
from ultralytics import YOLO
import cvzone
import math
import time
import cv2
ip_address='192.168.137.72'
port =4210

def detect_traffic_signs(cap, model_path, class_names):
    model = YOLO(model_path)
    prev_frame_time = 0
    new_frame_time = 0

    while True:
        new_frame_time = time.time()
        success, img = cap.read()
        if not success:
            break

        results = model(img, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Bounding Box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2 - x1, y2 - y1

                # Confidence
                conf = math.ceil((box.conf[0] * 100)) / 100

                # Class id
                cls = int(box.cls[0])


                if conf > 0.8:
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                    # Class name
                    class_name = class_names[cls] if cls < len(class_names) else "Unknown"
                    cvzone.putTextRect(img, f'{class_name} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
                    message=class_name
                    if message.startswith('Speed'):
                          l= message.split()
                          num=int(l[2])
                          num = int(70 + (num - 50) * (255 - 70) / (120 - 50))
                          message= 'SL '+str(num)
                    send_udp_message(message, ip_address, port)

        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time
        print(fps)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()