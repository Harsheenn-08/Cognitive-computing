import pandas as pd

csv_path = "iris.csv"
iris_df = pd.read_csv(csv_path)

iris_df = iris_df.drop(index=3)  
iris_df = iris_df.drop(columns=iris_df.columns[2]) 

print("\nData after deleting row 4 and column 3:")
print(iris_df)
