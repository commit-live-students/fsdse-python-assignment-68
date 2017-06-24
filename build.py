import numpy as np


def solution(array1, array2):
     for e in array2:
         for e2 in e:
             array1.append(e2)
     return array1


solution([1,2,3],[[4,5,6],[7,8,9]])
