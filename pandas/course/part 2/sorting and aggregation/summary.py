"""
df["column name"].mean()
df["column name"].sum()
df["column name"].min()
df["column name"].max()
"""

import pandas as pd

data = {
	"Name": ['Arun', 'Ram', 'Sita', 'Gita'],
	"Age" : [10, 20, 23, 40],
	"Salary" : [1000, 2000, 1500, 1555]
}

df = pd.DataFrame(data)

avg_salary = df['Salary'].mean()
print(avg_salary)