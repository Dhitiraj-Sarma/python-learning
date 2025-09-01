import pandas as pd

data = {
	"Name" : ['Ram', 'Shayam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
	"Age" : [10, 20 , 30, 40, 50,60, 70, 80],
	"Salary" : [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000],
	"Performance Score" : [85, 90, 75, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

# print('Descriptive Staristics')
# print(df.describe())


"""
1- how big is your dataset
2- what are the names of colums

shape and columns
"""

# print(f'Shape: {df.shape}')
# print(f'Column Names: {df.columns}')

"""
- select specific column
- filter rows
- combine multiple conditions

-square brackets
boolean conditions

selecting columsn
- a series
- dataframe multiple columns of data

column = df[["C1", "C2", .....]]

filtering rows
boolean indexing

based on a single condition
filtered_rows = df[df["salary"] > 50000]

combine multiple conditions
filtered-rows = df[(df["salary]> 50000) & (df[salary] < 80000)]
"""

# select single column
print("Name (Single column return series)")

print(df["Name"])
# select multiple columns
subset = df[["Name", "Salary"]]
print('\nSubset with Name and Salary')
print(subset)