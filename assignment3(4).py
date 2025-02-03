import pandas as pd
csv_path="iris.csv"
iris_df = pd.read_csv(csv_path)
print("\nFirst five rows of the CSV file:")
print(iris_df.head())