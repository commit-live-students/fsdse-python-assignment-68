import numpy as np
def solution(array1, array2):
    for i in array2:
        array1.extend(i)
    return array1
