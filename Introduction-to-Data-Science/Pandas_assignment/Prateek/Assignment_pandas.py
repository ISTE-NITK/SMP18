
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


player_match=pd.read_csv("/home/prateek/Documents/Python/Data_science/Data_science_smp/Ipl/DIM_PLAYER_MATCH.csv",encoding="ISO-8859-1",skiprows=[1])


# In[3]:


player_match


# In[4]:


#Q1:
for i in range(2008,2018):
    yp=player_match.loc[(player_match.Age_As_on_match<25) & (player_match.Season_year==i)]
    lyp=len(yp)
    l=len(player_match)
    per=(lyp/l)*100
    team=yp.Player_team.value_counts().index[0]
    print("% of young players and team having max players  in {:d} season={:f} and {}".format(i,per,team))
yp=player_match.loc[(player_match.Age_As_on_match<25) & (player_match.is_manofThematch==1.0)]
lyp=len(yp)
l=len(player_match)
per=(lyp/l)*100
print("Percentage of man of the match award won by young player={}".format(per))


# In[11]:


#Q2:
def bowl(s):
    if(s=="Legbreak" or s=="Legbreak googly"):
        s="right-handed leg spin bowler"
    return s
player_match.Bowling_skill=player_match.Bowling_skill.map(bowl,na_action="ignore")

def null(srs):
    if(pd.isnull(srs.Bowling_skill)==True):
        srs.Bowling_skill=srs.Batting_hand
    return srs
player_match=player_match.apply(null,axis="columns")
right=len(player_match.loc[player_match.Bowling_skill.str.contains("right",case=False) & player_match.is_manofThematch==1])
left=len(player_match.loc[player_match.Bowling_skill.str.contains("left",case=False) & player_match.is_manofThematch==1])
print("Number of times man of the match recieved by right handed player={} , and left handed player={}".format(right,left))


# In[8]:


#Q3:
right_list=list((player_match.loc[player_match.Batting_hand.str.contains("right",case=False) & player_match.is_manofThematch==1]).Player_Name.value_counts().index[0:2])

left_list=list((player_match.loc[player_match.Batting_hand.str.contains("left",case=False) & player_match.is_manofThematch==1]).Player_Name.value_counts().index[0:2])

keeper=((player_match.loc[((player_match.Role_Desc=="Keeper") | (player_match.Role_Desc=="CaptainKeeper")) & player_match.is_manofThematch==1]).Player_Name.value_counts().index[0])


pacers=list(player_match.loc[((player_match.Bowling_skill.str.contains("fast")) | (player_match.Bowling_skill.str.contains("medium"))) & player_match.is_manofThematch==1].Player_Name.value_counts().index[10:13])

A_rounder=(player_match.loc[((player_match.Bowling_skill.str.contains("fast")) | (player_match.Bowling_skill.str.contains("medium"))) & player_match.is_manofThematch==1].Player_Name.value_counts().index[8])

spin=list(player_match.loc[((player_match.Bowling_skill.str.contains("break")) | (player_match.Bowling_skill.str.contains("slow")) | (player_match.Bowling_skill.str.contains("spin")) ) & player_match.is_manofThematch==1].Player_Name.value_counts().index[[7,12]])
#player_match.Bowling_skill.unique()

type(right_list)
team=right_list+left_list+pacers+spin
#right_list.append(keeper)
team.append(keeper)
team.append(A_rounder)
print("best team is:",team)


# In[10]:


#Q4:
match=pd.read_excel("/home/prateek/Documents/Python/Data_science/Data_science_smp/Ipl/DIM_MATCH.xlsx",encoding="ISO-8859-1")
match.dropna(axis="index",subset=["match_winner"],inplace=True)
match

def win_lose(d):
    if(d.match_winner!=d.Team1):
        d.match_winner=d.match_winner+"-"+d.Team1
    else:
        d.match_winner=d.match_winner+"-"+d.Team2
    return d
(match.apply(win_lose,axis="columns")).match_winner.value_counts().index[0]

