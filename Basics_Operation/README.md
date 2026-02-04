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

# Broadcasting

Broadcasting in numpy is a powerful mechanism that allows arrays of different shapes to be combined in arithmetic operations without explicit reshaping.
***Purpose***: It eliminates the need for explicit loops and reduces memory usage by reusing data instead of copying it.
***Efficiency***: Operations are vectorized and executed in optimized C code rather than slower Python loops. 

**Example 1: Array with Scalar**
There are times when we might want to carryout an operation between arry and a single number (also called an operation between a vector and a scalar) or between arrays of two different sizes. For example, array (simply referred as "data") might contain information about distance in miles but we want to cover the information to kilometers. we can perform operation with:

```
python
data = np.array([1.0,2.0], dtype=np.float32)
print(f"Data in Miles: {data}")
print(f"Data in Kilometers: {data * 1.6}")
```

Output:
```
Data in Miles: [1. 2.]
Data in Kilometers: [1.6 3.2]
```

<image src="https://numpy.org/doc/stable/_images/np_multiply_broadcasting.png"> Figure. Conversion from miles to Kilometer </image>

Numpy understands that the multiplication should happen with each cell. That concept is called broadcasting.

**Example 2: Array with Different Shapes**

```python
a = np.array([13,12,15])
b = np.array([
    [10],
    [12],
    [16]
             ])
print(f"Data a: {a}")
print(f"Data b: {b}")
print(f"Multiplication a * b: {a * b}")
```

Output:
```
Data a: [13 12 15]
Data b: [[10]
 [12]
 [16]]
Multiplication a * b: [[130 120 150]
 [156 144 180]
 [208 192 240]]
```

## Advantages of Broadcasting
1. Eliminates explicit loops
2. Improves performance
3. Simplifies code

## Limitation of Broadcasting
1. Can cause memory inefficiency if arrays are very large
2. May lead to confusion if shapes are not carefully checked
3. Broadcasting errors occurs when shapes are incompatible.


# Most useful array operations

This section covers maximum, minimum, sum, mean, product, standard deviation, and more.

Numpy also performs aggregation functions. In addition to *min*,*max* and *sum*. we can run *mean* to get the average, *prod* to get the result of multiplying the elements together, *std* to get the standard deviation, and more.

```Python
data = np.array([2,4,6,8,10,12,16],dtype=np.float32)
print(f"Max value: {data.max()}")
print(f"Min value: {data.min()}")
print(f"Sum of all values: {data.sum()}")
```

Output:
```
Max value: 16.0
Min value: 2.0
Sum of all values: 58.0
```

For Matrix:
```Python
matrix_a = np.array([
    [2,4,6],
    [1,3,5],
    [3,4,6]
])
print(f"Matrix A:\n{matrix_a}")
print(f"Shape of Matrix A: {matrix_a.shape}")
print(f"Transpose of Matrix A:\n{matrix_a.T}")
print(f"Max value in Matrix A: {matrix_a.max()}")
print(f"Min value in Matrix A: {matrix_a.min()}")
print(f"Sum of all values in Matrix A: {matrix_a.sum()}")
```

Output:
```
Matrix A:
[[2 4 6]
 [1 3 5]
 [3 4 6]]
Shape of Matrix A: (3, 3)
Transpose of Matrix A:
[[2 1 3]
 [4 3 4]
 [6 5 6]]
Max value in Matrix A: 6
Min value in Matrix A: 1
Sum of all values in Matrix A: 34
```

We can aggregate all the values in matrux and we can aggregate them across columns or rows using *axis* parameter.

```python
print(f"Max value in Matrix A: {matrix_a.max(axis=0)}")
print(f"Min value in Matrix A: {matrix_a.min(axis=0)}")
print(f"Sum of all values in Matrix A: {matrix_a.sum(axis=0)}")
```

Output:
```
Max value in Matrix A: [3 4 6]
Min value in Matrix A: [1 3 5]
Sum of all values in Matrix A: [ 6 11 17]
```