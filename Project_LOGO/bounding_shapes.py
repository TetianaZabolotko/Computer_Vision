import os
import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread(os.path.join('.','logo.jpg'))
img_canny = cv2.Canny(img,100,200)
contours, hierarchy = cv2.findContours(img_canny,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,0,255), 1)

max_cnt_list = []
max_area = 0
max_cnt = 0 
for cnt in contours:    
    area = cv2.contourArea(cnt)
    if area>max_area:
        max_area = area
        max_cnt = cnt
        max_cnt_list.append(max_cnt)

#Contour Perimeter
perimeter = cv2.arcLength(max_cnt, True)
print(perimeter)
print(max_area)

# StraightBoundingRECT
# for cnt in max_cnt_list:
#     x,y,w,h = cv2.boundingRect(cnt)
#     cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)

# Rotated Rect
# for cnt in max_cnt_list:
#     rect = cv2.minAreaRect(cnt)
#     box = cv2.boxPoints(rect)
#     box = np.int0(box)
#     cv2.drawContours(img,[box],0,(255,0,0),2)

# How to get coordinate of point
for i,point in enumerate(max_cnt):
    # print(f'point {i} - {point}')
    x, y = point[0]
    # print(f'x - {x}, y - {y}')


# # contour approximation
# for cnt in max_cnt_list:
#     epsilon = 0.15*cv2.arcLength(cnt, True)
#     approx = cv2.approxPolyDP(cnt, epsilon, True)
#     cv2.drawContours(img,[approx],0,(255,0,0),2)

# minimum eclosing Circle
# for cnt in max_cnt_list:
#     (x,y), radius = cv2.minEnclosingCircle(cnt)
#     center = (int(x), int(y))
#     radius = int(radius)
#     cv2.circle(img, center,radius,(0,255,0),2)

# fitting an ellipse
# for cnt in max_cnt_list:
#     ellipse = cv2.fitEllipse(cnt)
#     cv2.ellipse(img,ellipse,(0,255,0),2)

# difference boxPoints and boundingRect
# rect = cv2.minAreaRect(cnt)
# box = cv2.boxPoints(rect)
# print(cv2.boundingRect(box))
# print(box)

# fitting a line
# for cnt in max_cnt_list:
#     rows, cols = img.shape[:2]
#     [vx,vy,x,y] = cv2.fitLine(cnt,cv2.DIST_L2,0,0.01,0.01)
#     lefty = int((-x*vy/vx)+y)
#     righty = int((cols-x*vy/vx)+y)
#     cv2.line(img,(cols-1,righty), (0,lefty),(0,255,0),2)    

    
# cv2.imshow('img', img)    
cv2.waitKey(0)
cv2.destroyAllWindows
        