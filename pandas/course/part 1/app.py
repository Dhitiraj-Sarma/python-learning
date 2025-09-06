import pandas as pd

# read data from CSV file into a dataframe
df = pd.read_csv("sales.csv")
# df= pd.read_excel("sales.xlsx")
# df=pd.read_json("sales.json")
print(df)