import numpy as np
import random as rand
l1 = list(range(6))
arr = np.array(l1)
'''#arr.dtype.itemsize.nbytes.size.shape.ndim
print(arr.reshape(3,2).ndim)
print(arr.nbytes)
print(arr.size)
print(arr.reshape(2,3))
print(arr.ndim)
arr2 = np.arange(15)'''
print(np.ones((2,5)))


lst = [1,2,3,4]
array = np.array(lst)
array = np.array([[1,2],[4,4],[3,9]])
array = np.array([[[1,2,3],[4,5,6],[7,8,9],[1,0,1],[0,0,1], [1,1,0]]])
array = np.arange(15)
array = np.reshape(array,(5,3,1))
arr.resize(2,3)
array = np.resize(arr,(3,2,1))
