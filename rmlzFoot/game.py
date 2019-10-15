# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:06:15 2019

@author: Ramon Barros
@github: https://github.com/rmlz
"""
from random import randrange, shuffle
from pprint import pprint
from time import sleep as timeslp
from rmlzFoot.common.commonfunctions import average, dice

class game:
    def __init__(self, team1, team2):
        
        
        print('TODAY IS A GREAT DAY FOR A CLASSIC RIVALRY!!\n')
        print(team1.name + ' VS ' + team2.name + '!!!\n')
        print('ONLY IN THE SCREEN OF RAMALSPORTS! PLIM PLIM!!!\n')
        timeslp(3)
        self.debug = False
        t1players = team1.players
        self.homeTeam_goalie = t1players[0]
        
        t1players = t1players[1:]
        print(team1.name + ' PLAYERS')
        print('-----------------------')
        pprint(t1players)
        print('')
        if team1.player == True:
            print('\n------------------')
            print(team1.name +' tactics: \n')
            print('------------------')
            
            try:
                print('Last game tactics: ' + str(team1.tactics)+ '. \n')
            except:
                pass
            
            while True:
                print('1 - Offensive')
                print('2 - Defensive')
                print('3 - Balanced\n')
                tact_number1 = input('Select your team state of mind\n')
                try:
                    tact_number1 = int(tact_number1)
                    if tact_number1 == 1:
                        print(team1.name + ' selected Offensive')
                        team1.tactics = 'Offensive'
                        break
                    elif tact_number1 == 2:
                        print(team1.name + ' selected Defensive')
                        team1.tactics = 'Defensive'
                        break
                    elif tact_number1 == 3:
                        print(team1.name + ' selected Balanced')
                        team1.tactics = 'Balanced'
                        break
                    else:
                        print('Select one of the numbers below.\n')
                except ValueError:
                    print('Select one of the numbers below.\n')
            
            try:
                print('Last game: ' + str(team1.defend) + ' defenders')
            except:
                pass
            
            while True:
                team1.defend = input('How many defenders you want to use? (2-6)\n')
                try:
                    team1.defend = int(team1.defend)
                    if team1.defend > 6:
                        print("You can't use that much players to defend!")
                    elif team1.defend < 2: 
                        print('You must use at least 2 players to defend!')
                    else:
                        break
                except ValueError:
                    print('\n' + str(team1.defend) + ' is not an integral number')
            
            self.homeTeam_defenders = t1players[0:team1.defend]
            
            t1players = t1players[team1.defend:]
            pprint(t1players)
            
            try:
                print('Last game: ' + str(team1.mildf) + ' mildfielders')
            except:
                pass
            
            while True:
                team1.mildf = input('How many mildfielders you want to use? (2-6)\n')
                try:
                    team1.mildf = int(team1.mildf)
                    if team1.mildf > 6:
                        print("You can't use that much players in the mildfield!")
                    elif team1.mildf < 2: 
                        print('You must use at least 3 players in the mildfield!')
                    elif team1.mildf + team1.defend > 9:
                        print('You need players in the Attack as well!')
                    else:
                        break
                except ValueError:
                    print('\n' + str(team1.mildf) + ' is not an integral number')
            
            self.homeTeam_mildfielders = t1players[0:team1.mildf]
            
            t1players = t1players[team1.mildf:]
            pprint(t1players)
            
            print('\nThe players left in the list are your attackers!')
            team1.attackers = 10 - team1.defend - team1.mildf
            self.homeTeam_attackers = t1players
        else:
                if team1.power - team2.power > 5:
                  team1.tactics = 'Offensive'
                  team1.defend = randrange(3) + 1

                  self.homeTeam_defenders = t1players[0:team1.defend]
                  t1players = t1players[team1.defend:]

                  team1.mildf = randrange(9-team1.defend) + 1

                  self.homeTeam_mildfielders = t1players[0:team1.mildf]
                  t1players = t1players[team1.mildf:]

                  team1.attackers = 10 - team1.defend - team1.mildf 
                  self.homeTeam_attackers = t1players
                elif team1.power - team2.power < 5:
                  team1.tactics = 'Defensive'
                  team1.defend = randrange(3) + 3

                  self.homeTeam_defenders = t1players[0:team1.defend]
                  t1players = t1players[team1.defend:]

                  team1.mildf = 9 - team1.defend

                  self.homeTeam_mildfielders = t1players[0:team1.mildf]
                  t1players = t1players[team1.mildf:]

                  team1.attackers = 10 - team1.defend - team1.mildf
                  self.homeTeam_attackers = t1players
                else:
                  team1.tactics = 'Balanced'
                  team1.defend = randrange(2) + 3

                  self.homeTeam_defenders = t1players[0:team1.defend]
                  t1players = t1players[team1.defend:]

                  team1.mildf = randrange(3) + 3

                  self.homeTeam_mildfielders = t1players[0:team1.mildf]
                  t1players = t1players[team1.mildf:]

                  team1.attackers = 10 - team1.defend - team1.mildf
                  self.homeTeam_attackers = t1players
        
        
        #==============================================
        
        t2players = team2.players
        self.awayTeam_goalie = t2players[0]
        
        t2players = t2players[1:]
        print(team2.name + ' PLAYERS')
        print('-----------------------')
        pprint(t2players)
        print('')
        if team2.player == True:
            print('\n------------------')
            print(team2.name +' tactics: \n')
            print('------------------')
            
            try:
                print('Last game tactics: ' + str(team2.tactics)+ '.\n')
            except:
                pass
            
            while True:
                print('1 - Offensive')
                print('2 - Defensive')
                print('3 - Balanced\n')
                tact_number2 = input('Select your team state of mind\n')
                try:
                    tact_number2 = int(tact_number2)
                    if tact_number2 == 1:
                        print(team2.name + ' selected Offensive')
                        team2.tactics = 'Offensive'
                        break
                    elif tact_number2 == 2:
                        print(team1.name + ' selected Defensive')
                        team2.tactics = 'Defensive'
                        break
                    elif tact_number2 == 3:
                        print(team2.name + ' selected Balanced')
                        team2.tactics = 'Balanced'
                        break
                    else:
                        print('Select one of the numbers below.\n')
                
                except ValueError:
                    print('Select one of the numbers below.\n')
            
            
            
            try:
                print('Last game: ' + str(team2.defend) + ' defenders')
            except:
                pass
            
            while True:
                team2.defend = input('How many defenders you want to use? (2-6)\n')
                try:
                    team2.defend = int(team2.defend)
                    if team2.defend > 6:
                        print("You can't use that much players to defend!")
                    elif team2.defend < 2: 
                        print('You must use at least 2 players to defend!')
                    else:
                        break
                except ValueError:
                    print('\n' + str(team2.defend) + ' is not an integral number')
            
            self.awayTeam_defenders = t2players[0:team2.defend]
            
            t2players = t2players[team2.defend:]
            pprint(t2players)
            
            try:
                print('Last game: ' + str(team2.mildf) + ' mildfielders')
            except:
                pass
            
            while True:
                team2.mildf = input('How many mildfielders you want to use? (2-6)\n')
                try:
                    team2.mildf = int(team2.mildf)
                    if team2.mildf > 6:
                        print("You can't use that much players in the mildfield!")
                    elif team2.mildf < 2: 
                        print('You must use at least 3 players in the mildfield!')
                    elif team2.mildf + team2.defend > 9:
                      print('You need players in the Attack as well!')
                    else:
                        break
                except ValueError:
                    print('\n' + str(team2.mildf) + ' is not an integral number')
            
            self.awayTeam_mildfielders = t2players[0:team2.mildf]
            
            t2players = t2players[team2.mildf:]
            pprint(t2players)
            
            print('\nThe players left in the list are your attackers!')
            team2.attackers = 10 - team2.defend - team2.mildf
            self.awayTeam_attackers = t2players
        else:
            if team2.power - team1.power > 5:
                  team2.tactics = 'Offensive'
                  team2.defend = randrange(4) + 1

                  self.awayTeam_defenders = t2players[0:team2.defend]
                  t2players = t2players[team2.defend:]

                  team2.mildf = randrange(9-team2.defend) + 1

                  self.awayTeam_mildfielders = t2players[0:team2.mildf]
                  t2players = t2players[team2.mildf:]

                  team2.attackers = 10 - team2.defend - team2.mildf 
                  self.awayTeam_attackers = t2players
            elif team2.power - team1.power > 3:
                  team2.tactics = 'Defensive'
                  team2.defend = randrange(3) + 3

                  self.awayTeam_defenders = t2players[0:team2.defend]
                  t2players = t2players[team2.defend:]

                  team2.mildf = 9 - team2.defend

                  self.awayTeam_mildfielders = t2players[0:team2.mildf]
                  t2players = t2players[team2.mildf:]

                  team2.attackers = 10 - team2.defend - team2.mildf
                  self.awayTeam_attackers = t2players
            else:
                  team2.tactics = 'Balanced'
                  team2.defend = randrange(2) + 3

                  self.awayTeam_defenders = t2players[0:team2.defend]
                  t2players = t2players[team2.defend:]

                  team2.mildf = randrange(3) + 3

                  self.awayTeam_mildfielders = t2players[0:team2.mildf]
                  t2players = t2players[team2.mildf:]

                  team2.attackers = 10 - team2.defend - team2.mildf
                  self.awayTeam_attackers = t2players      
        
        self.homeTeam = team1
        self.awayTeam = team2
        
        
    def powers(self):
        #Define the power of gk, def, mid and atk.
        
        ##############
        #   TEAM 1   #
        ##############
        if self.homeTeam.tactics == 'Balanced':
            gkmod1 = 7
            defmod1 = 4
            midmod1 = 3
            atkmod1 = 1
        elif self.homeTeam.tactics == 'Defensive':
            gkmod1 = 15
            defmod1 = 6
            midmod1 = 3
            atkmod1 = 0
        elif self.homeTeam.tactics == 'Offensive':
            gkmod1 = 5
            defmod1 = 1
            midmod1 = 4
            atkmod1 = 3
            
        if self.awayTeam.tactics == 'Balanced':
            gkmod2 = 7
            defmod2 = 4
            midmod2 = 3
            atkmod2 = 1
        elif self.awayTeam.tactics == 'Defensive':
            gkmod2 = 15
            defmod2 = 6
            midmod2 = 3
            atkmod2 = 0
        elif self.awayTeam.tactics == 'Offensive':
            gkmod2 = 5
            defmod2 = 1
            midmod2 = 4
            atkmod2 = 3
        
        self.homeTeam.gk_pwr = gkmod1 + self.homeTeam_goalie[1]
        self.homeTeam.def_pwr = (1 + (defmod1 * len(self.homeTeam_defenders))) + average(self.homeTeam_defenders)
        self.homeTeam.mid_pwr = (1 + (midmod1 * len(self.homeTeam_mildfielders))) + average(self.homeTeam_mildfielders)
        self.homeTeam.atk_pwr = (1 + (atkmod1 * len(self.homeTeam_attackers))) + average(self.homeTeam_attackers)
        
        print(self.homeTeam.name + ' POWER!!!')
        print('GKP: ' + str(self.homeTeam.gk_pwr))
        print('DEF: ' + str(self.homeTeam.def_pwr))
        print('MID: ' + str(self.homeTeam.mid_pwr))
        print('ATK: ' + str(self.homeTeam.atk_pwr))
        print('MORALE: ' + str(self.homeTeam.morale))
        print('')

        ##############
        #   TEAM 2   #
        ##############
        
        self.awayTeam.gk_pwr = gkmod2 + self.awayTeam_goalie[1]
        self.awayTeam.def_pwr = (1 + (defmod2 * len(self.awayTeam_defenders))) + average(self.awayTeam_defenders)
        self.awayTeam.mid_pwr = (1 + (midmod2 * len(self.awayTeam_mildfielders))) + average(self.awayTeam_mildfielders)
        self.awayTeam.atk_pwr = (1 + (atkmod2 * len(self.awayTeam_attackers))) + average(self.awayTeam_attackers)
        
        print(self.awayTeam.name + ' POWER!!!')
        print('GKP: ' + str(self.awayTeam.gk_pwr))
        print('DEF: ' + str(self.awayTeam.def_pwr))
        print('MID: ' + str(self.awayTeam.mid_pwr))
        print('ATK: ' + str(self.awayTeam.atk_pwr))
        print('MORALE: ' + str(self.awayTeam.morale))
        print('')
        
        input('Press enter to continue...')
        
    def playball(self):
        if self.homeTeam.player == True or self.awayTeam.player == True:
            watch = True
        else:
            y = input('Do you want to watch this match? (y-n)\n')
            if y.startswith('y'):
                watch = True
            else:
                watch = False
        if watch:
            while True:
                game_spd = input('Select the match speed (lower number = slower) (1-10)!\n')
                try:
                    game_spd = int(game_spd)
                    if game_spd > 10:
                        game_spd = 10
                    elif game_spd < 1:
                        game_spd = 1
                    break
                except ValueError:
                  print('SELECT A NUMBER BETWEEN 1 AND 10!\n')
        else:
          game_spd = 1000 

        regular_time = 45
        
        
        Score_HT = 0
        Score_AT = 0
        
        #Home team morale boost
        self.homeTeam.morale += 0.01    
        
        if self.homeTeam.morale > 1.1:
            self.homeTeam.morale = 1.1
        if self.awayTeam.morale > 1.1:
            self.awayTeam.morale = 1.1
        if self.homeTeam.morale < 0.9:
          self.homeTeam.morale = 0.95
        if self.awayTeam.morale <0.9:
          self.awayTeam.morale = 0.95
        
        counter_home = False
        counter_away = False
        
        j = 0
        while True:
            ref_time = randrange(4)
            if j == 0:
                print('The Referee sound the whistle! It is the game start!\n')
                timeslp(2/game_spd) 
            else:
                print('The Referee sound the whistle! It is the second half!\n')
                timeslp(2/game_spd) 
                
            chance = (((self.homeTeam.mid_pwr + self.awayTeam.mid_pwr) /1) / 100) * 25 #chance of game play by teams
            if chance < 10:
                chance = 10
            if self.homeTeam.tactics == 'Offensive':
                chance += 5
            if self.awayTeam.tactics == 'Offensive':
                chance += 5
            print('chance', chance)
            foul_chance_home = 100 - ((self.homeTeam.mid_pwr + self.homeTeam.def_pwr) /1)
            if foul_chance_home > 33:
                foul_chance_home = 33
            foul_chance_away = 100 - ((self.awayTeam.mid_pwr + self.awayTeam.def_pwr) /1)
            if foul_chance_away >33:
                foul_chance_away = 33
            if self.homeTeam.tactics == 'Defensive':
                foul_chance_home += 15
            if self.awayTeam.tactics == 'Defensive':
                foul_chance_away += 15
            
            for i in range(regular_time + ref_time):
                print('')
                if i > 43:
                    print('REFEREE TIME')
                print("SCORE")
                print('-------------------------------------------')
                print(self.homeTeam.name + ' ' + str(Score_HT) + '|')
                print(self.awayTeam.name + ' ' + str(Score_AT) + '|')
                print('-------------------------------------------')
                print('Minute: ' + str(i+1))
                print('HALF: ' + str(j+1))
                print('')
                timeslp(1/game_spd) 
                
                #checks if something will happen:
                
                
                if randrange(100)+1 <= chance or counter_home or counter_away:
                
                    #checks Home Team atk
                    
                    home_Mdf_dice = dice(self.homeTeam.mid_pwr, self.homeTeam.morale)
                    away_Mdf_dice = dice(self.awayTeam.mid_pwr, self.awayTeam.morale)
                    home_Mdf = home_Mdf_dice[2]   
                    away_Mdf = away_Mdf_dice[2]   
                    
                    if self.debug:
                        print('home_Mdf, away_Mdf')
                        print(home_Mdf, away_Mdf)
                        print('')
                    
                        
                    if home_Mdf > away_Mdf or counter_home: #Home team is preparing a play
                        if self.debug:
                            print('Home team Morale Boost = 0.001\n')
                        if counter_home:
                            counter_home = False
                            print(self.homeTeam.name +' are running in a counter attack!\n')
                            timeslp(2/game_spd)
                        self.homeTeam.morale += 0.001
                        print(self.homeTeam.name + ' have the ball possession...\n')
                        timeslp(1/game_spd)
                        print(self.homeTeam.name + ' are passing the ball in the mildfield...\n')
                        timeslp(2/game_spd)    
                        print(self.homeTeam.name + ' does a great pass forward!\n')
                        timeslp(2/game_spd)                
                        print(self.homeTeam.name + ' are trying to find a breach in the defense...\n')
                        timeslp(2/game_spd) 
                        
                        home_Atk_dice = dice(self.homeTeam.atk_pwr, self.homeTeam.morale)
                        away_Def_dice = dice(self.awayTeam.atk_pwr, self.awayTeam.morale)
                        home_Atk = home_Atk_dice[2]
                        away_Def = away_Def_dice[2]
                        
                        if self.debug:
                            print('home_Atk, away_Def')
                            print(home_Atk, away_Def)
                            print('')
                        
                            
                            
                        if home_Atk > away_Def: #Attackers are preparing the play
                            
                            if self.debug:
                                print('Home team Morale Boost = 0.001')
                                print('')
                            self.homeTeam.morale += 0.001
                                
                            
                            print(self.homeTeam.name + ' just found the breach! What a pass!\n')
                            timeslp(1/game_spd)   
                            
                            penalty_home = False
                            inside_area = False
                            rebound = True
                            new_rb = False
                            foul_home = False
                            while rebound:
                                home_Atk_dice = dice(self.homeTeam.atk_pwr, self.homeTeam.morale)
                                away_Def_dice = dice(self.awayTeam.atk_pwr, self.awayTeam.morale)
                                home_Atk = home_Atk_dice[2]
                                away_Def = away_Def_dice[2]
                                foul_test = randrange(100)+1
                                if self.debug:
                                    print('home_Atk, away_Def')
                                    print(home_Atk, away_Def)
                                    print('')
                                    print('foul_chance_away, foul_test')
                                    print(foul_chance_away, foul_test)
                                
                                if foul_chance_away - foul_test > 25: #HARD FOUL HAPPENS!
                                    print(self.awayTeam.name + "'s defense player tackle the ofense!!\n")
                                    timeslp(1/game_spd)
                                    print('FOUL! What an agressive impact!!\n')
                                    timeslp(3/game_spd)
                                    if inside_area == True:
                                      print(self.homeTeam.name + ' PENALTY KICK!!!!')
                                      timeslp(3/game_spd)
                                      penalty_home = True
                                    else:
                                      print(self.homeTeam.name + " That's a good oportunity for a goal!!")
                                      foul_home = True
                                
                                elif foul_chance_away - foul_test > 10: #SOFT FOUL HAPPEN
                                    print(self.awayTeam.name + "'s defense player grabbed the offense player by the shirt!!\n")
                                    timeslp(1/game_spd)
                                    print(self.awayTeam.name + " what a silly foul!\n")
                                    timeslp(4/game_spd)
                                    if inside_area == True:
                                      print(self.homeTeam.name + ' PENALTY KICK!!!!')
                                      timeslp(3/game_spd)
                                      penalty_home = True
                                    else:
                                      foul_home = True
                                
                                if penalty_home:
                                  print(self.homeTeam.name + ' prepares the ball in the penalty mark...\n')
                                  timeslp(5/game_spd)
                                  print(self.homeTeam.name + ' looks to the goal...\n')
                                  timeslp(4/game_spd)
                                  print('Referee authorizes the kick!\n')
                                  timeslp(3/game_spd)
                                  penal = randrange(10) + 1
                                  if penal > 5:
                                    print(self.homeTeam.name + ' SCOORESS!!!\n')
                                    timeslp(1/game_spd)
                                    print(self.homeTeam.name + ' No chance for the Keeper!!\n')
                                    timeslp(1/game_spd)
                                    Score_HT += 1
                                    if self.debug:
                                        print('Home team Morale Boost = 0.002')
                                        print('')
                                    self.homeTeam.morale += 0.002
                                  else:
                                    print(self.homeTeam.name + ' OH NO!!! THE KEEPER CAUGHT THE BALL!!!!\n')
                                    timeslp(3/game_spd)
                                    print(self.homeTeam.name + "'s players are desolated!!!\n") 
                                    timeslp(2/game_spd)

                                    if self.debug:
                                        print('Home team Morale Down = 0.002')
                                        print('')
                                    self.homeTeam.morale -= 0.002

                                  break
                                    

                                if foul_home == True:
                                    pass_or_shoot = randrange(10)+1
                                    if pass_or_shoot > 4: #BALL INSIDE THE AREA
                                        print(self.homeTeam.name + " Long ball inside the area!!\n")
                                        foul_home = False
                                        timeslp(2/game_spd)
                                        home_Atk_dice = dice(self.homeTeam.atk_pwr, self.homeTeam.morale)
                                        away_Def_dice = dice(self.awayTeam.atk_pwr, self.awayTeam.morale)
                                        home_Atk = home_Atk_dice[2]
                                        away_Def = away_Def_dice[2]
                                    else:
                                        home_Atk = away_Def + 1
                                    
                                    
                                if home_Atk > away_Def: #Defender could not stop the play
                                    offside = False
                                    offside_chance = randrange(10)+1
                                    if self.awayTeam.tactics == 'Defensive':
                                        if offside_chance > 3:
                                            offside = True
                                    elif self.awayTeam.tactics == 'Offensive':
                                        if offside_chance > 8:
                                            offside = True
                                    else:
                                        if offside_chance > 6:
                                            offside = True
            
                                    home_Atk_dice = dice(self.homeTeam.atk_pwr, self.homeTeam.morale)
                                    away_Gk_dice = dice(self.awayTeam.gk_pwr, self.awayTeam.morale)
                                    home_Atk = home_Atk_dice[2]
                                    away_Gk = away_Gk_dice[2]
                                    
                                    if foul_home == False:
                                        print(self.homeTeam.name + ' got a player in front of the goal!!\n')
                                        timeslp(1/game_spd)
                                    else:
                                        home_Atk *= 1.05
                                    print(self.homeTeam.name + ' shooots the ball!!!!\n')
                                    timeslp(1/game_spd)    
                                    print('Will the goalkeeper catch it!?\n')
                                    timeslp(2/game_spd)
                                    if offside == True and offside_chance > 8:
                                        print('The assistant raises the flag!!\n')
                                        timeslp(1/game_spd)
                                        print('It is offside...!\n')
                                        timeslp(2/game_spd)
                                        home_Atk = -10
                                    

                                    if self.debug:
                                        print('away_Gk, home_Atk\n')
                                        print(away_Gk, home_Atk)
                                        print('')

                                    if home_Atk < 0:
                                        print(self.awayTeam.name + ' restarts the game!\n')
                                        timeslp(3/game_spd)
                                        rebound = False

                                    elif away_Gk < home_Atk: #GoalKeeper fails!
                                        
                                        print('GOOOOAAALL!!!!')
                                        timeslp(1/game_spd)
                                        print(self.homeTeam.name + ' scoooooooreeeessss!!!!\n')
                                        timeslp(1/game_spd)
                                        print(self.homeTeam.name + ' that was an indefensable shot!\n')
                                        timeslp(3/game_spd)
                                        var = randrange(10)+1
                                        if var > 7:
                                          print('Ohhh....!\n')
                                          timeslp(1/game_spd)
                                          print('The assistant raised the flag!!\n')
                                          print('The referee is checking the video!!\n')
                                          timeslp(5/game_spd)
                                          if offside == False:
                                              print(self.homeTeam.name + ' That is a GOAL!!!\n')
                                              timeslp(3/game_spd)
                                              print(self.awayTeam.name + "'s defense can't believe it!!!\n")
                                              timeslp(3/game_spd)

                                        if offside == True:
                                          print('What a shame! NO GOAL!!\n')
                                          timeslp(1/game_spd)
                                          print(self.homeTeam.name + "'s players are very frustrated!!\n")
                                          print(self.homeTeam.name + " That was an offside!\n")
                                          timeslp(1/game_spd)
                                          rebound = False
                                        else:
                                          
                                          print(self.homeTeam.name + ' the ball is in the mildfield again!\n')
                                          timeslp(1/game_spd)
                                          print('The match restarts!\n')
                                          Score_HT += 1
                                          if self.debug:
                                              print('Home team Morale Boost = 0.002')
                                              print('')
                                          self.homeTeam.morale += 0.002
                                          timeslp(3/game_spd)
                                        rebound = False
                                    
                                    
                                    else: #GK catches/punch the ball
                                        if self.debug:
                                            print('Home team Morale Down = 0.001')
                                            print('')
                                        self.homeTeam.morale -= 0.001
                                            
                                        
                                        if away_Gk_dice[0] <= 25: #GK punches the ball
                                            print(self.awayTeam.name + "'S GOAL KEEPER PUNCHES IT!!!\n")
                                            timeslp(1/game_spd)
                                            
                                            if away_Gk - home_Atk <= 10: #Two-times defense!
                                                print("And now he catches it! A two-times defense!!!!\n")
                                                timeslp(1/game_spd)
                                                rebound = False
                                                counteratk = randrange(10)+1
                                                if counteratk > 9:
                                                    counter_away = True
                                            elif offside == True:
                                                print('The assistant raises the flag!\n')
                                                timeslp(1/game_spd)
                                                print('The player was totally out of position!\n')
                                                rebound = False

                                        
                                            else: #Ball is loose inside the area
                                                print('The ball is inside the goal area!!!')
                                                timeslp(1/game_spd)
                                                print(self.homeTeam.name + " WILL REACH THE BALL AND PUSH IT INSIDE THE GOAL!!!\n")
                                                inside_area = True
                                                timeslp(1/game_spd)
                                                new_rb = True
                                    
                                        else:
                                            print('NO!! HE CATCHES IT!!!')
                                            timeslp(1/game_spd)
                                            print('WHAT A CATCH! Unbelivable!!!')
                                            timeslp(1/game_spd)
                                            rebound = False
                                            counteratk = randrange(10)+1
                                            if counteratk > 8:
                                                counter_away = True
                                    
                                else: #Defenders stops the play!
                                    rebound = False
                                    if new_rb == False:
                                        if self.debug:
                                            print('Home team Morale Down = 0.001')
                                            print('')
                                        self.homeTeam.morale -= 0.001
                                        print(self.homeTeam.name + ' ohh no! They lost the ball!!\n')
                                        timeslp(1/game_spd)
                                        print(self.awayTeam.name + ' the defense is strong like a wall!\n')
                                        timeslp(2/game_spd)    
                                        print(self.awayTeam.name + ' tries to push the game forward!\n')
                                        timeslp(1/game_spd)
                                        counteratk = randrange(10)+1
                                        if counteratk > 6:
                                            counter_away = True
                                    else:
                                        new_rb = False
                                        if self.debug:
                                            print('Home team Morale Down = 0.005')
                                            print('')
                                        self.homeTeam.morale -= 0.005
                                        print(self.awayTeam.name + ' WOW! They managed to save the goal!!!!\n')
                                        timeslp(1/game_spd)
                                        print(self.awayTeam.name + ' What a great save!!!\n')
                                        timeslp(2/game_spd)    
                                        print(self.awayTeam.name + ' tries to push the game forward!\n')
                                        timeslp(1/game_spd)
                                        counteratk = randrange(10)+1
                                        if counteratk > 2:
                                            counter_away = True
                                
                        else: #Mildfielders couldn't find the attack
                            if self.debug:
                                print('Home team Morale Down = 0.001')
                                print('')
                            self.homeTeam.morale -= 0.001
                        
                            print(self.homeTeam.name + ' struggles to start a play...\n')
                            timeslp(1/game_spd)
                            print(self.awayTeam.name + ' now has the ball possession...\n')
                            timeslp(3/game_spd)
                            counteratk = randrange(10)+1
                            if counteratk > 7:
                                counter_away = True
                            
                    #checks Away Team atk

                    if home_Mdf < away_Mdf or counter_away: #Home team is preparing a play
                        if self.debug:
                            print('Away team Morale Boost = 0.001')
                            print('')
                        self.awayTeam.morale += 0.001
                        
                        if counter_away:
                            counter_away = False
                            print(self.awayTeam.name +' are running in a counter attack!\n')
                            timeslp(2/game_spd)
                            
                        print(self.awayTeam.name + ' have the ball possession...\n')
                        timeslp(1/game_spd)
                        print(self.awayTeam.name + ' are passing the ball in the mildfield...\n')
                        timeslp(2/game_spd)    
                        print(self.awayTeam.name + ' does a great pass forward!\n')
                        timeslp(2/game_spd)                
                        print(self.awayTeam.name + ' are trying to find a breach in the defense...\n')
                        timeslp(2/game_spd) 
                        
                        away_Atk_dice = dice(self.awayTeam.atk_pwr, self.awayTeam.morale)
                        home_Def_dice = dice(self.homeTeam.atk_pwr, self.homeTeam.morale)
                        away_Atk = away_Atk_dice[2]
                        home_Def = home_Def_dice[2]
                        
                        if self.debug:
                            print('away_Atk, home_Def')
                            print(away_Atk, home_Def)
                            print('')
                        
                            
                            
                        if away_Atk > home_Def: #Attackers are preparing the play
                            
                            if self.debug:
                                print('Away team Morale Boost = 0.001')
                                print('')
                            self.awayTeam.morale += 0.001
                            
                            print(self.awayTeam.name + ' just found the breach! What a pass!\n')
                            timeslp(1/game_spd)   
                            
                            penalty_away = False
                            inside_area = False
                            rebound = True
                            new_rb = False
                            foul_away = False
                            while rebound:
                                away_Atk_dice = dice(self.awayTeam.atk_pwr, self.awayTeam.morale)
                                home_Def_dice = dice(self.homeTeam.atk_pwr, self.homeTeam.morale)
                                away_Atk = away_Atk_dice[2]
                                home_Def = home_Def_dice[2]
                                foul_test = randrange(100)+1
                                
                                if self.debug:
                                    print('away_Atk, home_Def')
                                    print(away_Atk, home_Def)
                                    print('')
                                    print('foul_chance_away, foul_test')
                                    print(foul_chance_home, foul_test)
                                
                                if foul_chance_home - foul_test > 25: #HARD FOUL HAPPEN!
                                    print(self.homeTeam.name + "'s defense player tackle the ofense!!\n")
                                    timeslp(1/game_spd)
                                    print('FOUL! What an agressive impact!!\n')
                                    timeslp(3/game_spd)
                                    if inside_area == True:
                                      print(self.awayTeam.name + ' PENALTY KICK!!!!')
                                      timeslp(3/game_spd)
                                      penalty_away = True
                                    else:
                                      print(self.awayTeam.name + " That's a good oportunity for a goal!!")
                                      foul_away = True
                                
                                elif foul_chance_home - foul_test > 10: #SOFT FOUL HAPPEN
                                    print(self.homeTeam.name + "'s defense player grabbed the offense player by the shirt!!\n")
                                    timeslp(1/game_spd)
                                    print(self.homeTeam.name + " what a silly foul!\n")
                                    timeslp(4/game_spd)
                                    if inside_area == True:
                                      print(self.awayTeam.name + ' PENALTY KICK!!!!')
                                      timeslp(3/game_spd)
                                      penalty_away = True
                                    else:
                                      foul_away = True
                                
                                if penalty_away:
                                  print(self.awayTeam.name + ' prepares the ball in the penalty mark...\n')
                                  timeslp(5/game_spd)
                                  print(self.awayTeam.name + ' looks to the goal...\n')
                                  timeslp(4/game_spd)
                                  print('Referee authorizes the kick!\n')
                                  timeslp(3/game_spd)
                                  penal = randrange(10) + 1
                                  if penal > 5:
                                    print(self.awayTeam.name + ' SCOORESS!!!\n')
                                    timeslp(1/game_spd)
                                    print(self.awayTeam.name + ' No chance for the Keeper!!\n')
                                    timeslp(1/game_spd)
                                    Score_AT += 1
                                    if self.debug:
                                        print('Away team Morale Boost = 0.002')
                                        print('')
                                    self.awayTeam.morale += 0.002
                                  else:
                                    print(self.awayTeam.name + ' OH NO!!! THE KEEPER CAUGHT THE BALL!!!!\n')
                                    timeslp(3/game_spd)
                                    print(self.awayTeam.name + "'s players are desolated!!!\n") 
                                    timeslp(2/game_spd)

                                    if self.debug:
                                        print('Away team Morale Down = 0.002')
                                        print('')
                                    self.awayTeam.morale -= 0.002

                                  break

                                if foul_away == True:
                                    pass_or_shoot = randrange(10)+1
                                    if pass_or_shoot > 4: #BALL INSIDE THE AREA
                                        print(self.awayTeam.name + " Long ball inside the area!!\n")
                                        foul_away = False
                                        timeslp(2/game_spd)
                                        away_Atk_dice = dice(self.awayTeam.atk_pwr, self.awayTeam.morale)
                                        home_Def_dice = dice(self.homeTeam.atk_pwr, self.homeTeam.morale)
                                        away_Atk = away_Atk_dice[2]
                                        home_Def = home_Def_dice[2]
                                    else:
                                        away_Atk = home_Def + 1
                                    
                                    
                                if away_Atk > home_Def: #Defender could not stop the play
                                    
                                    offside = False
                                    offside_chance = randrange(10)+1
                                    if self.homeTeam.tactics == 'Defensive':
                                        if offside_chance > 3:
                                            offside = True
                                    elif self.homeTeam.tactics == 'Offensive':
                                        if offside_chance > 8:
                                            offside = True
                                    else:
                                        if offside_chance > 6:
                                            offside = True

                                    away_Atk_dice = dice(self.awayTeam.atk_pwr, self.awayTeam.morale)
                                    home_Gk_dice = dice(self.homeTeam.gk_pwr, self.homeTeam.morale)
                                    away_Atk = away_Atk_dice[2]
                                    home_Gk = home_Gk_dice[2]
                                    
                                    if foul_away == False:
                                        print(self.awayTeam.name + ' got a player in front of the goal!!\n')
                                        timeslp(1/game_spd)
                                    else:
                                        away_Atk *= 1.1
                                    print(self.awayTeam.name + ' shooots the ball!!!!\n')
                                    timeslp(1/game_spd)    
                                    print('Will the goalkeeper catch it!?\n')
                                    timeslp(2/game_spd)
                                    if offside == True and offside_chance > 8:
                                        print('The assistant raises the flag!!\n')
                                        timeslp(1/game_spd)
                                        print('It is offside...!\n')
                                        timeslp(2/game_spd)
                                        away_Atk = -10
                                    

                                    if self.debug:
                                        print('home_Gk, away_Atk\n')
                                        print(home_Gk, away_Atk)
                                        print('')

                                    if away_Atk < 0:
                                        print(self.homeTeam.name + ' restarts the game!\n')
                                        timeslp(3/game_spd) 
                                        rebound = False   
                                    elif home_Gk < away_Atk: #GoalKeeper fails!
                                        
                                            
                                        self.awayTeam.morale += 0.002
                                        print('GOOOOAAALL!!!!')
                                        timeslp(1/game_spd)
                                        print(self.awayTeam.name + ' scoooooooreeeessss!!!!\n')
                                        timeslp(1/game_spd)
                                        print(self.awayTeam.name + ' that was an indefensable shot!\n')
                                        timeslp(3/game_spd)
                                        var = randrange(10)+1
                                        if var > 7:
                                          print('Ohhh....!\n')
                                          timeslp(1/game_spd)
                                          print('The assistant raised the flag!!\n')
                                          print('The referee is checking the video!!\n')
                                          timeslp(5/game_spd)
                                          if offside == False:
                                              print(self.awayTeam.name + ' That is a GOAL!!!\n')
                                              timeslp(3/game_spd)
                                              print(self.homeTeam.name + "'s defense can't believe it!!!\n")
                                              timeslp(3/game_spd)
                                        if offside == True:
                                          print('What a shame! NO GOAL!!\n')
                                          timeslp(1/game_spd)
                                          print(self.awayTeam.name + "'s players are very frustrated!!\n")
                                          print(self.awayTeam.name + " That was an offside!\n")
                                          timeslp(1/game_spd)
                                          rebound = False
                                        else:
                                          Score_AT += 1
                                          if self.debug:
                                            print('Away team Morale Boost = 0.002')
                                            print('')
                                          print(self.awayTeam.name + ' the ball is in the mildfield again!\n')
                                          timeslp(1/game_spd)
                                          print('The match restarts!\n')
                                          timeslp(3/game_spd)
                                          rebound = False
                                    else: #GK catches/punch the ball
                                        if self.debug:
                                            print('Away team Morale Down = 0.001')
                                            self.awayTeam.morale -= 0.001
                                            print('')
                                        
                                        if home_Gk_dice[0] <= 25: #GK punches the ball
                                            print(self.homeTeam.name + "'S GOAL KEEPER PUNCHES IT!!!\n")
                                            timeslp(1/game_spd)
                                            
                                            if home_Gk - away_Atk <= 10: #Two-times defense!
                                                print("And now he catches it! A two-times defense!!!!\n")
                                                timeslp(1/game_spd)
                                                rebound = False
                                                counteratk = randrange(10) +1
                                                if counteratk > 9:
                                                    counter_home = True
                                            elif offside == True:
                                                print('The assistant raises the flag!\n')
                                                timeslp(1/game_spd)
                                                print('The player was totally out of position!\n')
                                                rebound = False
                                                
                                                
                                        
                                            else: #Ball is loose inside the area
                                                print('The ball is inside the goal area!!!')
                                                timeslp(1/game_spd)
                                                print(self.awayTeam.name + " WILL REACH THE BALL AND PUSH IT INSIDE THE GOAL!!!\n")
                                                inside_area = True
                                                timeslp(1/game_spd)
                                                new_rb = True
                                    
                                        else:
                                            print('NO!! HE CATCHES IT!!!')
                                            timeslp(1/game_spd)
                                            print('WHAT A CATCH! Unbelivable!!!')
                                            timeslp(1/game_spd)
                                            rebound = False
                                            counteratk = randrange(10)+1
                                            if counteratk > 8:
                                                counter_home = True
                                    
                                else: #Defenders stops the play!
                                    rebound = False
                                    if new_rb == False:
                                        if self.debug:
                                            print('Away team Morale Down = 0.001')
                                            print('')
                                            
                                        self.awayTeam.morale -= 0.001
                                        print(self.awayTeam.name + ' ohh no! They lost the ball!!\n')
                                        timeslp(1/game_spd)
                                        print(self.homeTeam.name + ' the defense is strong like a wall!\n')
                                        timeslp(2/game_spd)    
                                        print(self.homeTeam.name + ' tries to push the game forward!\n')
                                        timeslp(1/game_spd)
                                        counteratk = randrange(10)+1
                                        if counteratk > 6:
                                            counter_home = True
                                    else:
                                        new_rb = False
                                        if self.debug:
                                            print('Away team Morale Down = 0.005')
                                            print('')
                                        self.awayTeam.morale -= 0.005
                                
                                        print(self.homeTeam.name + ' WOW! They managed to save the goal!!!!\n')
                                        timeslp(1/game_spd)
                                        print(self.homeTeam.name + ' What a great save!!!\n')
                                        timeslp(2/game_spd)    
                                        print(self.homeTeam.name + ' tries to push the game forward!\n')
                                        timeslp(1/game_spd)
                                        counteratk = randrange(10)+1
                                        if counteratk > 2:
                                            counter_home = True
                        else: #Mildfielders couldn't find the attack
                            if self.debug:
                                print('Away team Morale Down = 0.001')
                                print('')
                            self.awayTeam.morale -= 0.001
                                
                            print(self.awayTeam.name + ' struggles to start a play...\n')
                            timeslp(1/game_spd)
                            print(self.homeTeam.name + ' now has the ball possession...\n')
                            timeslp(3/game_spd)    
                            counteratk = randrange(10)+1
                            if counteratk > 7:
                                counter_home = True
                
            
            if j == 0:
                print('Okay, That is the end of the first half!\n')
                j += 1
                input('Press enter to continue')
            else:
                print('Well, that is it! The end of the game!\n')
                timeslp(3)
                break
        if Score_AT == Score_HT:
            print('Tonight we had a Tie! The teams must reflect about their decisions in this game!\n')
            self.homeTeam.tie += 1
            self.awayTeam.tie += 1
        elif Score_AT > Score_HT:
            print('Wow! '+ self.homeTeam.name + ' could not win the visitors! What a sad day!\n')
            
            if self.debug:
                print('Away team Morale Boost = 0.05')
                print('Home team Morale Down = 0.05')
              
            if self.homeTeam.tactics == 'Offensive':
              self.homeTeam.morale -= 0.01
            if self.awayTeam.tactics == 'Offensive':
              self.awayTeam.morale += 0.01
            if self.awayTeam.tactics == 'Defensive':
              self.awayTeam.morale += 0.02
              self.homeTeam.morale -= 0.01
            self.homeTeam.morale -= 0.05
            self.awayTeam.morale += 0.05
            self.homeTeam.lose += 1
            self.awayTeam.win += 1
        else:
            self.homeTeam.win += 1
            self.awayTeam.lose += 1
            print('We could not think otherwise! '+ self.homeTeam.name + ' won the match! The stadium shouts in celebration!!\n')
            if self.debug:
                print('Home team Morale Boost = 0.025')
                print('')
                print('Away team Morale Down = 0.025')
                print('')
            if self.homeTeam.tactics == 'Defensive':
              self.awayTeam.morale -= 0.02
              self.homeTeam.morale += 0.02
            if self.awayTeam.tactics == 'Offensive':
              self.awayTeam.morale -= 0.02
            self.homeTeam.morale += 0.025
            self.awayTeam.morale -= 0.025