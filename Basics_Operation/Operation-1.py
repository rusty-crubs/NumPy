# Importing NumPy
import numpy as np

data = np.array([1, 2],)
print(f"Data:{data}")
ones = np.ones(2, dtype=int)
print(f"Ones:{ones}")
print(f"Summation between {data} and {ones} is {data + ones}")
print(f"The difference between {data} and {ones} is {data - ones}")
print(f"The product of {data} and {ones} is {data * ones}")
print(f"The division of {data} by {ones} is {data / ones}")

total = 0
i = 0
for i in range(len(data)):
    total += data[i]
print(f"Sum of elements in data:{total}")

Total = data.sum()
print(f"Total: {Total}")

Starting_Array = np.array([[1, 1], [2, 2]])

print(f"Axis of Rows: {Starting_Array.sum(axis=0)}")
print(f"Axis of Columns: {Starting_Array.sum(axis=1)}")

# Broadcasting
data = np.array([1.0, 2.0])
print(f"data * 1.6: {data * 1.6}")
