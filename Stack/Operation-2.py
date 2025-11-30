# Importing NumPy
import numpy as np

a1 = np.array([
    [1, 1],
    [2, 2]
])

a2 = np.array([
    [3, 3],
    [4, 4]
])

# Vertical stacking
Vertical_stacking = np.vstack((a1, a2))
print(f"Virtual Stacking: {Vertical_stacking}")

# Horizantal Stacking
horizontal_stacking = np.hstack((a1, a2))
print(f"Horizontal Stacking: {horizontal_stacking}")

# Spliting
x = np.arange(0, 25).reshape(5, 5)
print(f"x:\n {x}")

y = np.vsplit(x, 5)
print(f"Vertical splitting:\n {y}")

y = np.hsplit(x, 5)
print(f"Horizontal splitting: {y}")

# another
x = np.arange(1, 25).reshape(2, 12)
print(f"x:\n{x}")

y = np.vsplit(x, 2)
print(f"Vertical Splitting:\n {y}")

y = np.hsplit(x, 3)
print(f"Horizantal Splitting:\n {y}")

# Viewing Method
Orginal_Data = np.arange(1, 13).reshape(3, 4)
# print(f"Orginal data:\n {Orginal_Data}")

Temperory_Data = Orginal_Data[0, :]
print(f"Temperory data:\n {Temperory_Data}")

Temperory_Data[0] = 99
print(f"Temperory Data:\n {Temperory_Data}")
print(f"Orginal Data:\n {Orginal_Data}")

# Using copy()
Copied_Data = Orginal_Data.copy()
print(f"Copied Data:\n {Copied_Data}")

Copied_Data[0][0] = 1
print(f"Rearrangement in Copied_Data:\n {Copied_Data}")
print(f"Orginal Data:\n {Orginal_Data}")
