# Import pandas package
import pandas as pd
 
# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# Convert the dictionary into DataFrame 
print( "\n---- Convert the dictionary into DataFrame")
df = pd.DataFrame(data)
print(df)

# select two columns
print( "\n---- select two columns")
print(df[['Name', 'Qualification']])

# read data from file and select a data item
print( "\n---- read data from file and select a data item")
data = pd.read_csv("/home/kj/Krzys/git/computer-science-basics-tutorials/Data_Science/nba.csv", index_col ="Name")
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
print(first, "\n\n", second)
