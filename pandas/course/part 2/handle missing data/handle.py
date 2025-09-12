import pandas as pd

data = {
	"Name" : ['Ram', None, 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
	"Age" : [10, None , 30, 40, 50,60, 70, 80],
	"Salary" : [10000, None, 30000, 40000, 50000, 60000, 70000, 80000],
	"Performance Score" : [85, None, 75, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)
print(df)

#dropna()
df.dropna(inplace=True)
print(df)