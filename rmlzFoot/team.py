# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:06:15 2019

@author: Ramon Barros
@github: https://github.com/rmlz
"""
from random import randrange, shuffle

class team:
    def __init__(self, name, power):
    
        self.name = name
        self.power = power
        self.morale = float(1)
        self.win = 0
        self.lose = 0
        self.tie = 0
        self.tactics = 'Balanced'
        self.player = False
        while True:
            try:
                self.power = int(self.power)
                if self.power < 0:
                    self.power = self.power * -1
                elif self.power < 10 and self.power >= 0:
                    self.power = 10
                elif self.power > 30:
                    self.power = 30
                break
            except ValueError:
                print('\n' + str(self.power) + ' is not an integral number')
        
        self.players = []
        for i in range(11):
            if i == 0:
                self.players.append(('Player' + str(i+1), randrange(self.power+15, self.power+35)))
            else:
                self.players.append(('Player' + str(i+1), randrange(self.power-5, self.power+5)))