#! /usr/bin/env python
"""
https://projecteuler.net/problem=54

Library of functions to enable comparing poker hands.
"""

from __future__ import print_function
from collections import Counter
from utillib import values, sortedOnIndex, sortMultipleLists

def countOfValues(hand):
    vals = hand.getValues(distinctvalues=True)
    counts = []

    for val in vals:
        i = 0
        for card in hand:
            if card.getValue() == val: i += 1
        counts.append(i)
    sortMultipleLists(counts,vals)
    counts.reverse(); vals.reverse()
    return counts, vals
def isRoyalFlush(hand):
    """Returns True if the passed in Hand is a royal flush."""
    handvalues = sortedOnIndex(hand.getValues(), values)
    royalflushvalues = values[-5:]
    res = handvalues == royalflushvalues and len(hand.getSuits(distinctsuits=True)) == 1
    if res == True:
        return res, hand.getHighCard().getValue()
    return res, None
def isStraightFlush(hand):
    """
    Returns True if the passed in Hand is a straight flush and False if it is not.
    """
    if isFlush(hand)[0] == True and isStraight(hand)[0] == True:
        return True, hand.getHighCard().getValue()
    
    return False, None
def isFourOfAKind(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is four of a kind and false if 
    it is not. The second value in the list will be the value of
    the four of a kind, or None if the Hand is not four of a kind.
    """
    counts, vals = countOfValues(hand)
    if counts[0] == 4:
        return True, vals[0]
    return False, None
def isFullHouse(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is a full house and false if it 
    is not. The second value in the list will be the value of the 
    three of a kind in the full house, or None if the Hand is not 
    a full house.
    """
    counts, vals = countOfValues(hand)
    if counts[0] == 3 and counts[1] == 2:
        return True, vals[0]
    return False, None
def isFlush(hand):
    """
    Returns True if the passed in Hand is a flush and false if it is not.
    """
    handsuits = hand.getSuits(distinctsuits=True)
    if len(handsuits) == 1:
        return True, hand.getHighCard().getValue()
    
    return False, None
def isStraight(hand):
    """
    Returns True if the passed in Hand is a straight and false if it is not.
    """
    handvalues = sortedOnIndex(hand.getValues(), values)
    straight = []
    # take a slice of the list the same length as the Hand and see if the values match
    for s in range(len(values)-len(handvalues)+1):
        straight = values[s:s+len(handvalues)]
        if straight == handvalues:
            return True, handvalues[-1]
    
    return False, None
def isThreeOfAKind(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is three of a kind and false if 
    it is not. The second value in the list will be the value of
    the three of a kind, or None if the Hand is not three of a kind.
    """
    counts, vals = countOfValues(hand)
    if len(counts) == 3 and counts[0] == 3:
        return True, vals[:1]
    return False, None
def isTwoPairs(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is two pairs and false if it is 
    not. The second value in the list will be a list containing the 
    values of the two pairs, or None if the Hand is not two pairs.
    """
    counts, vals = countOfValues(hand)
    if len(counts) == 3 and counts[0] != 3:
        return True, vals[:2]
    return False, None
def isOnePair(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is a pair and false if it is not. 
    The second value in the list will be a list containing the value
    of the pair, or None if the Hand is not a  pair.
    """
    counts, vals = countOfValues(hand)
    if len(counts) == 4:
        return True, vals[:1]
    return False, None
def isHighCard(hand):
    """
    Returns True if the passed in Hand is a high card only hand and False if it is not.
    """
    if isStraight(hand) != (False, None): return False, None
    counts, vals = countOfValues(hand)
    if len(counts) == 5 and len(hand.getSuits(distinctsuits=True)) != 1:
        return True, vals[:1]
    return False, None
handrankfuncs = [isRoyalFlush, isStraightFlush, isFourOfAKind, isFullHouse, isFlush, isStraight, isThreeOfAKind, isTwoPairs, isOnePair, isHighCard]
def getHandRankFunc(hand):
    for rank in handrankfuncs:
        res, val = rank(hand)
        if res != False:
            return handrankfuncs.index(rank), val
    return None
if __name__ == '__main__':
    from cardlib import Card, Hand
    s = '5H KS 9C 7D 9H 8D 3S 5D 5C AH'
    hand1 = Hand(Card('5', 'h'), Card('6', 's'), Card('7', 'c'), Card('8', 'd'), Card('9', 'h'))
    hand2 = Hand(Card('8', 'd'), Card('3', 'd'), Card('5', 'd'), Card('4', 'd'), Card('a', 'd'))
    hand3 = Hand(Card('a', 'd'), Card('k', 'd'), Card('q', 'd'), Card('j', 'd'), Card('t', 'd'))
    for rank in handrankfuncs:
        print(rank.__name__, rank(hand3), handrankfuncs.index(rank))
    counts, vals = countOfValues(hand3)
    print(counts, vals)