# Pandas

Pandas allows us to analyze big data and make conclusions based on statistical theories.

Pandas can clean messy data sets, and make them readable and relevant.

## Basics

### Series

A Pandas Series is like a column in a table.

```
import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a)

print(myvar)
```

You can also use a key/value object, like a dictionary, when creating a Series.

```
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)

print(myvar)
```

### Labels

If nothing else is specified, the values are labeled with their index number.
This label can be used to access a specified value.

```
import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
print(myvar["y"])
```

### DataFrames

Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.

A standard pandas DataFrame is __inherently a two-dimensional__ data structure.

```
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)

print(myvar)
```

Pandas use the loc attribute to return one or more specified row(s)

```
// Return row 0:
print(df.loc[0])

// Return row 0 and 1:
print(df.loc[[0, 1]])
```

## Loading Data

Load a comma separated file (CSV file) into a DataFrame:

```
import pandas as pd

df = pd.read_csv('data.csv')

// If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
print(df) 

// or use to_string() to print the entire DataFrame.
print(df.to_string()) 

// Increase the maximum number of rows to display the entire DataFrame:
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
```

Load the JSON file into a DataFrame:

```
import pandas as pd

df = pd.read_json('data.json')

print(df)
```

Load a Python Dictionary into a DataFrame:

```
import pandas as pd

data = {
  "Duration":{
    "0":60,
    "5":60
  },
  "Pulse":{
    "0":110,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "5":127
  },
  "Calories":{
    "0":409,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 
```

## Analyzing DataFrames

### head and tail

The head() method returns the headers and a specified number of rows, starting from the top.

```
import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))
```

Print the last 5 rows of the DataFrame:

```
print(df.tail())
```

Print information about the data:

```
print(df.info()) 
```

### Cleaning data

Data cleaning means fixing bad data in your data set.

Bad data could be:
- Empty cells
- Data in wrong format
- Wrong data
- Duplicates

Return a new Data Frame with __no empty cells__:

```
import pandas as pd

df = pd.read_csv('data.csv')
new_df = df.dropna()

// If you want to change the original DataFrame, use the inplace = True argument:
df.dropna(inplace = True)

print(new_df.to_string())
```

By default, the dropna() method returns a new DataFrame, and will not change the original.
If you want to change the original DataFrame, use the inplace = True argument:

__Replace Empty Values__

Another way of dealing with empty cells is to insert a new value instead.
The fillna() method allows us to replace empty cells with a value:

```
import pandas as pd

df = pd.read_csv('data.csv')

// Replace NULL values with the number 130:
df.fillna(130, inplace = True) 

// Replace Only For Specified Columns
df.fillna({"Calories": 130}, inplace=True) 
```

### Mean, Median, or Mode

- Mean = the average value (the sum of all values divided by number of values).
- Median = the value in the middle, after you have sorted all values ascending.
- Mode = the value that appears most frequently.

```
import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mean()
x = df["Calories"].median()
x = df["Calories"].mode()

df.fillna({"Calories": x}, inplace=True)
```

### Cleaning Data of Wrong Format

Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

Convert all cells in the 'Date' column into dates:

```
import pandas as pd

df = pd.read_csv('data.csv')

// Convert all cells in the 'Date' column into dates:
df['Date'] = pd.to_datetime(df['Date'], format='mixed')

// Remove rows with a NULL value in the "Date" column:
df.dropna(subset=['Date'], inplace = True)

print(df.to_string())
```

Replacing Values

```
// Loop through all values in the "Duration" column. If the value is higher than 120, set it to 120:
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
```

Delete rows where "Duration" is higher than 120:

```
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True) 
```

### Removing Duplicates

```
// The duplicated() method returns a Boolean values for each row:
print(df.duplicated())

// Remove all duplicates:
df.drop_duplicates(inplace = True) 
```

### Data Correlations

A great aspect of the Pandas module is the corr() method.
The corr() method calculates the relationship between each column in your data set.

```
df.corr() 
```

Result:

```
          Duration     Pulse  Maxpulse  Calories
  Duration  1.000000 -0.155408  0.009403  0.922721
  Pulse    -0.155408  1.000000  0.786535  0.025120
  Maxpulse  0.009403  0.786535  1.000000  0.203814
  Calories  0.922721  0.025120  0.203814  1.000000
```

### Plotting

Pandas uses the plot() method to create diagrams.
We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.

```
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show() 
```

