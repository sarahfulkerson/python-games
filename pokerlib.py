#! /usr/bin/env python
"""
https://projecteuler.net/problem=54

Library of functions to enable comparing poker hands.
"""

from __future__ import print_function
from collections import Counter
from utillib import values, sortedOnIndex, sortMultipleLists, _valueMethodCustomizer

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
        return res, hand.getHighCard()
    else:
        return res, None

def isStraightFlush(hand):
    """
    Returns True if the passed in Hand is a straight flush and False if it is not.
    """
    # royal flush trumps straight flush
    if isRoyalFlush(hand) != False:
        return False, None

    handvalues = sortedOnIndex(hand.getValues(), values)
    handsuits = hand.getSuits(distinctsuits=True)

    # flush logic - there should only be 1 suit in the hand
    if len(handsuits) != 1:
        return False, None            # the straight flush should have only 1 suit in the hand

    # straight logic - break out of the loop if a straight is found and return straightflush
    for s in range(len(values)-len(handvalues)+1):
        st = values[s:s+len(handvalues)]
        if st == handvalues:
            return True, hand.getHighCard()    # the hand is indeed both a straight and a flush so return True
    
    return False, None # if the loop completes without returning then a straight was not found so return False

def isFourOfAKind(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is four of a kind and false if 
    it is not. The second value in the list will be the value of
    the four of a kind, or None if the Hand is not four of a kind.
    """
    fourofakind = countOfValues(hand)
    return _valueMethodCustomizer(fourofakind,'!=', 2, 4)

def isFullHouse(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is a full house and false if it 
    is not. The second value in the list will be the value of the 
    three of a kind in the full house, or None if the Hand is not 
    a full house.
    """
    fullhouse = countOfValues(hand)
    return _valueMethodCustomizer(fullhouse, '!=', 2, 3)

def isFlush(hand):
    """
    Returns True if the passed in Hand is a flush and false if it is not.
    """
    # royal flush and straight flush trumps flush
    if isRoyalFlush(hand) != False or isStraightFlush(hand) != False:
        return False, None

    handsuits = hand.getSuits(distinctsuits=True)
    if len(handsuits) == 1:
        return True, hand.getHighCard()
    
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

def getHandRankName(hand):
    for rank in handrankfuncs:
        if rank(hand) != False:
            return rank.__name__
    return None

def getHandRankFunc(hand):
    for rank in handrankfuncs:
        res, val = rank(hand)
        print(rank.__name__, res, val)
        #if rank(hand) != False:
        #    return rank
    return None

if __name__ == '__main__':
    from cardlib import Card, Hand
    s = '5H KS 9C 7D 9H 8D 3S 5D 5C AH'
    hand1 = Hand(Card('5', 'h'), Card('6', 's'), Card('7', 'c'), Card('8', 'd'), Card('9', 'h'))
    hand2 = Hand(Card('8', 'd'), Card('3', 's'), Card('5', 'd'), Card('5', 'c'), Card('a', 'h'))
    hand3 = Hand(Card('8', 'd'), Card('3', 's'), Card('5', 'd'), Card('4', 'c'), Card('a', 'h'))
    for rank in handrankfuncs[5:]:
        print(rank.__name__, rank(hand1))