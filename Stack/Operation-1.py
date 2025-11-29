# Importing Numpy
import numpy as np

# How to manipulate the existing data of array
# suppose
a = np.arange(0, 20, 2, dtype=int)
print(f"Value of const array: {a}")
print(f"Dimension: {a.ndim}")
print(f"Shape and size: {a.shape} & {a.size}")

# slicing
Sliced_array = a[3:8]
print(f"Sliced array: {Sliced_array}")
