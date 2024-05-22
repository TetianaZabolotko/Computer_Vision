import os

from PIL import Image
import numpy as np
import cv2
# import scikit-image

from scipy.ndimage import filters

#filters with cv2
im_cv  = cv2.imread(os.path.join('.', 'logo.jpg'))
print(im_cv)
blur = cv2.GaussianBlur(im_cv,(5,5),0) # standart deviation
cv2.imshow('blur_im', blur)

# with scipy
im = np.array(Image.open('./logo.jpg')).convert('L')
im2 = filters.gaussian_filter(im,5)


im_new = np.zeros(im.shape)
for i in range(3):
    im_new[:,:,i] = filters.gaussian_filter(im[:,:,i],5)


