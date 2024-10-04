import pandas as pd

df = pd.read_excel('test.xlsx')

data = df.dropna()
print(df)


