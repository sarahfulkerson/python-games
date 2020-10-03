#! /usr/bin/env python3
# https://projecteuler.net/problem=54

from __future__ import print_function
from cardlib import Card, Hand
from collections import Counter
from pokerlib import getHandRankFunc, handrankfuncs

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
    player1hand = getHandRankFunc(hand1)
    player2hand = getHandRankFunc(hand2)
    player1index = handrankfuncs.index(player1hand)
    player2index = handrankfuncs.index(player2hand)

    if player1index == player2index:                # if handrank is the same for both hands then check the high cards
        player1highcard = None
        player2highcard = None
        player1res = player1hand(hand1)
        player2res = player2hand(hand2)
        for x in range(1, 6):
            player1highcard = hand1.getHighCard(x*-1)
            player2highcard = hand2.getHighCard(x*-1)
            if player1highcard == player2highcard:      # if high cards are the same in each hand, continue in the loop
                continue
            elif player1highcard > player2highcard:     # else if player1's high card is greater than player2's then return True
                return True
            else:                                       # else return False
                return False
        return None                                     # if both hands have the same values then they are tied, return None
    elif player1index > player2index:               # else if player1's handrank is greater than player2's then return True
        return True
    else:                                           # else return False
        return False
    assert False, 'weird error in compareHands()'

def testercomparehands(hand1, hand2):
    player1hand = getHandRankFunc(hand1)
    player2hand = getHandRankFunc(hand2)
    player1index = handrankfuncs.index(player1hand)
    player2index = handrankfuncs.index(player2hand)
    player1res = player1hand(hand1)
    player2res = player2hand(hand2)
    totalhandcount[player1hand.__name__] += 1
    totalhandcount[player2hand.__name__] += 1
    player1total[player1hand.__name__] += 1
    player2total[player2hand.__name__] += 1

    if player1index == player2index:                # if handrank is the same for both hands then check the high cards
        player1highcard = None
        player2highcard = None
        for x in range(1, 6):
            player1highcard = hand1.getHighCard(x*-1)
            player2highcard = hand2.getHighCard(x*-1)
            if player1highcard == player2highcard:      # if high cards are the same in each hand, continue in the loop
                continue
            elif player1highcard > player2highcard:     # else if player1's high card is greater than player2's then return True
                return True, player1hand
            else:                                       # else return False
                return False, player2hand
        return None, player1hand                        # if both hands have the same values then they are tied, return None
    elif player1index > player2index:               # else if player1's handrank is greater than player2's then return True
        return True, player1hand
    else:                                           # else return False
        return False, player2hand
    assert False, 'weird error in compareHands()'

def testerline(line):
    player1ct = 0
    player1dict = Counter()
    player2ct = 0
    player2dict = Counter()
    tie = 0
    player1, player2 = buildhands(line)
    value, func = testercomparehands(player1,player2)
    func = func.__name__

    if value == True:
        player1ct += 1
        player1dict[func] += 1
    elif value == False:
        player2ct += 1
        player2dict[func] += 1
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

    file2 = open('isOnePair-fixappendon.txt', 'w')
    while True:
        line = file.readline().rstrip()
        if not line: break
        player1, player2 = buildhands(line)
        value, func = testercomparehands(player1,player2)
        func = func.__name__

        handcount[func] += 1

        if value == True:
            player1ct += 1
            player1dict[func] += 1
            if func == 'isOnePair': file2.write('p1: ' + line + '\n')
        elif value == False:
            player2ct += 1
            player2dict[func] += 1
            if func == 'isOnePair': file2.write('p2: ' + line + '\n')
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
        value = comparehands(player1,player2)
        if value == True:
            player1ct += 1
        elif value == False:
            player2ct += 1
        else:
            tie += 1
    print("player1ct: %s\nplayer2ct: %s\ntie: %s" % (player1ct, player2ct, tie)) 

if __name__ == '__main__':
    #TODO fix isOnePair, it is broken
    totalhandcount = Counter()
    player1total = Counter()
    player2total = Counter()
    line = '5H KS 9C 7D 9H 8D 3S 5D 5C AH'
    testerline(line)
    #testermain()
    #main()