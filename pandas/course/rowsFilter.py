import pandas as pd

data = {
	"Name" : ['Ram', 'Shayam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
	"Age" : [10, 20 , 30, 40, 50,60, 70, 80],
	"Salary" : [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000],
	"Performance Score" : [85, 90, 75, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

high_salary = df[df['Salary'] > 50000]
print('Employees with salary > 50000')
print(high_salary)

# filtering rows salary > 50k & age > 30
filtered = df[(df["Age"] > 70) & (df['Salary'] > 50000)]
print(filtered)

#using OR condition
filtered_or = df[(df['Age'] > 50) | (df['Performance Score']> 90)]
print(filtered_or)