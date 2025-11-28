# Indexing and Slicing

# Import Numpy
import numpy as np

data = np.arange(0, 10, dtype=np.int32)
print(f"Data: {data}")
print(f"type: {data.dtype}")

print(f"First two value: {data[0:2]}")  # array[0 1]
print(f"Second two values: {data[1:3]}")  # array[1 2]
print(data[1:])  # array[1 2 3 4 5 6 7 8 9]
print(data[-1:])
print(data[:-1])

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"Numbers less than 5: {a[a < 5]}")
print(f"NUmbers greater and equal to 5: {a[a >= 5]}")
print(f"Numbers divisible by 2: {a[a % 2 == 0]}")

# Checking the statements in the array applying a condition to be satisfied for
# satisfactory result
Condition = (a > 5) | (a == 5)
print(Condition)

# np.nonzero()
b = np.nonzero(a < 5)
print(f"nonzero: {b}")

list_of_coordinates = list(zip(b[0], b[1]))

for coordinates in list_of_coordinates:
    print(f"coordinates: {coordinates}")

print(f"Value of b:{a[b]}")

not_there = np.nonzero(a == 42)
print(f"Searching 42 in array a : {not_there}")
