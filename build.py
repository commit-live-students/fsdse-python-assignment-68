import numpy as np


def solution(array1, array2):
    """
    Enter your code here
    """
    array1 = np.array(array1)
    array2 = np.array(array2)

    array1 = np.append(array1,array2)
    return array1

solution([10, 20, 30],[[40, 50, 60], [70, 80, 90]])
