
import cv2
import json
import time
import numpy as np
from ultralytics import YOLO

def process_video(video_path):
    model = YOLO('yolov8n.pt')
    cap = cv2.VideoCapture(video_path)
    back_sub = cv2.createBackgroundSubtractorMOG2()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        
        results = model(frame, verbose=False)
        # هنا يوضع منطق الـ JSON والـ Motion الذي صممناه سابقاً
        # ... (تم اختصاره هنا ليكون جاهزاً للرفع)
        
    cap.release()

if __name__ == "__main__":
    print("AI Microservice Started...")
