#! /usr/bin/env python3
# https://projecteuler.net/problem=54

import pokerlib

def main():

    player1 = ['4H', '7H', '8H', '9H', 'TH']
    player2 = ['2C', '3S', '8S', '8D', 'TD']

    player1hand = list(whatsinhand(player1))
    #player2hand = whatsinhand(player2)

    print('%s' % player1hand)
    #print('%s' % player2hand)
    #print('%s\n%s' % (player1hand, player2hand))

def whatsinhand(h):
    hand = sorted(h[:])
    handvaluesct, handsuitsct, handvalues, handsuits = processhand(hand)
    rank = ''
    highcard = hand[-1]

    # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    if hand in pokerlib.royalflush:
        rank = 'Royal Flush, %s' % pokerlib.suits[hand[0][1]]
        return rank, highcard
    elif len(handsuitsct) == 1:
        # Straight Flush: All cards are consecutive values of same suit.
        if sorted(handvalues) in pokerlib.straight:
            rank = 'Straight Flush, %s' % pokerlib.suits[hand[0][1]]
            return rank, highcard 
        # Flush: All cards of the same suit.
        else:
            rank = 'Flush, %s' % pokerlib.suits[hand[0][1]]
            return rank, highcard 
    elif len(handvaluesct) == 2:
        # Four of a Kind
        if 4 in handvaluesct.values():
            hvc = list(handvaluesct.items())
            for h 
            pass#rank = 'Four of a Kind, %s' % handvaluesct.index(4)

def processhand(hand):
    valuesct = {}
    suitsct = {}
    values = []
    suits = []

    for h in hand:
        if h[0] not in valuesct:
            valuesct[h[0]] = 1
        else:
            valuesct[h[0]] += 1
        if h[1] not in suitsct:
            suitsct[h[1]] = 1
        else:
            suitsct[h[1]] += 1
        values.append(h[0])
        suits.append(h[1])
    return valuesct, suitsct, values, suits

main()