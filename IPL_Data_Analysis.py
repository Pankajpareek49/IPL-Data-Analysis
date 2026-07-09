#IPL Data Analysis Project

import numpy as np
import pandas as pd

match = pd.read_csv("matches.csv")
dvr = pd.read_csv("deliveries.csv")

#Basic Analysis of both files
match.head()
match.tail()
match.info()
match.shape
print(match)
print(match.describe())
print(match.columns)
print("Match basic Analysis completed ")

dvr.head()
dvr.tail()
dvr.shape
dvr.info()
print(dvr)
print(dvr.describe())
print(dvr.columns)
print("Deliveries basic analysis done")

#Find Missing values 
print(match.isnull())
print(match.isnull().sum())

print(dvr.isnull())
print(dvr.isnull().sum())

#Find Duplicate Values
print(match.duplicated())
print(match.duplicated().sum())

print(dvr.duplicated())
print(dvr.duplicated().sum())

#drop duplicated columns that are not used
match.drop(['umpire3'], axis=1, inplace=True)
print(match)

#find duplicated rows
print(match.duplicated().sum())

#convert date dtype into datetime
match['date'] = pd.to_datetime(
    match['date'],
    format='mixed',
    dayfirst=True
)
print(match.info())

#EDA 

total_seasons = match['season'].nunique()
print("Total IPLs Seasons: ", total_seasons)

#total matches 
total_matches = match['id'].nunique()
print("Total matches are: ", total_matches)

#season list
season_list = match['season'].unique()
print("List of all seasons: ", season_list)

#Total Teams
total_teams = pd.concat([match['team1'], match['team2']])
print(total_teams)
#remove duplicate teams

total_teams.drop_duplicates(inplace=True)
print(total_teams)
print(total_teams.count())

#team wise match played
team_match = pd.concat([match['team1'], match['team2']]).value_counts()
print(team_match)

#Season wise match
season_match = match['season'].value_counts()
print(season_match)

#Graph Creation
import matplotlib.pyplot as plt 

plt.figure(figsize=(8,5))

plt.bar(season_match.index, season_match.values)
plt.title("Matches Per Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.savefig("graphs/matches_per_season.png", dpi=300, bbox_inches="tight")
plt.show()

#most successful team
win_match = match['winner'].value_counts()
print(win_match)

#graph of this
plt.figure(figsize=(14,7))
plt.title("Most Win By An Team")
plt.bar(win_match.index, win_match.values)
plt.xlabel("Team Name")
plt.ylabel("Number Of Wins")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/Team_wins.png", dpi=300, bbox_inches="tight")

plt.show()

#toss winner analysis
toss_win = match['toss_winner'].value_counts()
print(toss_win)

venue = match['venue'].value_counts()
print(venue)

city = match['city'].value_counts()
print(city)

win_by_runs = match['win_by_runs'].max()
print(win_by_runs)

win_by_wkt = match['win_by_wickets'].max()
print(win_by_wkt)

plr_of_mtch = match['player_of_match'].value_counts().head(5)
print(plr_of_mtch)

#graph of top 5 player of match
plt.figure(figsize=(8,5))
plt.title("Top 5 Player of the match")
plt.bar(plr_of_mtch.index, plr_of_mtch.values)
plt.xlabel("Name Of Players")
plt.ylabel("Number of times")
plt.savefig("graphs/player_of_match.png", dpi=300, bbox_inches='tight')
plt.show()

#Match File's Data Analysis Completed

#Deliveries File's Data Analysis Started Here

top_runner = dvr.groupby('batsman')['batsman_runs'].sum()
print(top_runner)

sort_top = top_runner.sort_values(ascending=False).head()
print(sort_top)

#graph
plt.figure(figsize=(8,5))
plt.title("Top Scorer Batsman")
plt.bar(sort_top.index, sort_top.values)
plt.xlabel("Batsman Name")
plt.ylabel("Scored Runs")
plt.savefig("graphs/Top5_batsman.png", dpi=300, bbox_inches='tight')
plt.show()

#top wicket tacker
top_wkt = dvr.groupby('bowler')['dismissal_kind'].count()
print(top_wkt)

sort_wkt = top_wkt.sort_values(ascending=False).head(5)
print(sort_wkt)

#Graph 

plt.figure(figsize=(8,5))
plt.title("Top Wicket Taker Bowlers")
plt.bar(sort_wkt.index, sort_wkt.values)
plt.xlabel("Name of Bowlers")
plt.ylabel("Number of Wickets")
plt.savefig("graphs/top_wkt_tkr.png", dpi=300, bbox_inches='tight')
plt.show()

#most sixers 
sixes = dvr[dvr['batsman_runs'] == 6]
most_six = sixes.groupby('batsman')['batsman_runs'].count()
print(most_six)
sort_most_six = most_six.sort_values(ascending=False).head(5)
print(sort_most_six)

#Graph
plt.figure(figsize=(8,5))
plt.title("Most Sixes By Top 5 Batsmans")
plt.bar(sort_most_six.index, sort_most_six.values)
plt.xlabel("Name Of Batsmans")
plt.ylabel("Number of Sixes")
plt.savefig("graphs/Most_sixes.png", dpi=300, bbox_inches='tight')
plt.show()

#most dot balls
dots = dvr[dvr['total_runs'] == 6]
most_dot = dots.groupby('bowler')['total_runs'].count()
print(most_dot)
sort_most_dot = most_dot.sort_values(ascending=False).head(10)
print(sort_most_dot)

#Graph
plt.figure(figsize=(13,6))
plt.title("Top 10 Dot Delivery Bowlers")
plt.bar(sort_most_dot.index, sort_most_dot.values)
plt.xlabel("Name Of Bowlers")
plt.ylabel("Number Of Dots")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/most_dot_balls.png", dpi=300, bbox_inches='tight')
plt.show()

#Most Extra runs
most_extra = dvr.groupby('bowler')['extra_runs'].sum()
print(most_extra)
sort_most_extra = most_extra.sort_values(ascending=False).head(5)
print(sort_most_extra)

#Highest Team Score
high_run = dvr.groupby(['match_id', 'batting_team'])['total_runs'].sum()
print(high_run)
sort_high_run = high_run.sort_values(ascending=False).head(7)
print(sort_high_run)

#Graph
plt.figure(figsize=(10,6))
plt.title("Highscore Runs by a team")
labels = [f"{team} ({match_id})" for match_id, team in sort_high_run.index]
plt.bar(labels, sort_high_run.values)
plt.xlabel("Team Name")
plt.ylabel("Scored Runs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/high_score.png", dpi=300, bbox_inches='tight')
plt.show()

