import numpy as np

print( "\n====================================" )
print( "\nCreating a Numpy Array" )
print( "\n====================================" )

# Creating a rank 1 Array
print( "---- Creating a rank 1 Array" )
arr = np.array([1, 2, 3])
print("Array with Rank 1: \n",arr)
 
# Creating a rank 2 Array
print( "\n---- Creating a rank 2 Array" )
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Array with Rank 2: \n", arr)
 
# Creating an array from tuple
print( "\n---- Creating an array from tuple" )
arr = np.array((1, 3, 2))
print("\nArray created using passed tuple:\n", arr)

print( "\n====================================" )
print( "\nData Types in Numpy" )
print( "\n====================================" )

# Integer datatype guessed by Numpy
print( "\n---- Integer datatype guessed by Numpy" )
x = np.array([1, 2])  
print("Integer Datatype: ")
print(x.dtype)         
 
# Float datatype guessed by Numpy
print( "\n---- Float datatype guessed by Numpy" )
x = np.array([1.0, 2.0]) 
print("\nFloat Datatype: ")
print(x.dtype)  
 
# Forced Datatype
print( "\n---- Forced Datatype" )
x = np.array([1, 2], dtype = np.int64)   
print("\nForcing a Datatype: ")
print(x.dtype)


print( "\n====================================" )
print( "\nBasic Array Operations" )
print( "\n====================================" )

# Defining Array 1
print( "\n---- Defining Arrays 1 and 2" )
a = np.array([[1, 2],
              [3, 4]])
 
# Defining Array 2
b = np.array([[4, 3],
              [2, 1]])
               
# Adding 1 to every element
print( "\n---- Adding 1 to every element" )
print ("\nAdding 1 to every element:", a + 1)
 
# Subtracting 2 from each element
print( "\n---- Subtracting 2 from each element" )
print ("\nSubtracting 2 from each element:", b - 2)
 
# sum of array elements Performing Unary operations
print( "\n---- sum of array elements Performing Unary operations" )
print ("\nSum of all array elements: ", a.sum())
 
# Adding two arrays
print( "\n---- adding two arrays" )
print ("\nArray sum:\n", a + b)

# Square root of Array
print( "\n---- Square root of Array" )
Sqrt = np.sqrt(a)
print("\nSquare root of Array1 elements: ")
print(Sqrt)
 
# Transpose of Array using In-built function 'T'
print( "\n---- Transpose of Array using In-built function 'T'" )
Trans_arr = a.T
print("\nTranspose of Array: ")
print(Trans_arr)

