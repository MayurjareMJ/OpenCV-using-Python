import cv2
import torch
import numpy as np
path="C:/Users/91935/Downloads/yolov5win11customobj-main/yolov5win11customobj-main/best.pt"
model = torch.hub.load('ultralytics/yolov5', 'custom',path , force_reload=True)
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(1020,500))
    results=model(frame)
    frame=np.squeeze(results.render())
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.realese()
cv2.destroyAllWindows()
