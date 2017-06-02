import numpy as np

def solution(array1, array2):
    array1 = np.array(array1)
    array2 = np.array(array2)
    a, b = array2.shape
    array2 = np.reshape(array2, (a*b))
    return np.hstack((array1,array2))
