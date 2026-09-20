# Numpy

NumPy is a Python library used for working with arrays.

It also has functions for working in domain of linear algebra, fourier transform, and matrices.

NumPy stands for __Numerical Python__.

In Python we have lists that serve the purpose of arrays, but they are slow to process.

NumPy aims to provide an array object that is up to __50x faster than traditional Python lists__.

The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently. NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.

## Basics

### Creating Arrays

The array object in NumPy is called ndarray.

```
import numpy as np

# from list
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# from tuple
arr = np.array((1, 2, 3, 4, 5))
print(arr)

# 0-D Arrays or Scalars, are the elements in an array
arr = np.array(42)
print(arr) 

# Create a 1-D array containing the values 1,2,3,4,5:
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr) 

# Check Number of Dimensions
print(arr.ndim) 

# Create an array with 5 dimensions and verify that it has 5 dimensions:
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim) 
```

### Array Indexing

```
import numpy as np

# Get the second element from the following array.
arr = np.array([1, 2, 3, 4])
print(arr[1])

# Access the element on the first row, second column:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])          // 2

# 
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])                                   // 6
```

### Array Slicing

```
# Slice elements from index 1 to index 5 from the following array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

# slice index 1 to index 4 (not included), this will return a 2-D array:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])
```

### NumPy data types

NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

```
    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )

# Create an array with data type string:
import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

# Change data type from float to integer by using int as parameter value:
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype) 
```

The main difference between a __copy__ and a __view__ of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

### Shape and Reshape

The __shape__ of an array is the number of elements in each dimension.

```
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)                      // (2, 4)
```

Reshaping means changing the shape of an array.
```
# Convert the following 1-D array with 12 elements into a 2-D array
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)               

// [[ 1  2  3]
//  [ 4  5  6]
//  [ 7  8  9]
//  [10 11 12]]

# Iterate on the elements of the following 2-D array:
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y) 

// result
1
2
3
4
5
6
7
8
9
10
11
12

# nditer
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x) 

// result
1
2
3
4
5
6
7
8
```

### Joining Array

Joining means putting contents of two or more arrays in a single array.

In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.

```
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)                  // [1 2 3 4 5 6]

# 2D arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)                  // [[1 2 5 6]
                            //  [3 4 7 8]]
```

### Splitting NumPy Arrays

Splitting is reverse operation of Joining. Splitting breaks one array into multiple.

```
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr) 

// [array([1, 2]), array([3, 4]), array([5, 6])]
```

### Searching Arrays

You can search an array for a certain value, and return the indexes that get a match.

To search an array, use the where() method.

```
# Find the indexes where the value is 4:
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)                          // (array([3, 5, 6]),) 

# Find the indexes where the values are even
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x) 
```

### Filtering Arrays

Getting some elements out of an existing array and creating a new array out of them is called filtering.

In NumPy, you filter an array using a boolean index list. If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

```
# Create an array from the elements on index 0 and 2:
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)                     // [41 43]
```

### Data Distribution

Data Distribution is a list of all possible values, and how often each value occurs.

Such lists are important when working with statistics and data science.

The random module offer methods that returns randomly generated data distributions.

__Random Distribution__: A random distribution is a set of random numbers that follow a certain probability density function.

```
Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
The probability for the value to be 3 is set to be 0.1
The probability for the value to be 5 is set to be 0.3
The probability for the value to be 7 is set to be 0.6
The probability for the value to be 9 is set to be 0

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x) 

```

__Normal Distribution__: The Normal Distribution is one of the most important distributions.

It has three parameters:
- loc - (Mean) where the peak of the bell exists.
- scale - (Standard Deviation) how flat the graph distribution should be.
- size - The shape of the returned array.

```
# Generate a random normal distribution of size 2x3:
from numpy import random
x = random.normal(size=(2, 3))
print(x)

// result
[[-1.28581037 -2.27796264 -1.14552427]
 [-0.77853285 -1.64757371  0.14998528]]
```

