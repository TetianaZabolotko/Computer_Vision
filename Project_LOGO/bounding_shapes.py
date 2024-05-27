import os
import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread(os.path.join('.','logo.jpg'))
img_canny = cv2.Canny(img,100,200)
contours, hierarchy = cv2.findContours(img_canny,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

max_cnt_list = []
max_area = 0
max_cnt = 0 
for cnt in contours:    
    area = cv2.contourArea(cnt)
    if area>max_area:
        max_area = area
        max_cnt = cnt
        max_cnt_list.append(max_cnt)

# StraightBoundingRECT
for cnt in max_cnt_list:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)

# Rotated Rect
for cnt in max_cnt_list:
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img,[box],0,(255,0,0),2)
        