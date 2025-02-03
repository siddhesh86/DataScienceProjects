
'''
numpy.sum, concatenate, stack
'''

import numpy as np

np_array_2d = np.arange(0, 6).reshape([2,3])

print("np_array_2d:\n",np_array_2d)

print("np.sum(np_array_2d, axis = 0):",np.sum(np_array_2d, axis = 0))
print("np.sum(np_array_2d, axis = 1):",np.sum(np_array_2d, axis = 1))


# concatenate 2-d arrays
np_array_1s = np.array([[1,1,1],[1,1,1]])
np_array_9s = np.array([[9,9,9],[9,9,9]])

print("\nnp_array_1s:\n",np_array_1s)
print("np_array_9s:\n",np_array_9s)
print("\nnp.concatenate([np_array_1s, np_array_9s], axis = 0):\n",np.concatenate([np_array_1s, np_array_9s], axis = 0))
print("\nnp.concatenate([np_array_1s, np_array_9s], axis = 1):\n",np.concatenate([np_array_1s, np_array_9s], axis = 1))


# concatenate 1-d arrays
np_array_1s_1dim = np.array([1,1,1])
np_array_9s_1dim = np.array([9,9,9])
print("\nnp_array_1s_1dim:\n",np_array_1s_1dim)
print("np_array_9s_1dim:\n",np_array_9s_1dim)
print("\nnp.concatenate([np_array_1s_1dim, np_array_9s_1dim], axis = 0):\n",np.concatenate([np_array_1s_1dim, np_array_9s_1dim], axis = 0))
### ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# stack 1-D array
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

print("\n\narr1:\n",arr1)
print("arr2:\n",arr2)

print("\nnp.stack((arr1, arr2), axis=0):\n",np.stack((arr1, arr2), axis=0))
print("np.stack((arr1, arr2), axis=1):\n",np.stack((arr1, arr2), axis=1))

print("\nnp.hstack((arr1, arr2)):\n",np.hstack((arr1, arr2)))

print("\nnp.vstack((arr1, arr2)):\n",np.vstack((arr1, arr2)))

print("\nnp.dstack((arr1, arr2)):\n",np.dstack((arr1, arr2)))
