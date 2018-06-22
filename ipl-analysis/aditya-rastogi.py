import pandas as pd
import numpy as np
player_match= pd.read_csv("DIM_PLAYER_MATCH.csv",delimiter=',',encoding= "ISO-8859-1",skiprows=[1])
#1.
perc={} #noting and printing percentage of young players every year
for year in player_match.Season_year.unique():
	young=player_match[player_match.Season_year==year][player_match.Age_As_on_match<25]['Player_Id'].unique()
	allPlayers=player_match[player_match.Season_year==year]['Player_Id'].unique()
	perc[year]=(len(young)/len(allPlayers))*100
print("Percentage of young players with corresponding years")
print(perc)  
#calculating total young "man of the match" and percentage
manMatch=player_match[player_match.is_manofThematch==1]['Player_Id'].unique()
manMatchYoung=player_match[player_match.Age_As_on_match<25][player_match.is_manofThematch==1]['Player_Id'].unique()
percManMatch=len(manMatchYoung)/len(manMatch)*100
print("Young players were man of the macth in "+str(percManMatch)+"% matches")
#finding and assigning youngest team each season
youngestTeam={}
for year in player_match.Season_year.unique():
    maxNo=0;teamWithMax=''
    for teamName in player_match.Player_team.unique():
        youngNo=len(player_match[(player_match['Season_year']==year)&(player_match['Player_team']==teamName)][player_match['Age_As_on_match']<25]['Player_Id'].unique())
        if(youngNo>maxNo):
            maxNo=youngNo
            teamWithMax=teamName
    youngestTeam[year]=teamWithMax
print("Teams with maximum young players every season") 
print(youngestTeam)   
#2
if len(player_match['Batting_hand'].value_counts()==5) :
    player_match['Batting_hand'] = player_match['Batting_hand'].map({'Right-hand bat':'Right-handed',
                                                                 '\xa0Right-hand bat':'Right-handed',
                                                                'Left-hand bat' : 'Left-handed',
                                                                '\xa0Left-hand bat' : 'Left-handed'})
print(player_match['Batting_hand'].value_counts())
rightManOfTheMatch=player_match[(player_match.Batting_hand=='Right-handed')&(player_match.is_manofThematch==1)]
leftManOfTheMatch=player_match[(player_match.Batting_hand=='Left-handed')&(player_match.is_manofThematch==1)]
print("Right handed Man of the Match:",len(rightManOfTheMatch))
print("Left handed Man of the Match:",len(leftManOfTheMatch))
if len(player_match['Bowling_skill'].value_counts()==21):
    player_match['Bowling_skill']=player_match['Bowling_skill'].map({
      'Right-arm offbreak':'Spin','Right-arm medium':'pace',
        'Right-arm fast-medium':'pace','Left-arm fast-medium':'pace','Legbreak googly':'Spin',
        'Right-arm medium-fast':'pace',
        'Slow left-arm orthodox':'Spin','Right-arm fast':'pace',
        'Slow left-arm chinaman':'Spin','Left-arm medium-fast':'pace',
        'Legbreak':'Spin','Right-arm bowler':'pace','Left-arm medium':'pace',
        'Left-arm fast':'pace','\xa0Left-arm fast':'pace','\xa0Right-arm fast-medium':'pace',
        'Right-arm medium fast':'pace','\xa0Right-arm medium-fast':'pace',
        '\xa0Right-arm offbreak':'Spin','\xa0Legbreak':'Spin'})
print(player_match["Bowling_skill"].value_counts())
PaceMOM=player_match[(player_match.Bowling_skill=='pace')&(player_match.is_manofThematch==1)]
SpinMOM=player_match[(player_match.Bowling_skill=='spin')&(player_match.is_manofThematch==1)]
print("Pace Bowling Man of the Match:",len(PaceMOM))
print("Spin Bowling Man of the Match:",len(SpinMOM))
#3.
print(player_match[(player_match.Batting_hand=='Right-handed')&(player_match.is_manofThematch ==1)]['Player_Name'][:2])
print(player_match[(player_match.Batting_hand=='Left-handed')&(player_match.is_manofThematch ==1)]['Player_Name'][:2])
print(player_match[(player_match.Role_Desc=='Keeper')&(player_match.is_manofThematch ==1)]['Player_Name'][:1])
print(player_match[(player_match.Batting_hand!='NaN')&(player_match.Bowling_skill!='NaN')&(player_match.is_manofThematch ==1)]['Player_Name'][4:5])
print(player_match[(player_match.Bowling_skill=='pace')&(player_match.is_manofThematch==1)]['Player_Name'][6:9])#as matthew hayden was repeated instead of 5:8 went for 6:9
print(player_match[(player_match.Bowling_skill=='Spin')&(player_match.is_manofThematch==1)]['Player_Name'][1:3])
#4.
allTeams=player_match.Player_team.unique()
allMatchTable=pd.DataFrame(0,columns=allTeams,index=allTeams)
for matchKey in player_match.Match_Id.unique():
    uniqueMatch=player_match[player_match['Match_Id']==matchKey].reset_index().loc[0]
    first=uniqueMatch['Player_team']
    opposition=uniqueMatch['Opposit_Team']
    if(uniqueMatch['IsPlayers_Team_won']==1):
        allMatchTable.loc[opposition][first]+=1
    else:
        allMatchTable.loc[first][opposition]+=1
maxWins=0;teamWonMost='';teamLostMost=''
for team1 in allMatchTable.index:
    for team2 in allMatchTable.columns:
        if(allMatchTable.loc[team1][team2]>maxWins):
            maxWins=allMatchTable.loc[team1][team2]
            teamWonMost=team2
            teamLostMost=team1
print('Most wins :\n'+teamWonMost+' beat '+teamLostMost+' '+str(maxWins)+' times')
