# Python 3

# Table of Contents
- [basics](#basics)
- [advanced](#advanced)
  - [strong typing](#strongtyping)
  - [oop](#oop)
- [interview questions](#interview)

## Python basics <a id="basics"></a>

__Python Indentation__: Python uses indentation to indicate a block of code:
```
if 5 > 2:
  print("Five is greater than two!")
```

P__ython Variables:__ Python has no command for declaring a variable. Variable names are case-sensitive.
``` 
x = 5
y = "Hello, World!"

# assign many values to many variables
x, y, z = "Orange", "Banana", "Cherry"

# One Value to Multiple Variables
x = y = z = "Orange"

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
```

__Print Text__
```
print("Hello World!")

# same line
print("Hello World!", end=" ")

# print number
print(3)

# mixed
print("I am", 35, "years old.")
```

__Casting__: specify the data type of a variable
```
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

# Get the Type
print(type(x))
```

__global__: Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function. To create a global variable inside a function, you can use the global keyword 
```
# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x) 

# use the global keyword if you want to change a global variable inside a function.
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x) 
```

__Data Types__
```
Text Type: 	        str
Numeric Types: 	    int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	    dict
Set Types: 	        set, frozenset
Boolean Type: 	    bool
Binary Types: 	    bytes, bytearray, memoryview
None Type: 	        NoneType
```

__In Python 3, the integer type (int) has no maximum limit; it can grow as large as the available memory allows.__

maximum float value in Python is approximately 1.7976931348623157e+308

```
# Print the data type of the variable x:
x = 5
print(type(x))

x = "Hello World"                   //	str 	
x = 20 	                            // int 	
x = 20.5 	                        // float 	
x = 1j 	                            // complex 	
x = ["apple", "banana", "cherry"] 	// list 	
x = ("apple", "banana", "cherry") 	// tuple 	
x = range(6) 	                    // range 	
x = {"name" : "John", "age" : 36} 	// dict 	
x = {"apple", "banana", "cherry"} 	// set 	
x = frozenset({"apple", "banana", "cherry"}) 	//frozenset 	
x = True 	                        // bool 	
x = b"Hello" 	                    // bytes 	
x = bytearray(5) 	                // bytearray 	
x = memoryview(bytes(5)) 	        // memoryview 	
x = None
```

__Random Number__
```
# display a random number from 1 to 9
import random
print(random.randrange(1, 10))
```

__Strings__
```
# Multiline Strings: You can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 

# Strings are Arrays
a = "Hello, World!"
print(a[1])

# Loop through the letters in the word "banana":
for x in "banana":
  print(x)

# len
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

# Use negative indexes to start the slice from the end of the string: 
b = "Hello, World!"
print(b[-5:-2])

# upper
a = "Hello, World!"
print(a.upper())

# Remove Whitespace
a = " Hello, World! "
print(a.strip())

# replace
a = "Hello, World!"
print(a.replace("H", "J"))

# split
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 

# formatting
age = 36
txt = f"My name is John, I am {age}"
print(txt)
```

__Operators__
```
# Walrus Operator: assigns values to variables as part of a larger expression
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# Chaining Comparison Operators
x = 5
print(1 < x < 10)

# Identity Operators

# is: Returns True if both variables are the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)   // True
print(x is y)   // False

# ==  Checks if the values of both variables are equal
print(x == y)   // True

# Membership Operators

# in: Returns True if a sequence with the specified value is present in the object
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)      // True         
```

__Lists__
```
mylist = ["apple", "banana", "cherry"]

# List items can be of any data type:
list1 = ["abc", 34, True, 40, "male"]

# lists are defined as objects with the data type 'list'
mylist = ["apple", "banana", "cherry"]
print(type(mylist))       // <class 'list'>

# Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change the second value by replacing it with two new values
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)                       // ['apple', 'blackcurrant', 'watermelon', 'cherry']

# Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)                     // ['apple', 'orange', 'banana', 'cherry']

# Remove the first occurrence of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 

# Comprehention
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)                    // ['apple', 'banana', 'mango']

# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)                      // ['a', 'b', 'c', 1, 2, 3]
```

__Tuples__: are used to store multiple items in a single variable.

Tuple items are __ordered, unchangeable__, and allow duplicate values.

```
mytuple = ("apple", "banana", "cherry")

# Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)                        // ("apple", "kiwi", "cherry")
```

__Sets__: used to store multiple items in a single variable.

A set is a collection which is __unordered, unchangeable, and unindexed__.
Sets __cannot have duplicates__.
Once a set is created, you cannot change its items, __but you can add new items__.

```
set1 = {"abc", 34, True, 40, "male"} 

# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x) 

# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)                    // {'orange', 'apple', 'cherry', 'banana'} 

# Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)                    // {'banana', 'cherry', 'apple', 'orange', 'kiwi'}

# Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)                    // {'apple', 'cherry'}

# loops
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x) 

# frozenset is an immutable version of a set.

```

__Dictionaries__: store data values in key:value pairs

A dictionary is a collection which is __ordered*, changeable and do not allow duplicates__.

```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) 

# The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} 

# Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020}) 

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Loop Through a Dictionary
for x in thisdict:
  print(x) 

for x in thisdict.values():
  print(x)

for x, y in thisdict.items():
  print(x, y) 

# copy
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 

# Print the name of child 2:
print(myfamily["child2"]["name"])
```

__Match__ statement: Instead of writing many if..else statements, you can use the match statement.

```
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

  # Use _ as the last case value if you want a code block to execute when there are not other matches:
  case _:
    print("Looking forward to the Weekend")

# combine values
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
```

__Loops__

```
# while 
i = 1
while i < 6:
  print(i)
  i += 1
  # break statement we can stop the loop even if the while condition is true:
  if i == 5:
    break
  # continue statement we can stop the current iteration, and continue with the next:
  if i == 3:
    continue
else:
  print("i is no longer less than 6")

# for
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
else:
  print("Finally finished!") 
```

__Functions__

A function is a block of code which only runs when it is called.

A function can return data as a result.

Python uses a mechanism called "pass-by-object-reference" (or "pass-by-assignment"), which means neither "pass-by-value" nor "pass-by-reference" strictly applies. The behavior depends on whether the object passed is mutable (changeable) or immutable (unchangeable).

When an immutable object is passed, it behaves like pass-by-value. If you attempt to "modify" the value inside the function, Python actually creates a new object and the local variable is reassigned to this new object, leaving the original object in the caller's scope unaffected. 
```
def modify_immutable(value):
    value += 1 # Creates a new int object and reassigns the local 'value'
    print(f"Inside function: {value}")

x = 5
print(f"Before function: {x}")
modify_immutable(x)
print(f"After function: {x}")

output:
Before function: 5
Inside function: 6
After function: 5
```

Behavior with Mutable Objects: Mutable objects include types like:  list (lists), dict (dictionaries), set (sets), Class instances 

When a mutable object is passed, it behaves like pass-by-reference. Since both the local variable and the original variable refer to the same object in memory, modifications made in-place to the object inside the function will be visible outside the function as we

Examples:

```
# define a function
def my_function():
  print("Hello from a function") 

# calling a function 
my_function()

# return values
def get_greeting():
  return "Hello from a function

# arguments
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")

# You can assign default values to parameters:
def my_function(country = "Norway"):
  print("I am from", country)

# with keyword arguments, the order of the arguments does not matter.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function(name = "Buddy", animal = "dog") 

# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, name):
  print("Hello", name)
my_function(name = "Emil") 

```

*args and **kwargs: allow functions to accept a unknown number of __arguments__.

Inside the function, args becomes a __tuple__ containing all the passed arguments so you cannot add new values (tuple cannot be changed)

The **kwargs parameter allows a function to accept any number of __keyword arguments__.
**kwargs uses __dictionaty__ and you can add new values.

```
# Using *args to accept any number of arguments:
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus") 

# You can combine regular parameters with *args.
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)
my_function("Hello", "Emil", "Tobias", "Linus") 

# Using **kwargs to accept any number of keyword arguments:
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes") 
```

__Scope__

```
# global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = 300
myfunc()
print(x) 

# nonlocal keyword, the variable will belong to the outer function:
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x
print(myfunc1())                  // hello
```

__Decorators__

Decorators let you add extra behavior to a function, without changing the function's code.

Decorator is a function that takes another function as input and returns a new function.

You can use multiple decorators on one function. This is done by placing the decorator calls on top of each other.

```
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

# One decorator for upper case, and one for adding a greeting:
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())
```

__Lambda__

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Lambda with Built-in Functions: map(), filter(), and sorted().

```
x = lambda a : a + 10
print(x(5)) 

# Double all numbers in a list:
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)                          // [2, 4, 6, 8, 10] 

# Filter out even numbers from a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
```

__Generators__

Generators are functions that can pause and resume their execution.

When a generator function is called, it returns a generator object, which is an iterator.

The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.

The __yield__ keyword is what makes a function a generator.

When yield is encountered, the function's state is saved, and the value is returned. The next time the generator is called, it continues from where it left off.

Generators allow you to iterate over data without storing the entire dataset in memory.

Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory

```
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value) 
```

example:
```
# Generator to read a large file line by line
def read_large_file(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            yield line.strip()

# Usage example:
# Assuming 'large_file.txt' is a large file on your system
for line in read_large_file('large_file.txt'):
    print(line)  # Process each line one by one

```


__Module__

Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.

To create a module just save the code you want in a file with the file extension .py:

Now we can use the module we just created, by using the import statement.

The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc).

file mymodule.py:
```
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
} 
def greeting(name):
  print("Hello, " + name) 
```

Use:
```
import mymodule
mymodule.greeting("Jonathan")

# You can choose to import only parts from a module, by using the from keyword.
from mymodule import person1
print (person1["age"])
```

__Package__

A Python package is a way to organize related Python modules into a single directory hierarchy. In simpler terms, a package is a collection of Python files (modules) that are grouped together to provide a specific set of functionality.

Here’s an example of how to organize a Python package with multiple files:
```
my_package/
    __init__.py   // special file is required to tell Python that the directory is a package (can be empty or contain initialization code).
    module1.py
    module2.py
    submodule/
        __init__.py     // This file indicates that submodule is a subpackage
        submodule1.py
        submodule2.py

```

how to use it:
```
# Importing a module from the package
from my_package import module1

# Accessing functions, classes, or variables from module1
module1.some_function()

# Importing from a submodule
from my_package.submodule import submodule1

# Accessing functions, classes, or variables from submodule1
submodule1.another_function()
```

__PIP__

PIP is a package manager for Python packages, or modules if you like.

__Try Except__

The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

```
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
```

```
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a valid integer!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

OR

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")
else:
    print(f"The result is {result}")

```

__Create custom Exception__

You do this by defining a new class that inherits from a built-in exception class, typically Exception or one of its subclasses.
- Define a new class: Create a new class and inherit from Exception (or one of its subclasses).
- Optionally, define an __init__ method: You can customize the initialization to accept additional information or parameters that describe the exception.
- Optionally, define a __str__ method: This method is used to return a custom error message when the exception is raised.

```
# Define a custom exception class with a custom __str__ method
class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
    
    def __str__(self):
        return f"Insufficient balance: {self.balance} available, but {self.amount} required."

# Using the custom exception
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    return balance - amount

try:
    balance = 100
    withdraw_amount = 150
    new_balance = withdraw(balance, withdraw_amount)
except InsufficientBalanceError as e:
    print(f"Caught an error: {e}")

```

__None__

None is a special constant in Python that represents the absence of a value.

Its data type is NoneType, and None is the only instance of a NoneType object.

__User Input__

```
print("Enter your name:")
name = input()
print(f"Hello {name}")
```

__Virtual Environment__

A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.

It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.

Think of a virtual environment as a separate container for each Python project. Each container:
- Has its own Python interpreter
- Has its own set of installed packages
- Is isolated from other virtual environments
- Can have different versions of the same package

```
# create it
python -m venv myfirstproject 

# activate it
myfirstproject\Scripts\activate

# install modules
pip install cowsay 

# deactivate
deactivate 
```


## Advanced <a id="advanced"></a>

### Strong typing <a id="strongtyping"></a>

In Python, you can achieve "strong typing" in a function by using
type hints for function parameters and return values, and then using an external static type checker like mypy to enforce them during development.

```
def sum_numbers(a: int, b: int) -> int:
    """
    Calculates the sum of two integers.
    """
    return a + b
```

Enforcing Types with a Static Type Checker:
```
pip install mypy
mypy calc.py
```

For more complex scenarios, the typing module provides advanced types

### Python OOP <a id="oop"></a>

https://www.w3schools.com/python/python_oop.asp

__Creating a class and object__

```
class MyClass:
  x = 5

# create object
p1 = MyClass()
print(p1.x)
```

__constructor__ =  __init__()__
All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age) 
```

The __self__ parameter is a reference to the current instance of the class. It is used to access properties and methods that belong to the class.

Without self, Python would not know which object's properties you want to access:

It __does not have to be named self__, you can call it whatever you like, but it has to be the first parameter of any method in the class:

__Class Properties__ are variables that belong to a class. They store data for each object created from the class.

You can access object properties using dot notation:

```
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model) 
```

Modify Properties:
```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print(p1.age)
```

__Class Properties vs Object Properties__

Properties defined inside __init__() belong to each object (instance properties).

Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:

```
class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species) 

# add new properties to existing objects
p1.city = "Oslo"
```

__Class Methods__ are functions that belong to a class. They define the behavior of objects created from the class.
```
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet() 
```

The __str__() Method: controls what is returned when the object is printed:
```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1) 
```

Python Inheritance: Inheritance allows us to define a class that inherits all the methods and properties from another class.

```
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  # When you add the __init__() function, the child class will no longer inherit the parent's __init__() function
  def __init__(self, fname, lname):

  # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
```

```
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) 
    # Add a property called graduationyear to the Student class:
    self.graduationyear = 2019

```

Multiple inheritance in Python is a feature that allows a class to inherit from more than one parent class.

```
class ChildClass(ParentClass1, ParentClass2):
    # class body
```
- __Method Resolution Order (MRO)__: Python uses a method resolution order (MRO) algorithm to determine the order in which classes are searched for a method when it’s called. The default MRO follows the C3 linearization.
- __Diamond Problem__: In some cases (especially when a class inherits from two classes that have a common ancestor), a problem known as the diamond problem arises. Python handles this problem using C3 linearization to avoid ambiguity.
- __Super() Function__: The super() function can be used to call methods from parent classes in the context of multiple inheritance.

```
class A:
    def greet(self):
        print("Hello from class A")

class B(A):
    def greet(self):
        print("Hello from class B")

class C(A):
    def greet(self):
        print("Hello from class C")

class D(B, C):
    def greet(self):
        print("Hello from class D")
        super().greet()

# Using the classes
d = D()
d.greet()

// RESULT
Hello from class D
Hello from class B
Hello from class C
Hello from class A

```

__Polymorphism__
```
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
```

__Encapsulation__ is about protecting data inside a class.

In Python, you can make properties private by using a double underscore __ prefix:
```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age) # This will cause an error 
```

__Class methods__: use @staticmethod decorator, or a class method using the @classmethod decorator.

```
class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method.")

# Call the static method without creating an instance of the class
MyClass.my_static_method()
```

A @classmethod is similar to a static method in that it is bound to the class rather than an instance of the class. However, it takes a reference to the class itself (cls) as its first argument, which allows it to access and modify class-level data.

```
class MyClass:
    class_variable = 10
    
    @classmethod
    def my_class_method(cls):
        print(f"This is a class method. Class variable: {cls.class_variable}")

# Call the class method without creating an instance of the class
MyClass.my_class_method()

```


## Python Interview questions <a id="interview"></a>

### Is Python compiled or interpreted?

it is both compiled and interpreted

Python is generally considered an interpreted language, but the most common implementation, CPython, actually uses a hybrid approach: it is both compiled and interpreted. 

When you run a Python program using the standard CPython interpreter, the following steps occur:
- Compilation to Bytecode: The Python source code (.py file) is first compiled into an intermediate, low-level, and platform-independent representation called bytecode. This compilation step happens automatically and is largely hidden from the user. The resulting bytecode is often cached in .pyc files within a __pycache__ directory to speed up subsequent executions.
- Interpretation: The generated bytecode is then executed line-by-line by the Python Virtual Machine (PVM). The PVM acts as a runtime engine, interpreting the bytecode instructions and translating them into machine code that the computer's CPU can execut

### What is PEP 8, and why is it important?

PEP 8 is the official style guide for Python code, providing a set of conventions and best practices for writing clean, readable, and consistent code.

Key PEP 8 Guidelines:
- Indentation: Use 4 spaces per indentation level, never tabs.
- Line Length: Limit all lines to a maximum of 79 characters to ensure readability, especially when viewing multiple files side-by-side.
- Naming Conventions:
  - Variables and Functions: Use snake_case (lowercase with underscores).
  - Classes: Use CamelCase (capitalized words).
  -  Constants: Use ALL_CAPS (all uppercase with underscores).
- Whitespace: Use blank lines sparingly inside functions to indicate logical steps, and two blank lines around top-level function and class definitions. Use spaces around operators (e.g., a = 1 + 2), but avoid spaces immediately inside parentheses, brackets, or braces.
- Imports: Place imports at the top of the file and organize them into three groups: standard library imports, third-party imports, and local application imports, with a blank line between each group. Use separate lines for each 

### Explain mutable vs immutable objects in Python with examples.

__Mutable objects__ can have their content altered after creation. This can lead to unexpected side effects if multiple variables reference the same object.

Examples:
- list
- dict
- set
- bytearray
- User-defined classes (by default)

__Immutable objects__ have a fixed value once created:

Examples:
- int, float, bool, complex (numeric types)
- str
- tuple
- frozenset

### Difference between == and is operator?

The primary difference is that the __== operator checks for value equality__, 
while the __is operator checks for object identity__ (whether two variables refer to the exact same object in memory).

```
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2) # Output: True (values are the same)
print(list1 is list2) # Output: False (different objects in memory)
```

### What does if __name__ == "__main__": do?

The if __name__ == "__main__" block in Python ensures that specific code runs only when the Python file is executed directly, not when it's imported as a module into another script, allowing for reusable code (functions, classes) that can also serve as standalone programs with their own logic

```
# my_module.py

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This part only runs when you execute 'python my_module.py' directly
    print("Running as the main script.")
    print(greet("World"))
    # This could be test cases or setting up a GUI
```

### Explain *args and **kwargs.

In Python, *args and **kwargs are used to allow functions to accept an arbitrary number of arguments. 

Below code shows how *args collects multiple positional arguments into a tuple and how **kwargs collects keyword arguments into a dictionary.

```
# *args example
def fun(*args):
    return sum(args)

print(fun(5, 10, 15))   

# **kwargs example
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3)

// output
30
a 1
b 2
c 3
```

### What are list comprehensions? Give an example.

List comprehensions are a concise and efficient way to create new lists in Python by iterating over an existing iterable (like a list, tuple, or range) in a single line of code

```
original_numbers = [1, 2, 3, 4, 5, 6]
squared_evens = [number ** 2 for number in original_numbers if number % 2 == 0]

print(squared_evens)
# Output: [4, 16, 36]
```

### How do you check if a key exists in a dictionary?

The most common way in Python is to use the in operator:

```
my_dict = {"apple": 1, "banana": 2, "cherry": 3}
key_to_check = "banana"

if key_to_check in my_dict:
    print(f"'{key_to_check}' exists in the dictionary.")
else:
    print(f"'{key_to_check}' does not exist.")
```

### What is the difference between append() and extend()?

append() adds its argument as a single element to the end of a list, 

```
list1 = [1, 2, 3]
list1.append([4, 5])
print(list1)
# Output: [1, 2, 3, [4, 5]]
```

extend() adds multiple elements from an iterable (like another list, tuple, or string) to the list one by one.

```
list1 = [1, 2, 3]
list1.extend([4, 5])
print(list1)
# Output: [1, 2, 3, 4, 5]
```

### How to reverse a list/string in Python

```
# 1
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)
# Output: [5, 4, 3, 2, 1]

# 2
original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]
print(reversed_list)
# Output: [5, 4, 3, 2, 1]
print(original_list)
# Output: [1, 2, 3, 4, 5]

```

### what is iterator object in python?

An iterator object must implement two methods defined in the iterator protocol:

__iter__(): This method returns the iterator object itself. It allows an object to be used as an iterable.

__next__(): This method returns the next value from the iterable. When there are no more values to return, it raises the StopIteration exception

```
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if self.current > self.end:
            raise StopIteration  # Signals that there are no more items
        self.current += 1
        return self.current - 1

# Using the iterator
my_iter = MyIterator(1, 5)

for number in my_iter:
    print(number)
```

### explain map() in python

The map() function in Python is a built-in function that applies a given function to all items in an iterable (like a list, tuple, or string) and returns a map object, which is an iterator.

```
map(function, iterable, ...)
```

- function: This is the function that will be applied to each element in the iterable. It can be a built-in function, a lambda function, or any user-defined function.
- iterable: This is one or more iterables (like a list, tuple, etc.). If more than one iterable is passed, the function must take as many arguments as there are iterables.
- The result is a map object, which is an iterator. You can convert it to a list, tuple, or other types to see the output.

```
numbers = [1, 2, 3, 4, 5]

# Use a lambda function to square each number
squared_numbers = map(lambda x: x * x, numbers)

# Convert to a list and print
print(list(squared_numbers))
```

If you provide multiple iterables to map(), the function will receive one element from each iterable at a time, and the function should be able to handle multiple arguments. For example, let’s add corresponding elements from two lists:

```
numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7, 8]

# Add corresponding elements from two lists
result = map(lambda x, y: x + y, numbers1, numbers2)

# Convert to list and print
print(list(result))

// Result
[6, 8, 10, 12]
```



### Explain slicing in Python with negative indices.

### What are Python decorators and how do they work?

### Explain generators and yield keyword.

### What is a lambda function? When to use it?




## Python data engineering python interview questions

### Difference between list and tuple?

Lists are mutable; tuples are immutable and faster for read-only operations.

### What are Python generators?

Generators produce values lazily using yield, saving memory for large datasets.

### What is a Python iterator?

An object implementing __iter__() and __next__() to traverse elements.

```
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 5:
      x = self.a
      self.a += 1
      return x
    else:
      # Stop the iteration by raising StopIteration
      raise StopIteration

# Create an instance of the custom iterator class
my_class_instance = MyNumbers()

# Get the iterator object
my_iter = iter(my_class_instance)

# Iterate using a for loop (implicitly uses iter() and next())
for num in my_iter:
  print(num)
```

### What is list comprehension?

A concise way to create lists:
```
[x*x for x in range(5)]
```

### What is a dictionary and why is it fast?

Key-value data structure using hashing → O(1) average lookup.

### Explain shallow vs deep copy.

Shallow copies references; deep copies duplicate objects fully.

### What are Python decorators?

Functions that modify other functions’ behavior without changing code.

```
def uppercase_decorator(func):
    """Decorator to convert a function's return value to uppercase."""
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    """Decorator to add exclamation marks before and after a function's return value."""
    def wrapper():
        result = func()
        return f"!!! {result} !!!"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def greet():
    """Original function that returns a simple greeting."""
    return "Hello, World"

# Call the decorated function
print(greet())
```

Result:
```
!!! HELLO, WORLD !!!
```

### What is __init__?

Constructor method called when an object is created.

### What is *args and **kwargs?

Variable-length positional and keyword arguments.

### Difference between is and ==?

is checks identity; == checks value equality.

```
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(f"list_a == list_b: {list_a == list_b}")
print(f"list_a is list_b: {list_a is list_b}")
print(f"list_a is list_c: {list_a is list_c}")

// RESULT
list_a == list_b: True
list_a is list_b: False
list_a is list_c: True
```

### What is None?

Represents absence of a value.

### What is slicing?

Extracting subsets from sequences: arr[1:5].

### What are Python modules?

Files containing Python code that can be imported.

### What is lambda function?

Anonymous one-line function: lambda x: x+1.

### Difference between append() and extend()?

append adds one item; extend adds multiple items.

### Time complexity of dictionary lookup?

O(1) average case.

### When would you use a set?

For fast membership testing and uniqueness.

### What is a heap?

Tree-based structure used in priority queues.

```
import heapq

# 1. Create a heap from an existing list using heapify()
# The function rearranges the list in-place to satisfy the heap property
my_list = [21, 1, 45, 78, 3, 5]
heapq.heapify(my_list)
print(f"Heapified list: {my_list}")
# Output: [1, 3, 5, 78, 21, 45] (order of non-root elements may vary)
```

### What is a deque?

Double-ended queue optimized for fast appends/pops.

```
from collections import deque

# 1. Create a deque
numbers = deque([1, 2, 3, 4, 5])
print(f"Initial deque: {numbers}")

# 2. Add elements
numbers.append(6)         # Add to the right end
numbers.appendleft(0)     # Add to the left end
print(f"After adding elements: {numbers}")

# 3. Access elements (like a list)
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
```

### What is Big-O notation?

Measures algorithm efficiency.

### Explain map, filter, reduce.

Functional programming tools for transformation.

The __map__() function applies a given function to every item in an iterable and returns a map object (which can be converted to a list). It transforms the elements

```
# Function to apply
def square(n):
    return n * n

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using map()
# The result is a map object, convert to a list to see the values
squared_numbers = list(map(square, numbers))

# Output: [1, 4, 9, 16, 25]
print(squared_numbers)

# Using lambda (more compact)
squared_numbers_lambda = list(map(lambda n: n * n, numbers))
print(squared_numbers_lambda)
```

The __filter__() function tests each element in an iterable against a function that returns either True or False. It returns a filter object (convertible to a list) containing only the elements for which the function returned True. It selects a subset of elements

```
# Function to apply the condition
def is_even(n):
    return n % 2 == 0 # Returns True if even, False if odd

# List of numbers
numbers = [1, 2, 3, 4, 5, 6]

# Using filter()
# The result is a filter object, convert to a list to see the values
even_numbers = list(filter(is_even, numbers))

# Output: [2, 4, 6]
print(even_numbers)

# Using lambda (more compact)
even_numbers_lambda = list(filter(lambda n: n % 2 == 0, numbers))
print(even_numbers_lambda)
```

The __reduce__() function applies a rolling computation to sequential pairs of values in an iterable, reducing the iterable to a single cumulative value

```
# Python 3
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)
```

### How do you remove duplicates from a list?

Convert to set.

### Difference between Series and DataFrame in Pandas?

Series: 1D; DataFrame: 2D.

### How do you handle missing values in Pandas?

fillna(), dropna().

### Difference between loc and iloc in Pandas

loc is label-based, while iloc is integer-position-based. This means you use explicit row/column names with loc and numerical positions (starting from 0) with iloc

```
import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data, index=['row1', 'row2', 'row3'])

# Select row 'row2' and column 'B'
print(df.loc['row2', 'B']) # Output: 5

# Select the second row (position 1) and third column (position 1 for column 'B')
print(df.iloc[1, 1]) # Output: 5

```

### What is broadcasting in NumPy?

Applying operations between arrays of different shapes.

In this example, a 1D array is added to each row of a 2D array because the trailing dimensions are compatible (the 1D array's length matches the number of columns in the 2D array:

```
import numpy as np

a_2d = np.array([
    [0.0, 0.0, 0.0],
    [10.0, 10.0, 10.0],
    [20.0, 20.0, 20.0],
    [30.0, 30.0, 30.0]
])

b_1d = np.array([1.0, 2.0, 3.0])

result = a_2d + b_1d

print(f"Shape of a_2d: {a_2d.shape}")
print(f"Shape of b_1d: {b_1d.shape}")
print(f"Resulting array:\n{result}")
# Output:
# Shape of a_2d: (4, 3)
# Shape of b_1d: (3,)
# Resulting array:
# [[ 1.  2.  3.]
#  [11. 12. 13.]
#  [21. 22. 23.]
#  [31. 32. 33.]]
```

### Difference between apply and map?

map: Series only; apply: DataFrame/Series.

```
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

# Define a function that takes a row (as a Series) as input
def assign_status(row):
    if row['Age'] > 28:
        return 'Experienced'
    else:
        return 'Junior'

# Apply the function along the rows (axis=1)
df['Status'] = df.apply(assign_status, axis=1)
print("\nDataFrame after apply():")
print(df)
# Output:
#       Name  Age       Role       Status
# 0    Alice   25    Manager       Junior
# 1      Bob   30   Employee  Experienced
# 2  Charlie   35   Employee  Experienced
```

### How do you read large CSV files efficiently?

Use chunksize.

the chunksize parameter is commonly used with the pandas library to process large files (like CSVs) in smaller, memory-efficient chunks

```
import pandas as pd

# Define the number of rows per chunk
chunk_size = 100000 
file_path = 'large_dataset.csv'

# Create an empty list to store processed chunks (optional, if you need to combine later)
chunks = []

# Iterate over the file in chunks
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    # Perform operations on each chunk (e.g., filtering, aggregation)
    # Here, we're just appending for demonstration purposes
    chunks.append(chunk) 
    print(f"Processed a chunk of size: {len(chunk)} rows")

# If needed, concatenate all chunks into a single DataFrame (only if it fits in memory)
# full_df = pd.concat(chunks) 
```

### What is pivot table?

Summarizes data with aggregation.

```
import pandas as pd
import numpy as np

# 1. Create a sample DataFrame
data = {
    'Region': ['East', 'East', 'West', 'West', 'East', 'West'],
    'Product': ['Laptop', 'Phone', 'Laptop', 'Phone', 'Laptop', 'Laptop'],
    'Quantity': [10, 15, 5, 20, 12, 8],
    'Price': [1000, 500, 1000, 500, 1000, 1000]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("-" * 30)

# 2. Create the pivot table
pivot_df = df.pivot_table(
    values='Quantity',      # Column to aggregate
    index='Region',         # Row labels
    columns='Product',      # Column labels
    aggfunc=np.sum,         # Aggregation function (sum the quantities)
    fill_value=0            # Replace missing values (NaN) with 0
)

print("Pivot Table:")
print(pivot_df)

// RESULT
Original DataFrame:
  Region Product  Quantity  Price
0   East  Laptop        10   1000
1   East   Phone        15    500
2   West  Laptop         5   1000
3   West   Phone        20    500
4   East  Laptop        12   1000
5   West  Laptop         8   1000
------------------------------
Pivot Table:
Product  Laptop  Phone
Region                
East         22     15
West         13     20
```

### How do you optimize Pandas performance?

Use vectorization, categorical types.

### What is partitioning?

Splitting data for parallel processing.

### What is shuffling?

Redistribution of data across nodes.

### What is checkpointing?

Saving state for fault tolerance.

### What is window function?

Operates over a defined range of rows.

### compare pandas DataFrame to spark DataFrame

Pandas DataFrame:
- Part of the Pandas library, which is built on top of NumPy.
- Primarily designed for single-node, in-memory data manipulation and analysis.
- Commonly used in smaller-scale, local data analysis and processing tasks.

Spark DataFrame:
- Part of the Apache Spark ecosystem, which is designed for distributed computing.
- Built on top of Spark SQL and Catalyst optimizer, making it highly optimized for large-scale data processing.
- Primarily used for big data processing, typically in a cluster environment (distributed across multiple nodes).

| Feature              | **Pandas DataFrame**                              | **Spark DataFrame**                                               |
| -------------------- | ------------------------------------------------- | ----------------------------------------------------------------- |
| **Primary Use Case** | Small to medium data analysis on a single machine | Large-scale distributed data processing                           |
| **Processing Model** | In-memory, single-node                            | Distributed, cluster-based, lazy execution                        |
| **Scalability**      | Limited to system memory                          | Scales horizontally across multiple machines                      |
| **Performance**      | Fast for small datasets in memory                 | Optimized for big data, high performance in distributed computing |
| **Ease of Use**      | Simple, intuitive Pythonic API                    | More complex, especially for distributed setups                   |
| **Fault Tolerance**  | No built-in fault tolerance                       | Built-in fault tolerance with RDD lineage                         |
| **Memory & Storage** | In-memory only                                    | Memory and disk-based, distributed storage                        |
| **Integration**      | Python data science ecosystem                     | Spark ecosystem, big data tools, cloud services                   |





