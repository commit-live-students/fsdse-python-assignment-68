import numpy as np


def solution(array1, array2):
    list_a = array1
    list_b = array2
    map(list_a.extend, list_b)
    return list_a
