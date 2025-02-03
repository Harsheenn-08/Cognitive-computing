import pandas as pd

data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "No", "Yes", "No", "No"],
    "Marital Status": ["Single", "Married", "Single", "Married", "Divorced", "Married", "Divorced", "Single", "Married", "Single"],
    "Taxable Income": ["125K", "100K", "70K", "120K", "95K", "60K", "220K", "85K", "75K", "90K"],
    "Cheat": ["No", "No", "No", "No", "No", "No", "No", "Yes", "Yes", "No"]
}
df=pd.DataFrame(data)
print("\nRows from index 3 to 7:")
print(df.loc[3:7])

print("\nRows from index 4 to 8 and columns 2 to 4:")
print(df.iloc[4:9, 2:5])

print("\nAll rows with column index 1 to 3:")
print(df.iloc[:, 1:4])