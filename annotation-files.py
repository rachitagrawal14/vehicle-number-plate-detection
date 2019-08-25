import json
import csv
import os
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import cv2
pth="C:\\Users\\HP\\Desktop\\data_veh\\Indian_Number_plates.json"
f=open(pth)
def convert_labels(w1,h1, x1, y1, x2, y2):
    """
    Definition: Parses label files to extract label and bounding box
        coordinates.  Converts (x1, y1, x1, y2) KITTI format to
        (x, y, width, height) normalized YOLO format.
    """
    def sorting(l1, l2):
        if l1 > l2:
            lmax, lmin = l1, l2
            return lmax, lmin
        else:
            lmax, lmin = l2, l1
            return lmax, lmin
    
    xmax, xmin = sorting(x1, x2)
    ymax, ymin = sorting(y1, y2)
    dw = 1./w1
    dh = 1./h1
    x = (xmin + xmax)/2.0
    y = (ymin + ymax)/2.0
    w = xmax - xmin
    h = ymax - ymin
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
  
  #------------------------------------------------------------------
  # image_path x_min, y_min, x_max, y_max, class_id  x_min, y_min ,..., class_id 
cl=0
des="C:\\Users\\HP\\Desktop\\data_veh\\VOC-data\\"
for line in f:
    j=json.loads(line)
    size=[]
    url = j["content"] 
    if ".gif" in url:
        print(url.split('/')[-1])
        continue
    else:
        h1=j["annotation"][0]['imageHeight']
        w1=j["annotation"][0]['imageWidth']
        x1= j["annotation"][0]["points"][0]['x']*w1
        y1= j["annotation"][0]["points"][0]['y']*h1
        x2= j["annotation"][0]["points"][1]['x']*w1
        y2= j["annotation"][0]["points"][1]['y']*h1
        img_pth="C:\\Users\\HP\\Desktop\\data_veh\\images\\"+url.split('/')[-1]
        yolo =str(img_pth)+" "+str(x1)+","+str(y1)+","+str(x2)+","+str(y2)+"\n"
        with open(des+"dataset.txt","a") as file:
            file.write(yolo)
