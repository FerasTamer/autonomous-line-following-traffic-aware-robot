from webcam_capture import webcam_capture
from detect_traffic_signs import detect_traffic_signs
from send_data import send_udp_message
import cv2
if name== "main":
    class_names = [
        'Green Light', 'Red Light', 'Speed Limit 10', 'Speed Limit 100', 'Speed Limit 110', 'Speed Limit 120',
        'Speed Limit 20', 'Speed Limit 30', 'Speed Limit 40', 'Speed Limit 50', 'Speed Limit 60', 'Speed Limit 70',
        'Speed Limit 80', 'Speed Limit 90', 'Stop'
    ]
    model_path = "trrafic sign detection/yolov8 traffic/yolov8s smaller data set last resutls/416traininglast/weights/best.pt"

    cap = webcam_capture()
    detect_traffic_signs(cap, model_path, class_names)