# Array

## **What is Array??**

[>] In computer programming, an array is a structure for storing and retrieving data.

[>] There 'n' dimension of arrays like 1D, 2D, 3D and such.

[>] In Numpy, this idea is generalized to an arbitrary number of dimensions, and so the fundamental array class is called `ndarry`: it represents an 'N-dimensional array'.

[>] Most Numpy arrays have some restrictions. For instance:

[1.] All elements of the array must be same type of data.

[2.] Once created, the total size of the array can't be change.

[3.] The shape must be "rectangular", not "jagged", e.g., each row of a two-dimensional array must have same number of columns.


## **Array Attributes**

<p>
    Attributes of an arrays are:
    <ul>
    <li> <b>ndim</b>,   </li>
    <li> <b>shape</b>,  </li>
    <li> <b>size</b>, and</li>
    <li> <b>dtype</b>   </li>
</p>

### **ndim**

[-] This determines the number of dimension present in the targeted array or object.

### **shape**

[-] This determines the internal shapes. like 

Python
Object = np.array([
  [1,2],
  [3,4]
])


Output: shape: array([2,2])

### **size**

[-] This determines the size of the targeted object 

[-] if we import math library and apply product in shape we'll also get size of the object for dimension greater then 1D. i.e., size = mt.prod(Object.shape)

### **dtype**

[-] This determines the data type of targeted objects. i.e., objects.dtype or type(objects)

## **Basic Array**

[-] Contains np.zeros(), np.ones(), np.empty(), np.arrange(), np.linspace()

### **numpy.zeros()**

[-] Generates instructed number of zeros. Such as numpy.zeros(2) output:array([0.0,0.0])

### ***numpy.ones()***

[-] Generates instructed number of ones. Such as numpy.ones(2) output: array([1.0,1.0])

### ***numpy.empty()***

[-] Creates an array with 'n' different values.

### ***numpy.arange()***

[-] Its has 2 ways to do work

[1.] **numpy.arange(number)** : generates ascending order of values initilly starting from 0 to number - 1.

[2.] **numpy.arange(start,end,steps)**: generates array from start to end with instructed steps or space between elements.

### ***numpy.linspace()***

[-] Line space generates array with number of values instructed with its initial and final point. Such that numpy.linespace(initial, final, number_of_values)


## **Adding, Removing, and Sorting elements**

[-] Covers numpy.sort(), numpy.concatenate()

### ***numpy.sort()***

[>] Sorting an array is a simple with **np.sort()**. You can arrange any scrambled data or value with it.

[>] In addition to sort, which return a sorted copy of an array, you can say

[1.] ***argsort***, which is an indirect sort along a specified axis.

[2.] ***lexsort***, which is an indirect stable sort on multiple keys,

```
# lexsort
First_Name = np.array(['Raj', 'Prabin', 'Guber', 'Michal'])
Last_Name = np.array(['Kumar', 'Rai', 'Singh', 'Basti'])
indication = np.lexsort((First_Name, Last_Name))
print(f"Lexsort: {indication}")
print(f"Lexsort: {np.lexsort((First_Name, Last_Name))}")
order = indication
print(list(zip(First_Name[order], Last_Name[order])))
```

[3.] ***searchsorted***, which will find elements in a sorted array, and 

[4.] ***partition***, which is a partial sort.


### ***numpy.concatenate()***

[>] Combining two arrays is simple with **np.concatenate()**. You can combine any two arrays with it. i.e.,

```
> arr_1 = np.array([1, 2, 3, 4])
> arr_2 = np.array([2, 4, 6, 8])
> arr = np.concatenate((arr1, arr_2))
```


## ***Shape and Size of an array***

This section covers **ndarray.ndim**, **ndarray.size**, **ndarray.shape**.

### **ndarray.ndim**: 

[>] Tells the number of axis, or dimensions of the array.

### **ndarray.size**

[>] Tells the total number of elements of the array. 
[>] Product of the elements of the array's shape.

### **ndarray.shape**

[>] Display a tuples of integers that indicate the number of elements stored along each dimension of the array.


## ***Reshape***

[>] using **arr.reshape(rows, columns)** will gice a new shape to an array without changing the data.
[>] [!Reminder] When you use the reshape method, the array you want to produce needs to have same number of elements as the original array.

```
Python
a = np.array([0, 1, 2, 3, 4, 5]) # contains 6 elements
print(a)

b = a.reshape(3, 2) # product of 3 * 2 = 6 elements
print(b) # Output: array([[0, 1], [2, 3], [4, 5]])
```

[>] Also, we could use **np.reshape(array_name, shape = (row, columns), order='C')** to reshape array.

```
print(np.reshape(a, shape(3,2), order='C'))  # Output: array([[0, 1], [2, 3], [4, 5]])
```

[>] Where order is memory layout order for reading or writing elements such that:

[1.] "C"- row-major default, read/write the elements using C-like index order;

[2.] "F"- column-major Fortran, read/write elements in Fortran-like index order;

[3.] "A"- preserve original if possible, read/write the elements in Fortran-like index order if a is Fortran contiguous in memory.

## **Dimension**

[>] In NumPy, a dimension of an array is somethings referred as an "axis".

[>] The terminology may be useful to disambiguate between the dimensionality of an array and the dimensionality of the data represented by the array.

[>] Two method to increase dimensions:

[1.] We could increase an object existing dimensions by increasing that object axis, through **numpy.newaxis**, which adds an additional layer of axis without affecting its elements.

```
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
```

[2.] we could increase an object dimensions through **numpy.expand_dims(array_name, axis= 0\1)**

```
a = np.arange(6)
print(a.shape) # output: 6

b = np.expand_dims(a, axis = 1)
print(b.shape) # output: (6,1)

c = np.expand_dims(a, axis=0)
print(c.shape) # output: (1,6)
```


## **Indexing and Slicing**

[>] In Python, slicing is a method used to extract specific portions of sequences such as string, lists, tuples, ranges, and bytes.

[>] You can index and slice NumPy array in the same ways you can slice Python list.

```
data = np.arange(0, 10, dtype=np.int32)
print(f"Data: {data}")
print(f"type: {data.dtype}")

print(f"First two value: {data[0:2]}")  # array[0 1]
print(f"Second two values: {data[1:3]}")  # array[1 2]
print(data[1:])  # array[1 2 3 4 5 6 7 8 9]
print(data[-1:])
print(data[:-1])
```

[>] we could visualize it

<image src="https://numpy.org/doc/stable/_images/np_indexing.png">

[>] You may want to take a section of your array or specific array elements to use in further analysis or additional operations. To do that, you'll need to subset, slice, and/or index your arrays.

[>] For example:

```
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5])

# output: array[1, 2, 3, 4]

```

[>] you can easily select values through this kind of slicing methods. Generally used to assign satisfactory resulting conditions to new array without effecting previous array.

[>] Basics conditioning and sampling methods like:

```
import numpy as np 
array = np.arange(0,10,dtype = int32)
print(f"Array values: {array}")

Divisible_by_2 = arrays[arrays % 2 == 0]
print(f"Divisible by 2: {Divisible_by_2}") # Output: array[0 2 4 6 8 10]

Less_than_5 = array[array < 5]
print(f"Less than 5: {Less_than_5}") # Output: array[0 1 2 3 4]

# conditions 
print(f"Numbers between 3 and 9: {array[ array > 3 & array < 9 ]}")

five_up = (array > 5) | (array == 5)
print(five_up)
```

[>] We can also use ***numpy.nonzero()*** to select elements or indices from an array.

```
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.nonzero(a < 5)
print(b) # Output: array([0, 0, 0, 0], arrays([0, 1, 2, 3]))
```

[>] In this example, a tuple of arrays was returned: one for each dimensions. The first array represents the row indices where these values are found, and the second array represents the column indices where the values are found.

[>] If we want to generate a list of coordinates where the elements exist, we can zip the arrays, iterate over the list of coordinates, and print them. For example:

```
list_of_coordinates = list(zip(b[0], b[1]))

for coordinates in list_of_coordinates:
    print(f"coordinates: {coordinates}")
```

[>] We can also use **numpy.zero()** to print the elements in an array that are less than 5 with:

```
print(a[b])
# Output: [1 2 3 4]
```

[>] If the element we're looking for doesn't exit in the array, then the returned array of indices will be empty. For example:

```
not_there = np.nonzero(a == 42)
print(not_there)
# Output: (array[], dtype=int64), array([],dtype=int64)
```

# **Recommend videos**

## About array: 
[-] <a href="https://www.youtube.com/watch?v=NptnmWvkbTw">Array 9.1 - Processing Tutorial</a>
[-] <a href="https://www.youtube.com/watch?v=47JBVxCWXJA">Array 9.2 - Processing Tutorial</a>
