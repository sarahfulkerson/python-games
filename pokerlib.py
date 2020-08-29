#! /usr/bin/env python3
"""
https://projecteuler.net/problem=54

Library of functions to enable comparing poker hands.
"""

from utillib import values, sortedOnIndex, _valueMethodCustomizer

def countOfValues(hand):
    carddict = {}
    res = {}
    # make a dictionary of suits in the Hand, and make the values of the keys the set of Card values in those suits
    for card in hand:
        s = card.getSuit()
        if carddict.get(s) == None:
            carddict[s] = {card.getValue()}
        else:
            carddict[s].add(card.getValue())

    # count the number of times a particular value appears in the hand
    for suit in carddict:
        for value in carddict[suit]:
            if res.get(value) == None:
                res[value] = 1
            else:
                res[value] += 1

    return res

def isRoyalFlush(hand):
    """Returns True if the passed in Hand is a royal flush."""
    handvalues = sortedOnIndex(hand.getValues(), values)
    royalflushvalues = values[-5:]
    return handvalues == royalflushvalues and len(hand.getSuits(distinctsuits=True)) == 1

def isStraightFlush(hand):
    """
    Returns True if the passed in Hand is a straight flush and False if it is not.
    """
    # royal flush trumps straight flush
    if isRoyalFlush(hand) == True:
        return False

    handvalues = sortedOnIndex(hand.getValues(), values)
    handsuits = hand.getSuits(distinctsuits=True)

    # flush logic - there should only be 1 suit in the hand
    if len(handsuits) != 1:
        return False            # the straight flush should have only 1 suit in the hand

    # straight logic - break out of the loop if a straight is found and return straightflush
    for s in range(len(values)-len(handvalues)+1):
        st = values[s:s+len(handvalues)]
        if st == handvalues:
            return True    # the hand is indeed both a straight and a flush so return True
    
    return False # if the loop completes without returning then a straight was not found so return False

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
    if isRoyalFlush(hand) == True or isStraightFlush(hand) == True:
        return False

    handsuits = hand.getSuits(distinctsuits=True)
    if len(handsuits) == 1:
        return True
    
    return False

def isStraight(hand):
    """
    Returns True if the passed in Hand is a straight and false if it is not.
    """
    # royal flush and straight flush trumps straight
    if isRoyalFlush(hand) == True or isStraightFlush(hand) == True:
        return False

    handvalues = sortedOnIndex(hand.getValues(), values)
    straight = []
    # take a slice of the list the same length as the Hand and see if the values match
    for s in range(len(values)-len(handvalues)+1):
        straight = values[s:s+len(handvalues)]
        if straight == handvalues:
            return True
    
    return False

def isThreeOfAKind(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is three of a kind and false if 
    it is not. The second value in the list will be the value of
    the three of a kind, or None if the Hand is not three of a kind.
    """
    # full house trumps three of a kind, so if the hand is a full house then this function should not continue to run
    if type(isFullHouse(hand)) == list:
        return False

    threeofakind = countOfValues(hand)
    return _valueMethodCustomizer(threeofakind, '<', 3, 3)

def isTwoPairs(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is two pairs and false if it is 
    not. The second value in the list will be a list containing the 
    values of the two pairs, or None if the Hand is not two pairs.
    """
    
    twopairs = countOfValues(hand)
    return _valueMethodCustomizer(twopairs, '!=', 3, 2, appendon=True)

def isOnePair(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is a pair and false if it is not. 
    The second value in the list will be a list containing the value
    of the pair, or None if the Hand is not a  pair.
    """
    # two pairs and full house trumps one pair, so if the hand is not one pair then this function should not continue to run
    if type(isTwoPairs(hand)) == list or type(isFullHouse(hand)) == list:
        return False
    
    onepair = countOfValues(hand)
    return _valueMethodCustomizer(onepair, '<', 2, 2)

def isHighCard(hand):
    """
    Returns True if the passed in Hand is a high card only hand and False if it is not.
    """
    # everything else trumps this hand
    if isRoyalFlush(hand) == True or isStraightFlush(hand) == True or type(isFourOfAKind(hand)) == list or type(isFullHouse(hand)) == list or isFlush(hand) == True or isStraight(hand) == True or type(isThreeOfAKind(hand)) == list or type(isTwoPairs(hand)) == list or type(isTwoPairs(hand)) == list or type(isOnePair(hand)) == list:
        return False
    
    return True

handrankfuncs = [isHighCard, isOnePair, isTwoPairs, isThreeOfAKind, isStraight, isFlush, isFullHouse, isFourOfAKind, isStraightFlush, isRoyalFlush]

def getHandRank(hand):
    for rank in handrankfuncs:
        if rank(hand) != False:
            return rank.__name__
    return None
    

if __name__ == '__main__':
    from cardlib import Card, Hand
    hand1 = Hand(Card('a', 'd'), Card('k', 'd'), Card('q', 'd'), Card('j', 'd'), Card('t', 'd'))
    hand2 = Hand(Card('a', 'c'), Card('k', 'd'), Card('q', 'c'), Card('j', 'c'), Card('2', 'c'))
    print("hand1: %s" % getHandRank(hand1))
    print("hand2: %s" % getHandRank(hand2))