#! /usr/bin/env python3
# https://projecteuler.net/problem=54

from __future__ import print_function
from cardlib import Card, Hand
from collections import Counter
from pokerlib import getHandRankFunc, handrankfuncs
from utillib import values

def buildhands(line):
    """
    Builds the 2 players hands from each line in the file. Returns 2 Hand objects.
    """
    player1list = line.split(' ')[:5]
    player2list = line.split(' ')[5:]

    for c in player1list:
        card = Card(c[0], c[1])
        player1list[player1list.index(c)] = card
    
    player1hand = Hand(*player1list)
        
    for c in player2list:
        card = Card(c[0], c[1])
        player2list[player2list.index(c)] = card
    
    player2hand = Hand(*player2list)

    return player1hand, player2hand

def comparehands(hand1, hand2):
    player1func, player1val = getHandRankFunc(hand1)
    player2func, player2val = getHandRankFunc(hand2)

    if player1func < player2func:
        return True
    elif player1func > player2func:
        return False
    else:
        player1index = values.index(player1val[0])
        player2index = values.index(player2val[0])
        if player1index > player2index:
            return True
        elif player1index < player2index:
            return False
        else:
            return None

def testercomparehands(hand1, hand2):
    player1func, player1val = getHandRankFunc(hand1)
    player2func, player2val = getHandRankFunc(hand2)
    totalhandcount[player1func] += 1
    totalhandcount[player2func] += 1
    player1total[player1func] += 1
    player2total[player2func] += 1

    if player1func < player2func:
        return True, player1func
    elif player1func > player2func:
        return False, player2func
    else:
        player1index = values.index(player1val[0])
        player2index = values.index(player2val[0])
        if player1index > player2index:
            return True, player1func
        elif player1index < player2index:
            return False, player2func
        else:
            return None, -1

def testerline(line):
    player1ct = 0
    player1dict = Counter()
    player2ct = 0
    player2dict = Counter()
    tie = 0
    player1, player2 = buildhands(line)
    res, func = testercomparehands(player1,player2)
    name = handrankfuncs[func].__name__

    if res == True:
        player1ct += 1
        player1dict[name] += 1
    elif res == False:
        player2ct += 1
        player2dict[name] += 1
    else:
        tie += 1
    print("player1ct: %s\nplayer2dict: %s\nplayer2ct: %s\nplayer2dict: %s\ntie: %s" % (player1ct, player1dict, player2ct, player2dict, tie))

def testermain():
    file = open('p054_poker.txt')
    line = ''
    player1ct = 0
    player2ct = 0
    tie = 0
    handcount = Counter()
    player1dict = Counter()
    player2dict = Counter()

    while True:
        line = file.readline().rstrip()
        if not line: break
        player1, player2 = buildhands(line)
        res, func = testercomparehands(player1,player2)
        name = handrankfuncs[func].__name__

        handcount[name] += 1

        if res == True:
            player1ct += 1
            player1dict[name] += 1
        elif res == False:
            player2ct += 1
            player2dict[name] += 1
        else:
            tie += 1
        
    print("player1ct: %s\nplayer2ct: %s\ntotalhandcount: %s\nplayer1total: %s\nplayer2total: %s\nhandcount: %s\nplayer1dict: %s\nplayer2dict: %s" % 
        (player1ct, player2ct, totalhandcount, player1total, player2total, handcount, player1dict, player2dict))

def main():
    file = open('p054_poker.txt')
    line = ''
    player1ct = 0
    player2ct = 0
    tie = 0
    while True:
        line = file.readline().rstrip()
        if not line: break
        player1, player2 = buildhands(line)
        res = comparehands(player1,player2)
        if res == True:
            player1ct += 1
        elif res == False:
            player2ct += 1
        else:
            tie += 1
    print("player1ct: %s\nplayer2ct: %s\ntie: %s" % (player1ct, player2ct, tie)) 

if __name__ == '__main__':
    #totalhandcount = Counter()
    #player1total = Counter()
    #player2total = Counter()
    #line1 = 'KH QH JH TH AD KD QD JD TC 9H' # 2 straights
    #line2 = 'KH KD KS TH TD QH QD QS TC TS' # 2 full houses
    #line3 = '2H 2D 5H 5D 6S 8D 8C 4H 4S JD' # 2 2-pairs
    #line4 = 'KH QH JH TH AD KD QD JD TC AH' # 2 straights that tie
    #hand1, hand2 = buildhands(line4)
    #print(testercomparehands(hand1, hand2))
    #testermain()
    main()