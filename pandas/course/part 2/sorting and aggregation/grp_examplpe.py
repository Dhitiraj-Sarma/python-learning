import pandas as pd

data = {
	"Name": ['Arun', 'Ram', 'Sita', 'Gita'],
	"Age" : [10, 20, 20, 40],
	"Salary" : [10000, 20000, 15000, 15550]
}

df = pd.DataFrame(data)
print(df)
# grouped = df.groupby("Age")["Salary"].sum()
# print(grouped)

grouped = df.groupby(["Age", "Name"])["Salary"].sum()
print(grouped)