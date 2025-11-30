<h2><b>How to create an array from existing data</b></h2>
<p>
  This section utilizes <b>Slicing</b>, <b>numpy.vstack()</b>, <b>numpy.hstack()</b>, <b>numpy.hsplit</b>, <b>.view</b>, <b>copy</b>.
</p>
<p>
  We can easily create an array from a section of an existing arra. Lets say
</p>


```
a = numpy.arange(1,11,steps=1)
```

<p>We can create a new array from a section of the array anytime by specifying where we want to slice that array.</p>

```
arr1 = a[3:8]
print(arr1)
# Output: array([4, 5, 6, 7, 8])
```

```
a = np.arange(0, 20, 2, dtype=int)
print(f"Value of const array: {a}")
print(f"Dimension: {a.ndim}")
print(f"Shape and size: {a.shape} & {a.size}")

# slicing
Sliced_array = a[3:8]
print(f"Sliced array: {Sliced_array}")
```

<p>Here, we grabbed a section of the array(named a) from index position 3 through index position 8 but not including position 8 itself</p>

<reminder>Reminder: Array indexes begin at 0. This means the first element of the array is at index 0, the second element is at index 1, and so on.</reminder>

<p>We can also stack two existing arrays, both vertically and horizontially. Lets consider array <b>a1</b> and <b>a2</b>:</p>

```
a1 = np.array([
    [1, 1],
    [2, 2]
])

a2 = np.array([
    [3, 3],
    [4, 4]
])

virtual_stacking = np.vstack((a1, a2))
print(f"Virtual Stacking: {virtual_stacking}")

horizontal_stacking = np.hstack((a1, a2))
print(f"Horizontal Stacking: {horizontal_stacking}")
```

<p>Vertical and horizontial stacking utilizes <b>numpy.vstack()</b> and <b>numpy.hstack()</b> to stack array <b>a1</b> and <b>a2</b>. </p>

```
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
```

We can use **numpy.vstack()** and **numpy.hstack()** to rearrange the array.

```
Output:
Virtual Stacking: [[1 1]
 [2 2]
 [3 3]
 [4 4]]

Horizontal Stacking: [[1 1 3 3]
 [2 2 4 4]]
```

We can split an array into several smaller arrays using **numpy.hsplit()** and **numpy.vsplit()**. 

```
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
```

We have split the array into 5, 2 and 3 equal parts of the array **arange()** and **reshape()**.

```
x:
 [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
Vertical splitting:
 [array([[0, 1, 2, 3, 4]]), array([[5, 6, 7, 8, 9]]), array([[10, 11, 12, 13, 14]]), array([[15, 16, 17, 18, 19]]), array([[20, 21, 22, 23, 24]])]
Horizontal splitting: [array([[ 0],
       [ 5],
       [10],
       [15],
       [20]]), array([[ 1],
       [ 6],
       [11],
       [16],
       [21]]), array([[ 2],
       [ 7],
       [12],
       [17],
       [22]]), array([[ 3],
       [ 8],
       [13],
       [18],
       [23]]), array([[ 4],
       [ 9],
       [14],
       [19],
       [24]])]
x:
[[ 1  2  3  4  5  6  7  8  9 10 11 12]
 [13 14 15 16 17 18 19 20 21 22 23 24]]
Vertical Splitting:
 [array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]]), array([[13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]])]
Horizantal Splitting:
 [array([[ 1,  2,  3,  4],
       [13, 14, 15, 16]]), array([[ 5,  6,  7,  8],
       [17, 18, 19, 20]]), array([[ 9, 10, 11, 12],
       [21, 22, 23, 24]])]
```

We can use view method to create a new array object that looks at same data as the original array (a shallow copy)

Views are an important NumPy concept! NumPy functions, as well as operations like indexing and slicing, will return views whenever possible.This saves memory and is faster (no copy of data has to be made). However it's important to be aware of this-modifying data in view also modifies the original array!

```
Orginal_Data = np.arange(1, 13).reshape(3, 4)
# print(f"Orginal data:\n {Orginal_Data}")

Temperory_Data = Orginal_Data[0, :]
print(f"Temperory data:\n {Temperory_Data}")

Temperory_Data[0] = 99
print(f"Temperory Data:\n {Temperory_Data}")
print(f"Orginal Data:\n {Orginal_Data}")
```

Using the **copy()** method will make a complete copy of the array and its data (a deep copy). We could use this method to make a copy and do whatever we want for the project and so on.

```
# Using copy()
Copied_Data = Orginal_Data.copy()
print(f"Copied Data:\n {Copied_Data}")

Copied_Data[0][0] = 1
print(f"Rearrangement in Copied_Data:\n {Copied_Data}")
print(f"Orginal Data:\n {Orginal_Data}")
```


