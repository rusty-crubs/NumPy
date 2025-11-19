# Convert a 1D array into a 2D array

# Import NumPy
import numpy as np

# Creating a 1D array
One_Dimensional_Array = np.array([0, 1, 2, 3, 4, 5])

print(f"One Dimensional Array shape: {One_Dimensional_Array.shape}")
print(f"Dimension: {One_Dimensional_Array.ndim}")
print(f"Shape: {One_Dimensional_Array.shape}")

# Adding a new axis
Two_Dimensional_Array = One_Dimensional_Array[np.newaxis, :]
print(f"Two_Dimensional_Array: {Two_Dimensional_Array}")
print(f"Two_Dimensional_Array shape: {Two_Dimensional_Array.shape}")
print(f"Dimension: {Two_Dimensional_Array.ndim}")
print(f"Shape:{Two_Dimensional_Array.shape}")

# Adding new axis
Two_Dimensional_Array = np.random.random(size=(3, 3))
print(f"Value:\n{Two_Dimensional_Array}")
new = Two_Dimensional_Array[np.newaxis, :]
print(f"New: {new}")
print(f"Dimension: {new.ndim}")
print(f"Shape:{new.shape}")


row_vector = Two_Dimensional_Array[np.newaxis, :]
print(f"row_vector: {row_vector}")
print(f"dimension: {row_vector.ndim}")
print(f"shape:{row_vector.shape}")
print(f"reshape:\n{np.reshape(row_vector, shape=(3, 3, 1), order='c')}")
print(f"reshape:{np.reshape(row_vector, shape=(3, 3, 1), order='c').shape}")


column_vector = Two_Dimensional_Array[:, np.newaxis]
print(f"column_vector: {column_vector}")
print(f"dimension: {column_vector.ndim}")
print(f"shape:{column_vector.shape}")
# print(f"reshape:\n{np.reshape(row_vector, shape=(3, 3, 1), order='c')}")
# print(f"reshape:{np.reshape(row_vector, shape=(3, 3, 1), order='c').shape}")
