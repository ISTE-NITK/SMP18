import numpy as np
import pandas as pd

player_match = pd.read_csv("DIM_PLAYER_MATCH.csv",delimiter=',',encoding = "ISO-8859-1", skiprows=[1])
player_match
players=pd.read_csv("DIM_PLAYER.csv",delimiter=',',encoding = "ISO-8859-1", skiprows=[1])

player_match.fillna('None',inplace=True)
player_match['Player_team'].replace('sunrisers Hyderabad','Sunrisers Hyderabad',inplace=True)
player_match['Player_team'].replace('kings XI Punjab','Kings XI Punjab',inplace=True)



#Q1

seasons=player_match['Season_year'].unique()
for i in seasons:
    print("Season:",i)
    young_player=player_match[(player_match.Age_As_on_match<25)&(player_match.Season_year== i)]['Player_Id'].unique()
    total_players=player_match[player_match.Season_year==i]['Player_Id'].unique()
    per_young_player=len(young_player)/len(total_players)*100
    print("Percentage of young player",per_young_player)
    team_young=player_match.loc[player_match['Player_Id'].isin(young_player)].drop_duplicates(subset='Player_Id')
    bla=team_young['Player_team'].value_counts().index[0]
    print("Team Having Maximum Young Players:",bla,"\n")
mofm=player_match[(player_match.Age_As_on_match<25)&(player_match.is_manofThematch==1)]['Player_Id'].unique()
total_mofm=player_match[(player_match.is_manofThematch==1)]['Player_Id'].unique()
print("Percentage of Man of the Match won by Young Players:",len(mofm)/len(total_mofm)*100)
    



#Q2

if len(player_match['Batting_hand'].value_counts()==5) :
    player_match['Batting_hand'] = player_match['Batting_hand'].map({'Right-hand bat':'Right-handed',

                                                                 '\xa0Right-hand bat':'Right-handed',

                                                                'Left-hand bat' : 'Left-handed',

                                                                '\xa0Left-hand bat' : 'Left-handed'})
print(player_match['Batting_hand'].value_counts())
r_won=player_match[(player_match.Batting_hand=='Right-handed')&(player_match.IsPlayers_Team_won==1)]
l_won=player_match[(player_match.Batting_hand=='Left-handed')&(player_match.IsPlayers_Team_won==1)]
r_mom=player_match[(player_match.Batting_hand=='Right-handed')&(player_match.is_manofThematch==1)]
l_mom=player_match[(player_match.Batting_hand=='Left-handed')&(player_match.is_manofThematch==1)]
print("Team won when right handed played:",len(r_won))
print("Team won when left handed played:",len(l_won))
print("Right handed Man of the Match:",len(r_mom))
print("Left handed Man of the Match:",len(l_mom))

if len(player_match['Bowling_skill'].value_counts()==21):
    player_match['Bowling_skill']=player_match['Bowling_skill'].map({ 'Right-arm offbreak':'Spin','Right-arm medium':'pace',
        'Right-arm fast-medium':'pace','Legbreak googly':'pace',
        'Right-arm medium-fast':'pace','Left-arm fast-medium':'pace',
        'Slow left-arm orthodox':'Spin','Right-arm fast':'pace',
        'Slow left-arm chinaman':'Spin','Left-arm medium-fast':'pace',
        'Legbreak':'Spin','Right-arm bowler':'pace','Left-arm medium':'pace',
        'Left-arm fast':'pace','\xa0Left-arm fast':'pace','\xa0Right-arm fast-medium':'pace',
        'Right-arm medium fast':'pace','\xa0Right-arm medium-fast':'pace',
        '\xa0Right-arm offbreak':'Spin','\xa0Legbreak':'Spin'
})
print(player_match["Bowling_skill"].value_counts())
p_won=player_match[(player_match.Bowling_skill=='pace')&(player_match.IsPlayers_Team_won==1)]
s_won=player_match[(player_match.Bowling_skill=='spin')&(player_match.IsPlayers_Team_won==1)]
p_mom=player_match[(player_match.Bowling_skill=='pace')&(player_match.is_manofThematch==1)]
s_mom=player_match[(player_match.Bowling_skill=='spin')&(player_match.is_manofThematch==1)]
print("Team won when pace bowled:",len(p_won))
print("Team won when spin bowled:",len(s_won))
print("Pace Bowling Man of the Match:",len(p_mom))
print("Spin Bowling Man of the Match:",len(s_mom))

#Q3

  def best_team():
    print("Best team:\n")
    print(player_match[(player_match.Batting_hand=='Right-handed')&(player_match.is_manofThematch ==1)]['Player_Name'][:2])
    print(player_match[(player_match.Batting_hand=='Left-handed')&(player_match.is_manofThematch ==1)]['Player_Name'][:2])
    print(player_match[(player_match.Role_Desc=='Keeper')&(player_match.is_manofThematch ==1)]['Player_Name'][:1])
    print(player_match[(player_match.Batting_hand!='NaN')&(player_match.Bowling_skill!='NaN')&(player_match.is_manofThematch ==1)]['Player_Name'][4:5])
    print(player_match[(player_match.Bowling_skill=='pace')&(player_match.is_manofThematch==1)]['Player_Name'][5:8])
    print(player_match[(player_match.Bowling_skill=='Spin')&(player_match.is_manofThematch==1)]['Player_Name'][1:3])
best_team()

#Q4

seasons=player_match['Season_year'].unique()
for k in range(len(seasons)):
    team_name=player_match[(player_match.Season_year==seasons[k])]['Player_team'].unique()
    count=player_match[(player_match.Player_team==team_name[0])&(player_match.Opposit_Team==team_name[1])&(player_match.IsPlayers_Team_won==1)]['Match_Id'].value_counts()
    for i in range(len(team_name)):
        for j in range(len(team_name)):
            s=player_match[(player_match.Player_team==team_name[i])&(player_match.Opposit_Team==team_name[j])&(player_match.IsPlayers_Team_won==1)]['Match_Id'].value_counts()
            if(len(count)<len(s)):
                won_t=i
                lost_t=j
print(teamname[won_t],"won most of their matches against",team_name[lost_t],"in the season",seasons[k])
