# Array

## **What is Array??**

[>] In computer programming, an array is a structure for storing and retrieving data.

[>] There 'n' dimension of arrays like 1D, 2D, 3D and such.

[>] In Numpy, this idea is generalized to an arbitrary number of dimensions, and so the fundamental array class is called `ndarry`: it represents an 'N-dimensional array'.

[>] Most Numpy arrays have some restrictions. For instance:

[1.] All elements of the array must be same type of data.

[2.] Once created, the total size of the array can't be change.

[3.] The shape must be "rectangular", not "jagged", e.g., each row of a two-dimensional array must have same number of columns.

## **Dimension**

[>] In NumPy, a dimension of an array is somethings referred as an "axis".

[>] The terminology may be useful to disambiguate between the dimensionality of an array and the dimensionality of the data represented by the array.


## **Slice in Array**

[>] In Python, slicing is a method used to extract specific portions of sequences such as string, lists, tuples, ranges, and bytes.


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


# **Recommend videos**

## About array: 
[-] <a href="https://www.youtube.com/watch?v=NptnmWvkbTw">Array 9.1 - Processing Tutorial</a>
[-] <a href="https://www.youtube.com/watch?v=47JBVxCWXJA">Array 9.2 - Processing Tutorial</a>
