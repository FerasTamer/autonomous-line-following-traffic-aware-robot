import cv2

def webcam_capture():
    cap = cv2.VideoCapture(1)  # For Webcam
    cap.set(3, 1280)
    cap.set(4, 720)
    return cap