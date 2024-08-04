import pandas as pd

# Load the two CSV files into pandas DataFrames
df1 = pd.read_csv("Ball_By_Ball_Match_Data_2024.csv")
df2 = pd.read_csv('Match_info.csv')

df2_selected=df2[["Match_ID","team1","team2"]]

merged_data=pd.merge(df1,df2_selected,on="Match_ID",how="inner")


# Save the filtered DataFrame to a new CSV file
merged_data.to_csv('Ball_By_Ball_Match_Data_merge_2024.csv', index=False)
