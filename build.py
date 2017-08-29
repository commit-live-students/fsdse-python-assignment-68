import numpy as np


def solution(array1, array2):
    array2 = np.array(array2)
    return np.append(array1, array2.flatten())
