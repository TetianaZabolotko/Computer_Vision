import os
import cv2

import numpy as np

img = cv2.imread(os.path.join('.','shape.png'))

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray,130,255,cv2.THRESH_BINARY) 
adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 10)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('adaptive_thresh', adaptive_thresh)
cv2.imshow('thresh', thresh)

for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        # cv2.drawContours(img_gray, [cnt],0,(0,0, 255), 3)
        x1, y1, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img_gray, (x1,y1), (x1+w,y1+h), (0,255,0),2)
  
      
num = len(contours)
print(num) 

contr_max_area = []
contr_max_arr = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 200:
        contr_max_area.append(area)
        contr_max_arr.append(cnt)


print(len(contr_max_area))
print(sorted(contr_max_area))
print(max(contr_max_area))

max_indx = contr_max_area.index(max(contr_max_area))
print(max_indx)

cnt = contr_max_arr[max_indx]
cv2.drawContours(img,[cnt],0,(0,255,0), 3)    

cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)


cv2.boundingRect(cnt)


cv2.waitKey(0)
cv2.destroyAllWindows()