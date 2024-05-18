from PIL import Image
import numpy as np
from pylab import *
import PCA

imlist = [1,2,3,3,4,]
im = array(Image.open(imlist[0]))

m,n = im.shape[0:2]
imnbr = len(imlist)

# create matrix to create all linear images
immatrix = array([array(Image.open(im)).flatten() for im in imlist], 'f')(

# pca
V,S,immean = PCA.pca(immatrix)

# show few images
figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range(7):
    subplot(2,4,i+2)
    imshow(V[i].reshape(m,n))

show()


# X = np.array([[1,2,3,4,5],
#              [1,2,3,4,5],
#              [1,2,3,4,5],
#              [1,2,3,4,5]])
# print(X.shape[0:2])