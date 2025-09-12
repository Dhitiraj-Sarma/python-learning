import pandas as pd

# Vertical Concatenation (Row-wise)

df1 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']})
df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']})

result = pd.concat([df1, df2], axis=0, ignore_index=True)
print(result)


# Horizontal Concatenation (Column-wise)

df1 = pd.DataFrame({'A': ['A0', 'A1']})
df2 = pd.DataFrame({'B': ['B0', 'B1']})

result = pd.concat([df1, df2], axis=1)
print(result)
