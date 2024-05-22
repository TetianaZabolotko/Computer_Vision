import os

import cv2
import numpy as np

img = cv2.imread(os.path.join('.','logo.jpg'))
print(img)

cv2.imshow('img', img)
cv2.waitKey(0)
