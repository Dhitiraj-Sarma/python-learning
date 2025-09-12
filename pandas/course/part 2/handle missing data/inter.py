import pandas as pd

data = {
	"Name" : ['Ram', None, 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
	"Age" : [10, None , 30, 40, 50,60, 70, 80],
	"Salary" : [10000, None, 30000, 40000, 50000, 60000, 70000, 80000],
	"Performance Score" : [85, None, 75, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)
print(df)

# linear, polynomial, time

df.interpolate(method="linear", axis=0, inplace=True)
print(df)

data1={
	"TIme": [1, 2, 3, 4, 5],
	"Value": [10, None, 30, None, 50]
}

df1= pd.DataFrame(data1)
print('Before Interpolation')
print(df1)

df1['Value'] = df1['Value'].interpolate(method="linear")
print('After interpolation')
print(df1)

"""
time series data
numeric data with trends
avoid dropping rows
"""