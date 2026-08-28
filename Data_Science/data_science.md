# DATA SCIENCE with python

In a world of data space where organizations deal with petabytes and exabytes of data, the era of Big Data emerged.
Data science is a field that involves using statistical and computational techniques to extract insights and knowledge from data.

It encompasses a wide range of tasks, including data cleaning and preparation, data visualization, statistical modeling, machine learning, and more. Data scientists use these techniques to discover patterns and trends in data, make predictions, and support decision-making.

Python has been considered the preferred choice among data scientists.

## Python Pandas

### install pandas

Open Visual Studio Code.
In terminal run the following command:

```
pip install pandas
```

### DataFrame

DataFrame is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns):

| id  | name  | phone      | age  |   
|---- | ----- | ---------- | ---- |
| 1   | Chris | 1234567890 | 40   |   <- row 1
| 2   | Tom   | 1234567891 | 10   |   <- row 2
| 3   | Kate  | 1234567892 | 11   |   <- row 3
| 4   | Mom   | 1234567893 | NULL |

columns: id, name, phone, age

In the real world, a Pandas DataFrame will be created by loading the datasets from existing storage, storage can be SQL Database, CSV file, and Excel file.

Dataframe can be created in different ways here are some ways by which we create a dataframe:

```
# import pandas as pd
import pandas as pd
 
# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)
```

Dataframe with column titles:

```
# Import pandas package
import pandas as pd
 
# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
print(df)
```

Select columns:

```
# select two columns
print(df[['Name', 'Qualification']])
```

Read data from file and select a data item

```
data = pd.read_csv("/home/kj/Krzys/git/computer-science-basics-tutorials/Data_Science/nba.csv", index_col ="Name")
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
print(first, "\n\n", second)
```

## Python Numpy

Numpy is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays.

Array in Numpy is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers. In Numpy, number of dimensions of the array is called rank of the array.A tuple of integers giving the size of the array along each dimension is known as shape of the array. An array class in Numpy is called as ndarray.

### Creating a Numpy Array

```
import numpy as np
 
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
```
### Data Types in Numpy

Every Numpy array is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers. Every ndarray has an associated data type (dtype) object. This data type object (dtype) provides information about the layout of the array. 

In Numpy, datatypes of Arrays need not to be defined unless a specific datatype is required. Numpy tries to guess the datatype for Arrays which are not predefined in the constructor function.

```
# Python Program to create a data type object
import numpy as np
 
# Integer datatype guessed by Numpy
x = np.array([1, 2])  
print("Integer Datatype: ")
print(x.dtype)         
 
# Float datatype guessed by Numpy
x = np.array([1.0, 2.0]) 
print("\nFloat Datatype: ")
print(x.dtype)  
 
# Forced Datatype
x = np.array([1, 2], dtype = np.int64)   
print("\nForcing a Datatype: ")
print(x.dtype)
```

### Basic Array Operations
```
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
Sqrt = np.sqrt(a)
print("\nSquare root of Array1 elements: ")
print(Sqrt)
 
# Transpose of Array using In-built function 'T'
Trans_arr = a.T
print("\nTranspose of Array: ")
print(Trans_arr)
```

## Python Machine Learning Library with scikit-learn 

scikit-learn is an open-source Python library that implements a range of machine learning, pre-processing, cross-validation, and visualization algorithms using a unified interface.

* Simple and efficient tools for data mining and data analysis. It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means, etc.
* Built on the top of NumPy, SciPy, and matplotlib.

### Installation

```
pip install -U scikit-learn
```

### Load an exemplar dataset

```
from sklearn.datasets import load_iris 
iris = load_iris() 
    
# store the feature matrix (X) and response vector (y) 
X = iris.data 
y = iris.target 
    
# store the feature and target names 
feature_names = iris.feature_names 
target_names = iris.target_names 
    
# printing features and target names of our dataset 
print("Feature names:", feature_names) 
print("Target names:", target_names) 
    
# X and y are numpy arrays 
print("\nType of X is:", type(X)) 
    
# printing first 5 input rows 
print("\nFirst 5 rows of X:\n", X[:5])
```

### Splitting the dataset

One important aspect of all machine learning models is to determine their accuracy. Now, in order to determine their accuracy, one can train the model using the given dataset and then predict the response values for the same dataset using that model and hence, find the accuracy of the model. 

```
# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)
  
# printing the shapes of the new X objects
print(X_train.shape)
print(X_test.shape)
  
# printing the shapes of the new y objects
print(y_train.shape)
print(y_test.shape)
```

### Training the model

Scikit-learn provides a wide range of machine learning algorithms that have a unified/consistent interface for fitting, predicting accuracy, etc.

```
# training the model on training set
from sklearn.neighbors import KNeighborsClassifier

# We create a knn classifier object using:
knn = KNeighborsClassifier(n_neighbors=3)

# The classifier is trained using X_train data. The process is termed fitting
knn.fit(X_train, y_train)
  
# making predictions on the testing set, test our classifier on the X_test data. knn.predict method is used for this
y_pred = knn.predict(X_test)
  
# comparing actual response values (y_test) with predicted response values (y_pred)
from sklearn import metrics
print("kNN model accuracy:", metrics.accuracy_score(y_test, y_pred))
  
# making prediction for out of sample data
sample = [[3, 5, 4, 2], [2, 3, 5, 4]]
preds = knn.predict(sample)
pred_species = [iris.target_names[p] for p in preds]
print("Predictions:", pred_species)
  
# saving the model
import joblib
joblib.dump(knn, 'iris_knn.pkl')
```

## Introduction to Matplotlib

Matplotlib is a multi-platform data visualization library built on NumPy arrays and designed to work with the broader SciPy stack.

### Installation

```
pip install -U matplotlib
```

### Basic plots in Matplotlib

```
# importing matplotlib module
from matplotlib import pyplot as plt
 
# x-axis values
x = [5, 2, 9, 4, 7]
 
# Y-axis values
y = [10, 5, 8, 4, 2]
 
# Function to plot
plt.plot(x,y)
 
# function to show the plot
plt.show()
```


## References

https://www.geeksforgeeks.org/data-science-tutorial/
