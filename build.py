import numpy as np


def solution(array1, array2):
    """
    Enter your code here
    """
    for i in array2:
        for j in i:
            array1.append(j)
    return array1
