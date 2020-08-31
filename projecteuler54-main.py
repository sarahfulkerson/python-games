#! /usr/bin/env python3
# https://projecteuler.net/problem=54

from cardlib import Card, Hand
from pokerlib import getHandRank, handrankfuncs

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
    player1hand = getHandRank(hand1)
    player2hand = getHandRank(hand2)
    print(repr(player1hand), repr(player2hand))

    if player1hand == player2hand:
        player1highcard = hand1.getHighCard()
        player2highcard = hand2.getHighCard()
        if player1highcard == player2highcard:
            return None
        elif player1highcard > player2highcard:
            return True
        else:
            return False
    else:
        #TODO
        pass

def main():
    file = open('p054_poker.txt')
    line = ''
    player1ct = 0
    player2ct = 0
    tie = 0
    for i in range(2):
        line = file.readline()
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
    line = '8C TS KC 9H 4S 7D 2S 5D 3S AC'
    main()