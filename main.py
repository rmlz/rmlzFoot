# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:06:15 2019

@author: Ramon Barros
@github: https://github.com/rmlz
"""
from teams import teams
from random import randrange, shuffle
from pprint import pprint
from rmlzFoot.team import team
from rmlzFoot.game import game 
from rmlzFoot.common.commonfunctions import create_balanced_round_robin



team_names = []
teams_list = []
for item in teams: #create teams
    t1 = team(item['Name'], item['Power'])
    team_names.append(item['Name'])
    teams_list.append(t1)

selected = True
while selected:
  pprint(team_names)
  select_team = input('Select the team you want to control!:')
  if select_team in team_names:
     for i in teams_list:
        if i.name == select_team:
            i.player = True
            selected = False
        else:
          continue

games = []

# prepare the schedule, 0's designate free space  
schedule = []
shuffle(teams_list)


#g1 = game(t1,t2)
#g1.powers()
#g1.playball()


schedule = create_balanced_round_robin(teams_list)
round_ = 0

for r in schedule:
  round_ += 1
  mat = 0
  print('\n\n')
  print('ROUND: '+ str(round_))
  for match in r:
    mat += 1
    print('MATCH: '+ str(mat))
    print('-----------------')
    g = game(match[0],match[1])
    g.powers()
    g.playball()
    games.append(g)
    for item in teams_list:
      points = (item.win * 3) + item.tie
      print(item.name + ' :' + str(points))
    print('')
    

