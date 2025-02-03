import pandas as pd

data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "No", "Yes", "No", "No"],
    "Marital Status": ["Single", "Married", "Single", "Married", "Divorced", "Married", "Divorced", "Single", "Married", "Single"],
    "Taxable Income": ["125K", "100K", "70K", "120K", "95K", "60K", "220K", "85K", "75K", "90K"],
    "Cheat": ["No", "No", "No", "No", "No", "No", "No", "Yes", "Yes", "No"]
}
df=pd.DataFrame(data)
print("row 0-",df.loc[0],"\n")
print("row 4-",df.loc[4],"\n")
print("row 7-",df.loc[7],"\n")
print("row 8-",df.loc[8])