# Adding, Removing, and sorting elements

# Importing Numpy
import numpy as np

# Sorting
arr = np.array([8, 10, 1, 4, 6, 2, 3, 9])
arr = np.sort(arr)
print(arr)

# argsort
print(f"Argsort: {arr.argsort()}")  # location
print(f"Argsort: {np.argsort(arr)}")  # location

# lexsort
First_Name = np.array(['Raj', 'Prabin', 'Guber', 'Michal'])
Last_Name = np.array(['Kumar', 'Rai', 'Singh', 'Basti'])
indication = np.lexsort((First_Name, Last_Name))
print(f"Lexsort: {indication}")
print(f"Lexsort: {np.lexsort((First_Name, Last_Name))}")
order = indication
print(list(zip(First_Name[order], Last_Name[order])))

# Concatination
arr_1 = np.array([1, 2, 3, 4])
arr_2 = np.array([2, 4, 6, 8])
arr = np.concatenate((arr_1, arr_2))
print(arr)
print(np.sort(arr))


# Reshape
a = np.array([0, 1, 2, 3, 4, 5])  # contains 6 elements
print(f"Orginal array: {a}")

b = a.reshape(3, 2)  # product of 3 * 2 = 6 elements
print(f"Reshaped array:\n {b}")  # Output: array([[0, 1], [2, 3], [4, 5]])

b = np.reshape(a, shape=(3, 2), order='C')
print(f"Reshaped array:\n {b}")  # Output: array([[0, 1], [2, 3], [4, 5]])
