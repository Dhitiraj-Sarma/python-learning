import pandas as pd

data = {
	"Name" : ['Ram', 'Shayam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
	"Age" : [10, 20 , 30, 40, 50,60, 70, 80],
	"Salary" : [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000],
	"Performance Score" : [85, 90, 75, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)
print(df)

# .loc[]
# df.loc[row_index, "column_name"] = new_value

df.loc[0, 'Salary'] = 55000
print(df)

# increasing salary by 10%
df['Salary'] = df['Salary']*0.1
print(df)