# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:06:15 2019

@author: Ramon Barros
@github: https://github.com/rmlz
"""
from random import randrange, shuffle

def create_balanced_round_robin(players):
    """ Create a schedule for the players in the list and return it"""
    s = []
    if len(players) % 2 == 1: players = players + [None]
    # manipulate map (array of indexes for list) instead of list itself
    # this takes advantage of even/odd indexes to determine home vs. away
    n = len(players)
    map = list(range(n))
    mid = n // 2
    for i in range(n-1):
        l1 = map[:mid]
        l2 = map[mid:]
        l2.reverse()
        round = []
        for j in range(mid):
            t1 = players[l1[j]]
            t2 = players[l2[j]]
            if j == 0 and i % 2 == 1:
                # flip the first match only, every other round
                # (this is because the first match always involves the last player in the list)
                round.append((t2, t1))
            else:
                round.append((t1, t2))
        s.append(round)
        # rotate list by n/2, leaving last element at the end
        map = map[mid:-1] + map[:mid] + map[-1:]
    return s

def average(arr):
    avg = 0
    for item in arr:
        avg += int(item[1])
    avg = avg/len(arr)
    
    return avg

def dice(mod, morale, d=50):
    dice = randrange(d)+1
    if dice <= 3:
        mod = 0
    elif dice >= 45:
        mod = mod*2
            
    return (dice, mod, dice + (mod * morale))