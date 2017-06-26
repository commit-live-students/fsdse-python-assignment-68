import numpy as np

def solution(array1, array2):
    array1 = np.array(array1)
    array2 = np.array(array2)

    array1 = np.append(array1,array2)
    return array1
