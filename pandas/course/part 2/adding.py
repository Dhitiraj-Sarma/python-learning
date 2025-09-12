import pandas as pd

data = {
	"Name" : ['Ram', 'Shayam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
	"Age" : [10, 20 , 30, 40, 50,60, 70, 80],
	"Salary" : [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000],
	"Performance Score" : [85, 90, 75, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)
print(df)

# adding column df["column_name"] = some_data

df["Bonus"] = df['Salary'] * 0.1
print(df)

# using insert()
# df.insert(loc, "Column_name", some_data)

df.insert(0, "Employee ID", [1, 2, 3, 4, 5, 6, 7, 8])
print(df)