import pandas as pd

# Load the CSV file
file_path = 'Ball_By_Ball_Match_Data_merge_2024.csv'
df = pd.read_csv(file_path)

# Create 'BowlingTeam' based on the condition
df['BowlingTeam'] = df.apply(lambda row: row['team2'] if row['BattingTeam'] == row['team1'] else row['team1'], axis=1)

# Aggregating the batting summary with additional columns
batting_summary = df.groupby(['Match_ID', 'team1', 'team2', 'BattingTeam', 'Batter']).agg(
    runs=pd.NamedAgg(column='BatsmanRun', aggfunc='sum'),
    balls_faced=pd.NamedAgg(column='BallNumber', aggfunc='count'),
    fours=pd.NamedAgg(column='BatsmanRun', aggfunc=lambda x: (x == 4).sum()),
    sixes=pd.NamedAgg(column='BatsmanRun', aggfunc=lambda x: (x == 6).sum())
).reset_index()

batting_summary['strike_rate'] = batting_summary['runs'] / batting_summary['balls_faced'] * 100

# Aggregating the bowling summary with additional columns
bowling_summary = df.groupby(['Match_ID', 'BattingTeam', 'team1', 'team2', 'BowlingTeam', 'Bowler']).agg(
    balls_bowled=pd.NamedAgg(column='BallNumber', aggfunc='count'),
    runs_conceded=pd.NamedAgg(column='TotalRun', aggfunc='sum'),
    wickets=pd.NamedAgg(column='IsWicketDelivery', aggfunc='sum')
).reset_index()

# Calculate overs, economy rate, and maiden overs
bowling_summary['overs'] = bowling_summary['balls_bowled'] // 6
bowling_summary['economy_rate'] = bowling_summary['runs_conceded'] / bowling_summary['overs']

# Calculate maiden overs (overs where no runs were conceded)
bowling_summary['maiden_overs'] = bowling_summary['overs'] - (bowling_summary['runs_conceded'] // 6)

# Save the summaries to CSV files
batting_summary_path = 'batting_summary_with_teams.csv'
bowling_summary_path = 'bowling_summary_with_teams.csv'
batting_summary.to_csv(batting_summary_path, index=False)
bowling_summary.to_csv(bowling_summary_path, index=False)

batting_summary_path, bowling_summary_path
