import pandas as pd
import matplotlib.pyplot as plt

# 1 pandas Data Structures

# 1.1 Series data
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
city = pd.Series(['Pathsala', 'Tihu', 'Nalbari'], index=['a', 'b', 'c'])

print(city["c"])

# 1.2 DataFrame – table

data = {'Name': ['Ana','Ben'], 'Score': [89, 95]}
df = pd.DataFrame(data)

print(df)

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Delhi', 'Mumbai', 'Kolkata']
}

df = pd.DataFrame(data)
print(df)


data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'Delhi'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Mumbai'}
]

df = pd.DataFrame(data)
print(df)


data = [
    ['Alice', 25, 'Delhi'],
    ['Bob', 30, 'Mumbai']
]

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
df[df['Age'] > 28]
print(df)