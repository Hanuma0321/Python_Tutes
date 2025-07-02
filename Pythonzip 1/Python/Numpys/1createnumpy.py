'''
numpy are as lists only
but 50x faster than  lists
it has so many functions to work with matrices and fouroer transformations

1D - []
2D - [[],[]]
3D -[[[]]]
'''

import numpy as np

print(np.__version__)
arr = np.array([3,5,7,4])
print(arr,arr.ndim)

arr1 = np.array([[3,5,4],[4,6,8]])
print(arr1,arr1.ndim)

arr2 = np.array([[[3,5,4],[4,6,8]]])
print(arr2,arr2.ndim)