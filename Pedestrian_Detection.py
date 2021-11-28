import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os
net = cv2.dnn.readNetFromDarknet(r"yolov3_custom_test.cfg",r"yolov3_custom_4000.weights")

classes = ['person']

# cap = cv2.VideoCapture(0)

while 1:
    img = cv2.imread(r'Testing Images\FudanPed00033.png')
    img = cv2.resize(img,(1280,720))
    height,width,_ = img.shape
    blob = cv2.dnn.blobFromImage(img, 1/255,(416,416),(0,0,0),swapRB = True,crop= False)

    boxes =[]
    confidences = []
    class_ids = []
    net.setInput(blob)

    output_layers_name = net.getUnconnectedOutLayersNames()

    layerOutputs = net.forward(output_layers_name)

    indexes = cv2.dnn.NMSBoxes(boxes,confidences,.5,.4)

    for output in layerOutputs:
        for detection in output:
            score = detection[5:]
            class_id = np.argmax(score)
            confidence = score[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3]* height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x,y,w,h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes,confidences,.8,.4)
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0,255,size =(len(boxes),3))
    if  len(indexes)>0:
        for i in indexes.flatten():
            x,y,w,h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i],2))
            color = colors[i]
            cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
            cv2.putText(img,label + " " + confidence, (x,y+400),font,3,color,2)

    cv2.imshow('img',img)
    if cv2.waitKey(1) == 27:
        break
cv2.imwrite('Result.jpg',img)
cap.release()
cv2.destroyAllWindows()