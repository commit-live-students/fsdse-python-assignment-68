import numpy as np


def solution(array1, array2):
    #return_array = []

    if array1 == None or array2 == None:
        return None

    array1 = np.array(array1)
    array2 = np.array(array2)

    return_array = np.append(array1,array2)
    return np.array(return_array)
