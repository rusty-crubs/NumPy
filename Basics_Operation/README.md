***<h2>Basic Array Operations</h2>***

This section covers the addition, subtraction, multiplication, division, and more.

***<h4>Addition</h4>***

We create two arrays namely **data** and **ones** respectively.

```
data = np.array([1, 2])
print(f"Data:{data}")
ones = np.ones(2, dtype=int)
print(f"Ones:{ones}")
```

<image src="https://numpy.org/doc/stable/_images/np_array_dataones.png">Fig. Data and ones arrays</image>

We can add the array together with the plus sign (+).

```
print(f"Summation between {data} and {ones} is {data + ones}")
# Output: array([2,3])
```

<image src="https://numpy.org/doc/stable/_images/np_data_plus_ones.png">Fig. Addition of data and ones</image>

**<h4>subtraction</h4>**

We can subtract the array using minus sign (-)

```
print(f"subtraction between {data} and {ones} is {data - ones}")
# Output: array([0, 1])
```

**<h4>Multiplication</h4>**

We can multiply the array using asterisk sign (*).

```
print(f"The product of {data} and {ones} is {data * ones}")
# Output: array([1, 2])
```

**<h4>Division</h4>**

We can divide the array using / sign.

```
print(f"The division of {data} by {ones} is {data / ones}")
# Output: array([1, 2])
```

We used to add the elements like this.

```
total = 0
i = 0

for i in range(len(data)):
    total += data[i]

print(f"Sum of elements in data:{total}")
# Output: 3
```

Basic operations are simple with NumPy. If we want to find the sum of the elements in the array, we could use **sum()**. This works for 1D, 2D arrays, and arrays in higher dimensions.

```
Total = data.sum()
print(f"Total: {Total}")
# output: 3
```

To add the rows or the columns in a 2D array, we can specify the axis:

Consider starting array as:
```
Starting_Array = np.array([[1, 1], [2, 2]])
```

For sum over the axis with rows:

```
print(f"Axis of Rows: {Starting_Array.sum(axis=0)}")
```

For sum over the axis of columns:

```
print(f"Axis of Columns: {Starting_Array.sum(axis=1)}")
```
