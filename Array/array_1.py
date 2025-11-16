# Importing Numpy
import numpy as np
import math as mt

# Numerical Arrays
# Applying numpy 1th dimension array
array = np.array([1, 2, 3, 4, 5])
# Multiplying array
array = array * 2
# printing outputs
print(array)
# Pringting its type like integer, float, double
print(array.dtype)
# Printing its shape
print(array.shape)

array = np.array(1)
print(array)
print(array.dtype)

# 0D array
One_Dimension_Array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(f"Array Value: {One_Dimension_Array}")
print(f"Dimesion:{One_Dimension_Array.ndim}")
print(f"Shape: {One_Dimension_Array.shape}")
print(f"Size: {One_Dimension_Array.size}")
print(f"Array datatype:{One_Dimension_Array.dtype}")

# Slice notation
print(f"3 first data of the Array: {One_Dimension_Array[:3]}")

# 2D array or Matrix
Two_Dimension_Array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(f"Array value:{Two_Dimension_Array}")
print(f"Dimension: {Two_Dimension_Array.ndim}")
print(f"Shape: {Two_Dimension_Array.shape}")
print(f"Size: {mt.prod(Two_Dimension_Array.shape)}")
print(f"Array Datatype: {Two_Dimension_Array.dtype}")

# Slice in 1D - looped row and n column values: e.g.,Mid-range in the array
# [2, 5, 8]
print(f"3 values in the array: {Two_Dimension_Array[:, 1]}")


# String Arrays
print("\nString Array\n")
String_Array = np.array(['Buddha', 'Sagar', 'kilton', 'Hilton'])

print(f"Array Values: {String_Array}")
print(f"Dimension: {String_Array.ndim}")
print(f"Shape: {String_Array.shape}")
print(f"Datatype: {String_Array.dtype}")

# Basic Arrays [np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace()]
# np.zeros()
print("\nZeros\n")
Zeros = np.zeros(2)
# >> Generates 2 zeros array i.e array([0.0, 0.0])
print(f"Zeros: {Zeros}")
print(f"Dimension: {Zeros.ndim}")
print(f"Size: {Zeros.size}")
print(f"type: {Zeros.dtype}")

# np.ones()
print("\nOnes\n")
Ones = np.ones(2)
# > Generating 2 ones i.e aray[(1.0, 1.0)]
print(f"Ones: {Ones}")
print(f"dimension: {Ones.ndim}")
print(f"Size: {Ones.size}")
print(f"type: {Ones.dtype}")

# np.empty()
print("\nEmpty\n")

Empty = np.empty(2)
# > Generates 2 empty sets
print(f"Empty:{Empty}")
print(f"Dimension: {Empty.ndim}")
print(f"shape: {Empty.shape}")
print(f"Size: {mt.prod(Empty.shape)}")
print(f"Type: {Empty.dtype}")

# np.arrange()
print("Arrange")

Arange = np.arange(4)
# > Generates 4 arranged values i.e., array([0,1,2,3])
print(f"Arrange: {Arange}")
print(f"Dimension: {Arange.ndim}")
print(f"Shape: {Arange.shape}")
print(f"size: {Arange.size}")
print(f"type: {Arange.dtype}")

# Also can be in this format
print("Arange 2nd method:\n")
Arange = np.arange(0, 4, 1)
# np.arrange(Start, end, step)

print(f"Arrange: {Arange}")
print(f"Dimension: {Arange.ndim}")
print(f"Shape: {Arange.shape}")
print(f"size: {Arange.size}")
print(f"type: {Arange.dtype}")

# np.linspace()
print("Line space: \n")

Linespace = np.linspace(0, 10, num=5)
# generates the values into 5 parts start = 0 and ends in 10

print(f"Values: {Linespace}")
print(f"Dimesion: {Linespace.ndim}")
print(f"Shape: {Linespace.shape}")
print(f"size: {Linespace.size}")
print(f"type: {Linespace.dtype}")
