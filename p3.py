import pandas as pd
data = {
    "Name": ["mithun", "mohith"],
    "Age": [40,20]
}
df = pd.DataFrame(data)
print(df)
print("\n")
print(df.loc[0])
