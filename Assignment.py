import pandas as pd
import numpy as np

def count(data,col,target,more=False):
    cnt=0
    for i in data.index:
        if(more==False):
            if(data.loc[i][col]==target):
                cnt+=1
        else:
            if(data.loc[i][col] in target):
                cnt+=1
    return cnt

players_match=pd.read_csv('/home/sakshat/Downloads/ipl-2017/DIM_PLAYER_MATCH.csv',encoding = "ISO-8859-1",delimiter=',',skiprows=[1])
players_match.fillna('None',inplace=True)
players_match['Player_team'].replace('sunrisers Hyderabad','Sunrisers Hyderabad',inplace=True)
players_match['Player_team'].replace('kings XI Punjab','Kings XI Punjab',inplace=True)

young_players_match=players_match.loc[players_match['Age_As_on_match']<25]

#% of young players playing
young_perc={}
for i in players_match.Season_year.unique():
    x=len(young_players_match[young_players_match['Season_year']==i]['Player_Id'].unique())
    y=len(players_match[players_match['Season_year']==i]['Player_Id'].unique())
    young_perc[i]=x/y*100
print('\n\n% of young players playing matches per season :\n')
print(young_perc)

#Team with max young players
max_young={}
for i in players_match.Season_year.unique():
    max_young_no=0;max_young_team=''
    for j in players_match.Player_team.unique():
        x=len(young_players_match[(young_players_match['Season_year']==i)&(young_players_match['Player_team']==j)]['Player_Id'].unique())
        if(x>max_young_no):
            max_young_no=x
            max_young_team=j
    max_young[i]=max_young_team
print('\n\nTeams with maximum number of young players per season :\n')
print(max_young)

#% of young players winning Man of the Match
x=young_players_match['is_manofThematch'].value_counts().loc[1]
y=players_match['is_manofThematch'].value_counts().loc[1]
motm_young=x/y*100
print('\n\n% of young players winning MOTM :\n')
print(motm_young)

players_match['Batting_hand']=players_match['Batting_hand'].map({'Right-hand bat':'R','\xa0Right-hand bat':'R','Right-handed':'R','Left-hand bat':'L','\xa0Left-hand bat':'L'})
r_data=players_match.loc[players_match['Batting_hand']=='R']
l_data=players_match.loc[players_match['Batting_hand']=='L']

#Right-handed batsmen vs. Left-handed batsmen
def check_performance(r_data,l_data):
    a=count(r_data,'is_manofThematch',1)
    b=count(l_data,'is_manofThematch',1)
    c=count(r_data,'IsPlayers_Team_won',1)
    d=count(l_data,'IsPlayers_Team_won',1)
    e=count(r_data,'Role_Desc','Captain')+count(r_data,'Role_Desc','CaptainKeeper')
    f=count(l_data,'Role_Desc','Captain')+count(l_data,'Role_Desc','CaptainKeeper')
    print('\n\nMan of the Matches\n'+str(a)+'\t'+str(b)+'\nTeam Wins\n'+str(c)+'\t'+str(d)+'\nMatches as Captains\n'+str(e)+'\t'+str(f))

print('\n\n\nRight-Handed vs. Left-Handed')
check_performance(r_data,l_data)

bowling_skill=[]
for i in players_match.index:
    given=players_match.loc[i]['Bowling_skill'].split(' ')
    given2=[]
    for j in given:
        given2.extend(j.split('-'))
    if('None' in given2 or players_match.loc[i]['Player_Name']==players_match.loc[i]['Player_keeper']):
        bowling_skill.append('-')
    elif('medium' in given2 or 'fast' in given2 or 'bowler' in given2):
        bowling_skill.append('Pace')
    else:
        bowling_skill.append('Spin')
players_match['Bowling_skill']=pd.Series(bowling_skill)
pace_data=players_match[players_match['Bowling_skill']=='Pace']
spin_data=players_match[players_match['Bowling_skill']=='Spin']

print('\n\n\nPace Bowlers vs. Spin Bowlers')
check_performance(pace_data,spin_data)

wk_data=players_match[(players_match['Role_Desc']=='Keeper')|(players_match['Role_Desc']=='CaptainKeeper')]

def best(data,num):
    scores={}
    for i in list(data['Player_Name'].unique()):
        player_data=data.loc[data['Player_Name']==i]
        if(len(player_data)>50):
            scores[i]=(count(player_data,'is_manofThematch',1)+count(player_data,'IsPlayers_Team_won',1))
            scores[i]/=((player_data.shape[0])*2)
        else:
            scores[i]=0
    return sorted(scores.items(),key=lambda x:x[1],reverse=True)[:num]

#print(best(l_data,5))
#MEK Hussey   CH Gayle

#print(best(r_data,5))
#SR Tendulkar   YK Pathan

#print(best(pace_data,5))
#MEK Hussey   KA Pollard   DR Smith   SL Malinga

#print(best(spin_data,5))
#SR Tendulkar   YK Pathan   CH Gayle   SB Jakati   SK Raina

#print(best(wk_data,1))
#MS Dhoni

best_10={'wk':'MS Dhoni','right-handed':['SR Tendulkar','YK Pathan'],'left-handed':['MEK Hussey','CH Gayle'],'pace':['KA Pollard','DR Smith','SL Malinga'],'spin':['SB Jakati','SK Raina']}

#print(best(players_match,8))
#'MEK Hussey   SR Tendulkar   YK Pathan   CH Gayle   SB Jakati   KA Pollard   MS Dhoni   AT Rayudu

#All-Rounder is player (other than best 10) with highest score
best_10['all_rounder']='AT Rayudu'
best_11=best_10

print('\n\nIPL Best XI :\n')
print(best_11)

ipl_teams=players_match.Player_team.unique()
head_to_head=pd.DataFrame(0,columns=ipl_teams,index=ipl_teams)
for i in players_match.Match_Id.unique():
    match_data=players_match[players_match['Match_Id']==i].reset_index().loc[0]
    player_team=match_data['Player_team']
    opp_team=match_data['Opposit_Team']
    if(match_data['IsPlayers_Team_won']==1):
        head_to_head.loc[opp_team][player_team]+=1
    else:
        head_to_head.loc[player_team][opp_team]+=1
most_wins=0;win_team='';against_team=''
for i in head_to_head.index:
    for j in head_to_head.columns:
        if(head_to_head.loc[i][j]>most_wins):
            most_wins=head_to_head.loc[i][j]
            win_team=j
            against_team=i
            
print('\n\nMost wins by an IPL team against another :\n'+win_team+' against '+against_team+' - '+str(most_wins)+' wins!')
