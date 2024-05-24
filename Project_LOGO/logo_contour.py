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
hist, bin_edges = np.histogram(img_gray, bins=256, range=(0,256))
fig = plt.plot(hist)
plt.show()

threshold = 70

# Threshold
# ret, img_thres = cv2.threshold(img_gray, threshold, 255, cv2.THRESH_BINARY)
# cv2.imshow('thres', img_thres)

# Adaptive Threshold
img_thres_adapt = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,13,5)
# cv2.imshow('thres', img_thres_adapt)

img_canny = cv2.Canny(img,100,200)
cv2.imshow('canny_img', img_canny)

# Circle Transform
circles = cv2.HoughCircles(img_canny, cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=40)
circles = np.int16(np.around(circles))

print(circles)

for i in circles[0,:]:
    img = cv2.circle(img, (i[0],i[1]),i[2],(0,255,0),2)

cv2.imshow('draw_img', img)


cv2.waitKey(0)