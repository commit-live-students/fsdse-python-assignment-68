import numpy as np


def solution(array1, array2):
    """
    Enter your code here
    """
    listArr = np.array(array1)
    listArr = np.append(array1,array2)
    return listArr
arr1 = np.array([10, 20, 30])
arr2 = np.array([[40, 50, 60], [70, 80, 90]])
print solution(arr1, arr2)
