#1
import pandas as pd
import numpy as np
pm=pd.read_csv("DIM_PLAYER_MATCH.csv",encoding="ISO-8859-1")
team_name=pm[(pm.Season_year==2008)]['Player_team'].unique()
for i in range (2008, 2018):
	a=pm[(pm.Season_year==i)&(pm.Age_As_on_match<25)]['Player_Id'].value_counts()
	b=pm[(pm.Season_year==i)]['Player_Id'].value_counts()
	print("percentage of young players in season",i,"is")
	print((len(a)/len(b))*100)
	k=0
	l=0
	c=0
	for j in range (8):
		n=pm[(pm.Season_year==i)&(pm.Age_As_on_match<25)&(pm.Player_team ==team_name[j])]['Player_Id'].value_counts()
		if(len(n)>k):
			c = j
			k= len(n)
	print("the team with max young players is ",team_name[c],"with",k,"young players")
m=pm[(pm.Age_As_on_match<25)&(pm.is_manofThematch==1)]['Player_Id'].value_counts()
l=pm[(pm.is_manofThematch==1)]['Player_Id'].value_counts()
print("percentage of man of the match award won by young players is",(len(m)/len(l))*100)
print()

#2.
def repl (name):
	pm['Bowling_skill']=pm['Bowling_skill'].replace(name,'spin')
repl('\xa0Legbreak')
repl('Slow left-arm orthodox')
repl('Slow left-arm chinaman')
repl('Right-arm offbreak')
repl('Legbreak googly')
repl('\xa0Right-arm offbreak')
def count(name):
	s=pm[(pm.Bowling_skill.str.contains(name))&(pm.is_manofThematch==1)]['Player_Name'].value_counts()
	return (sum(s)/len(s))*100
a=count('spin')
b=count('arm')
if a>b:
	print("spin bowlers perform better than pace bowlers")
else:
	print("pace bowlers perform better than spin bowlers")
#pm=pd.read_csv("DIM_PLAYER_MATCH.csv",encoding="ISO-8859-1")
def c (name1,name2):
	u=pm[(pm.Bowling_skill.str.contains(name1))&(pm.is_manofThematch==1)]['Player_Name'].value_counts()
	u=u.append(pm[(pm.Bowling_skill.str.contains(name2))&(pm.is_manofThematch==1)]['Player_Name'].value_counts())
	return (sum(u)/len(u))*100
r=c('Right','Legbreak')
l=c('Left','left')
if (r>l):
	print("Right-handed players perform better than left-handed players")
else:
	print("left-handed players perform better than right-handed players")
print()
#3.
print("the efficient team would have")
if len(pm['Batting_hand'].value_counts())==5:
	pm['Batting_hand']=pm['Batting_hand'].map({'Right-hand bat':'Right-handed','\xa0Right-hand bat':'Right-handed','Left-hand bat':'Left-handed','\xa0Left-hand bat':'Left-handed',np.nan:'none'})
def batsman(hand):
	a=pm[(pm.Batting_hand==hand)&(pm.is_manofThematch==1)]['Player_Name'].value_counts()
	print("2",hand,"batsman are=")
	print(a.index[0:2])
batsman('Right-handed')
batsman('Left-handed')
w=pm[(pm.is_manofThematch==1)]['Player_Name'].value_counts()
print("wicket keeper=")
print(w.index[0:1])
ar=pm[(pm.is_manofThematch==1)&(pm.Bowling_skill.isnull()==False)]['Player_Name'].value_counts()
print("all rounder:")
print(ar.index[3:4])
pm['Bowling_skill']=pm['Bowling_skill'].replace(np.nan,'none')
def repl(name):
	pm['Bowling_skill']=pm['Bowling_skill'].replace(name,'spin')
repl('\xa0Legbreak')
repl('Slow left-arm orthodox')
repl('Slow left-arm chinaman')
repl('Right-arm offbreak')
repl('Legbreak googly')
repl('\xa0Right-arm offbreak')
s=pm[(pm.Bowling_skill.str.contains('spin'))&(pm.is_manofThematch==1)]['Player_Name'].value_counts()
print("2 spin bowlers")
print(s[1:2])
print(s[3:4])
p=pm[(pm.Bowling_skill.str.contains('arm'))&(pm.is_manofThematch==1)]['Player_Name'].value_counts()
print("3 pace bowlers")
print(p[1:4])
print()

#4.
a=pm[(pm.Season_year==2008)]['Player_team'].unique()
k=0
for i in range(8):
	for j in range(8):
		s=pm[(pm.Player_team==a[i])&(pm.Opposit_Team==a[j])&(pm.IsPlayers_Team_won==1)]['Match_Id'].value_counts()
		if(k<len(s)):
			pt=i
			ot=j
print("the team which won most of their matches is",a[pt],"against",a[ot])
