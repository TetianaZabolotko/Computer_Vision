import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

box = np.array([10,20, 30, 40])
print(box)

img = cv2.imread(os.path.join('.','logo.jpg'))
# cv2.imshow('origin_img', img)

# IMAGE PROCESSING

# Filter to reduce noise
# img = cv2.GaussianBlur(img,(5,5),0)
# cv2.imshow('gauss_img', img)

# Mean Shift Algorithm

# Explore Threshold
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# hist, bin_edges = np.histogram(img_gray, bins=256, range=(0,256))
# fig = plt.plot(hist)
# plt.show()

# threshold = 70

# Threshold
# ret, img_thres = cv2.threshold(img_gray, threshold, 255, cv2.THRESH_BINARY)
# cv2.imshow('thres', img_thres)

# Adaptive Threshold
img_thres_adapt = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,13,5)
# cv2.imshow('thres', img_thres_adapt)

img_canny = cv2.Canny(img,100,200)
cv2.imshow('canny_img', img_canny)

# Circle Transform
# circles = cv2.HoughCircles(img_canny, cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=30, maxRadius=100)
# circles = cv2.HoughCircles(img_canny, cv2.HOUGH_GRADIENT,1,20,param1=150,param2=30,minRadius=30, maxRadius=100)
# circles = np.int16(np.around(circles))

# print(len(circles))
# print(circles.shape)
# print(circles[0,:])
# i=circles[0,1]
# img = cv2.circle(img, (i[0],i[1]),i[2],(0,255,0),2)


# for i in circles[0,:]:
#     img = cv2.circle(img, (i[0],i[1]),i[2],(0,255,0),2)

# cv2.imshow('draw_img', img)


# Find Contours
contours, hierarchy = cv2.findContours(img_canny,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# cv2.drawContours(img,contours,-1,(0,255,0), 1)

max_cnt_list = []
max_area = 0
max_i=0
max_cnt = 0 
# for cnt, i in enumerate(contours):
for cnt in contours:    
    area = cv2.contourArea(cnt)
    if area>max_area:
        max_area = area
        max_cnt = cnt
        max_cnt_list.append(max_cnt)
        print(area)
        print(cnt)
        # max_i=i

# max_cnt = contours[max_i]

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

cv2.drawContours(img,contours,-1,(0,0,255), 1)
cv2.drawContours(img,[max_cnt],0,(0,255,0), 3)
 
print(max_cnt)
print('Number of Contours found =' + str(len(contours)))

# for c in cnt:
    # cv2.drawContours(img,[c],-1,(0,0,255),1)
    # cv2.drawContours(img,[c],0,(0,255,0), 3)  

cv2.imshow('drimg', img)
cv2.waitKey(0)
cv2.destroyAllWindows