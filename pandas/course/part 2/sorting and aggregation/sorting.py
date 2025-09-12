# sorting data

# sorting data 1 column

import pandas as pd

data = {
	"Name": ['Arun', 'Ram', 'Sita', 'Gita'],
	"Age" : [10, 20, 23, 40],
	"Salary" : [1000, 2000, 1500, 1555]
}

df = pd.DataFrame(data)

print(df)

df.sort_values(by="Age", ascending=True, inplace=True)
print(df)

df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)
print(df)