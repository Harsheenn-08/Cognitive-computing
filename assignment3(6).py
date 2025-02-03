import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}

df = pd.DataFrame(data)

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

print("\n(a) Shape of the DataFrame:", df.shape)

print("\n(b) Summary of the DataFrame:")
print(df.info())

print("\n(c) Descriptive Statistics:")
print(df.describe())

print("\n(d) First 5 rows:")
print(df.head())
print("\nLast 3 rows:")
print(df.tail(3))

print("\n(e) Calculated Statistics:")
print("i. Average Salary:", df["Salary"].mean())
print("ii. Total Bonus Paid:", df["Bonus"].sum())
print("iii. Youngest Employee's Age:", df["Age"].min())
print("iv. Highest Performance Rating:", df["Rating"].max())

df_sorted = df.sort_values(by="Salary", ascending=False)
print("\n(f) Data sorted by Salary (Descending):")
print(df_sorted)

def categorize_performance(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    else:
        return "Average"

df["Performance_Category"] = df["Rating"].apply(categorize_performance)
print("\n(g) Performance Categories:")
print(df[["Name", "Rating", "Performance_Category"]])

print("\n(h) Missing Values in the DataFrame:")
print(df.isnull().sum())

df.rename(columns={"Employee_ID": "ID"}, inplace=True)
print("\n(i) Renamed Column:")
print(df.head())

exp_filtered = df[df["Years_of_Experience"] > 5]
print("\n(j.i) Employees with more than 5 years of experience:")
print(exp_filtered)

it_department = df[df["Department"] == "IT"]
print("\n(j.ii) Employees in IT Department:")
print(it_department)

df["Tax"] = df["Salary"] * 0.10
print("\n(k) Data with Tax Deduction:")
print(df[["Name", "Salary", "Tax"]])

df.to_csv("modified_employees.csv", index=False)
print("\n(l) The modified DataFrame has been saved as 'modified_employees.csv'.")
