from PIL import Image
import numpy as np

def pca(X):
    """ Метод гловних компонент
    вхід: матриця Х, в якій дані для навчання 
    зберігаються у вигляді лінеаризованих масивів, 
    по одному в кожному рядку

    вихід: матриця проекції, дисперсія та середнє  
    """

    # get shape
    num_data, dim = X.shape

    #center data
    mean_X = X.mean(axis=0)
    X = X - mean_X

    if dim > num_data:    
        M = np.dot(X,X.T) # cov matrix E[(X - E(X))(X - E(X)).T]
        e, EV = np.linalg.eigh(M) # eigen values, eigen vectors
        tmp = np.dot(X.T,EV).T 
        V = tmp[::-1] # change order, we need last eigen vectors
        S = np.sqrt(e)[::-1] # change order eigen values represent in increased order

        for i in range(V.shape[1]): # possible use arrange() and xrange()
            V[:,i]/= S

    else:
        # SVD
        U,S,V = np.linalg.svd(X)
        V = V[:num_data] # it has sense return only first num_data rows

    # return matrix projection, dispersion and mean
    return V,S,mean_X








# X = np.array([[2, 3, 4],
#      [6,5,8],
#      [7,2,0]])

# print(X.dtype)  
# print(X.shape)  
# print('REORDER: ', X[::-1])
# e, EV = np.linalg.eigh(X)
# print(e)
# print()
# print('VECTORS: ', EV)
