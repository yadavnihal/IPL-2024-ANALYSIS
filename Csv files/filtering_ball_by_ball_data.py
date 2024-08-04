import pandas as pd

# Load the two CSV files into pandas DataFrames
df1 = pd.read_csv("Ball_By_Ball_Match_Data.csv")
df2 = pd.read_csv('Match_info.csv')

# Filter the first DataFrame to keep only the rows with 'id' values present in the second DataFrame
filtered_df = df1[df1["Match_ID"].isin(df2["Match_ID"])]

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv('Ball_By_Ball_Match_Data_2024.csv', index=False)
