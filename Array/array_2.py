# Adding, Removing, and sorting elements

# Importing Numpy
import numpy as np

arr = np.random.rand(10)
arr = np.sort(arr)
print(arr)


# Concatination
arr_1 = np.array([1, 2, 3, 4])
arr_2 = np.array([2, 4, 6, 8])
arr = np.concatenate((arr_1, arr_2))
print(arr)
print(np.sort(arr))
