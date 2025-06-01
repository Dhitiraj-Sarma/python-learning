# Importing necessary libraries

import pandas as pd
import numpy as np

# loading the dataset
df = pd.read_csv('C:/Users/USER/Desktop/python/numpy/indian employ/employee_data_unrealistic.csv')

# Displaying the first few rows of the dataset

print("Initial DataFrame:")
print(df.head())


# chekcing the missing values
print('Missing values in reach column of the dataset: ')
print(df.isnull().sum())

df['Salary'].fillna(df['Salary'].mean(), inplace=True)

df['PerformanceRating'].fillna(df['PerformanceRating'].median(), inplace=True)

df.replace([np.inf, -np.inf], np.nan, inplace=True)

df.fillna(df.select_dtypes(include=np.number).mean(), inplace=True)

# Remove duplicate records
df.drop_duplicates(inplace=True)

# replace negative salaries
df['Salary'] = np.where(df['Salary'] < 0, df['Salary'].mean(), df['Salary'])

# handle unrealisting salary

salary_mean = df['Salary'].mean()
salary_std = df['Salary'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)


#  remove rows where salary istoo high or too low

df = df[(df['Salary'] >= lower_bound) & (df['Salary'] <= upper_bound)]

df.to_csv('cleaned_indian_employee_data.csv', index=False)
print('Data cleaning completed! Saved as cleaned_indian_employee_data.csv')