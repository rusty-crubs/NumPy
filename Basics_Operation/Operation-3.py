# Broadcasting
import numpy as np

data = np.array([1.0,2.0], dtype=np.float32)
print(f"Data in Miles: {data}")
print(f"Data in Kilometers: {data * 1.6}")

a = np.array([13,12,15])
b = np.array([
    [10],
    [12],
    [16]
             ])
print(f"Data a: {a}")
print(f"Data b: {b}")
print(f"Multiplication a * b: {a * b}")

# Most useful array operations
data = np.array([2,4,6,8,10,12,16],dtype=np.float32)
print(f"Max value: {data.max()}")
print(f"Min value: {data.min()}")
print(f"Sum of all values: {data.sum()}")

# Matrix operations
matrix_a = np.array([
    [2,1,6],
    [1,3,5],
    [3,4,9]
])
print(f"Matrix A:\n{matrix_a}")
print(f"Shape of Matrix A: {matrix_a.shape}")
print(f"Transpose of Matrix A:\n{matrix_a.T}")
print(f"Max value in Matrix A: {matrix_a.max(axis=0)}")
print(f"Min value in Matrix A: {matrix_a.min(axis=0)}")
print(f"Sum of all values in Matrix A: {matrix_a.sum(axis=0)}")