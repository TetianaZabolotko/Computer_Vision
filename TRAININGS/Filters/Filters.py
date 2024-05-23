import os

from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
# import scikit-image

from scipy.ndimage import filters

#filters with cv2
im_cv  = cv2.imread(os.path.join('.', 'logo.jpg'))
im_cv = cv2.cvtColor(im_cv, cv2.COLOR_RGB2GRAY)
# print(im_cv)
# blur = cv2.GaussianBlur(im_cv,(5,5),0) # standart deviation
# cv2.imshow('blur_im', blur)
# cv2.waitKey(0)

# with scipy
# im = np.array(Image.open('./logo.jpg')).convert('L')
# im2 = filters.gaussian_filter(im,5)

# im_new = np.zeros(im_cv.shape)
# for i in range(3):
#     # im_new[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
#     cv2.imshow('im', blur[:,:,i])
#     cv2.waitKey(0)
print('5*4', '270', im_cv.shape)
new_width = 270*2
new_height = 270*3
new_dim = (new_width, new_height)
im_cv = cv2.resize(im_cv, new_dim)
cv2.imshow('Origina', im_cv)

ret, thresh = cv2.threshold(im_cv, 150, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('Contours', thresh)

# DERIVATIVES
# X

sobel_X = cv2.Sobel(im_cv,cv2.CV_64F,1,0)
sobel_X_abs = np.int8(np.absolute(sobel_X))
cv2.imshow('X', sobel_X)
cv2.imshow('X_abs', sobel_X_abs)

sobel_Y = cv2.Sobel(im_cv,cv2.CV_64F,0,1)
sobel_Y_abs = np.int8(np.absolute(sobel_Y))
# cv2.imshow('Y', sobel_Y)

sobel_XY_combined = cv2.bitwise_or(sobel_Y_abs, sobel_X_abs)
# cv2.imshow('XY', sobel_XY_combined)

magnitude = np.sqrt(sobel_X**2 + sobel_Y**2)
# cv2.imshow('Magnitude', magnitude)

cv2.waitKey(0)

titles = ['Original image', 'Sobel X', 'Sobel Y', 'Sobel XY combined using OR']
images = [im_cv, sobel_X_abs, sobel_Y_abs, sobel_XY_combined]

# plt.figure(figsize=(13,5))
# for i in range (4):
#     plt.subplot(2,2,i+1)
#     plt.imshow(images[i])
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])

# plt.tight_layout()
# plt.show()    
    