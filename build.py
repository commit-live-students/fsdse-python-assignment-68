import numpy as np

def solution(array1, array2):
    a = np.append(array1,array2)
    return a

# solution([10, 20, 30], [[40, 50, 60], [70, 80, 90]])
# Output : array([10, 20, 30, 40, 50, 60, 70, 80, 90])
