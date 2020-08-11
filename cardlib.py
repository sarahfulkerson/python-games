#! /usr/bin/env python3
# https://projecteuler.net/problem=54

# TODO: abstract base classes!
from utillib import values, suits, sortedOnIndex, _valueMethodCustomizer

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
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is a straight flush and false if 
    it is not. The second value in the list will be the value of 
    the high card in the straight flush, or None if the Hand is 
    not a straight flush.
    """
    # royal flush trumps straight flush
    if isRoyalFlush(hand) == True:
        return [False, None]

    handvalues = sortedOnIndex(hand.getValues(), values)
    handsuits = hand.getSuits(distinctsuits=True)
    straightflush = []

    # flush logic - there should only be 1 suit in the hand
    if len(handsuits) == 1:
        straightflush = [True, handvalues[-1]]  # straightflush only gets returned if the hand is also a straight
    else:
        return [False, None]

    # straight logic - break out of the loop if a straight is found and return straightflush
    for s in range(len(values)-len(handvalues)+1):
        st = values[s:s+len(handvalues)]
        if st == handvalues:
            return straightflush    # the hand is indeed both a straight and a flush so return straightflush
    else:   # if the loop completes then a straight was not found so return [False, None]
        return [False, None]

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
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is a flush and false if it is 
    not. The second value in the list will be the value of the 
    high card in the flush, or None if the Hand is not a flush.
    """
    # royal flush and straight flush trumps flush
    if isRoyalFlush(hand) == True or isStraightFlush(hand)[0] == True:
        return [False, None]

    handvalues = sortedOnIndex(hand.getValues(), values)
    handsuits = hand.getSuits(distinctsuits=True)
    if len(handsuits) == 1:
        return [True, handvalues[-1]]
    else:
        return [False, None]

def isStraight(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is a straight and false if it is
    not. The second value in the list will be the high card in the
    straight, or None if the Hand is not a straight.
    """
    # royal flush and straight flush trumps straight
    if isRoyalFlush(hand) == True or isStraightFlush(hand)[0] == True:
        return [False, None]

    handvalues = sortedOnIndex(hand.getValues(), values)
    straight = []
    # take a slice of the list the same length as the Hand and see if the values match
    for s in range(len(values)-len(handvalues)+1):
        straight = values[s:s+len(handvalues)]
        if straight == handvalues:
            return [True, straight[-1]]
    else:
        return [False, None]

def isThreeOfAKind(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is three of a kind and false if 
    it is not. The second value in the list will be the value of
    the three of a kind, or None if the Hand is not three of a kind.
    """
    # full house trumps three of a kind, so if the hand is a full house then this function should not continue to run
    if isFullHouse(hand)[0] == True:
        return [False, None]

    threeofakind = countOfValues(hand)
    return _valueMethodCustomizer(threeofakind, '<', 3, 3)

def isTwoPairs(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is two pairs and false if it is 
    not. The second value in the list will be a list containing the 
    values of the two pairs, or None if the Hand is not two pairs.
    """
    # flush trumps two pairs, so if the hand is a flush then this function should not continue to run
    if isFlush(hand)[0] == True:
        return [False, None]
    
    twopairs = countOfValues(hand)
    return _valueMethodCustomizer(twopairs, '!=', 3, 2, appendon=True)

class Card:
    """
    Represents a playing card in a card game.

    Attributes:
    
    value
        Holds the value of the card. 
        Available values: '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'

    suit
        Holds the suit of the card. 
        Available values: 'C', 'D', 'H', 'S'

    suitRank
        When True, all relational operators will consider both values and suits in comparisons.
        When False, all relational operators will consider only values in comparisons.
        Defaults to False. 'suitRank=True' still needs implementation.
    """
    def __init__(self, value, suit, suitRank=False):
        self.value = str(value).upper()
        self.suit = suit.upper()
        self.suitRank = suitRank
    def getValue(self):
        """Returns the value of 'value'."""
        return self.value
    def getSuit(self):
        """Returns the value of 'suit'."""
        return self.suit
    def getSuitRank(self):
        """Returns the value of 'suitRank'."""
        return self.suitRank
    def __eq__(self, other):
        """
        self == other
        
        Returns true if the Cards are equal.
        """
        if self.suitRank == False:
            return values.index(self.value) == values.index(other.value)
        else:
            pass
    def __ne__(self, other):
        """
        self != other
        
        Returns true if the Cards are not equal.
        """
        if self.suitRank == False:
            return values.index(self.value) != values.index(other.value)
        else:
            pass
    def __gt__(self, other):
        """
        self > other
        
        Returns true if the Card 'self' is greater than Card 'other'.
        """
        if self.suitRank == False:
            return values.index(self.value) > values.index(other.value)
        else:
            pass
    def __ge__(self, other):
        """
        self >= other
        
        Returns true if the Card 'self' is greater than or equal to Card 'other'.
        """
        if self.suitRank == False:
            return values.index(self.value) >= values.index(other.value)
        else:
            pass
    def __lt__(self, other):
        """
        self < other
        
        Returns true if the Card 'self' is less than Card 'other'.
        """
        if self.suitRank == False:
            return values.index(self.value) < values.index(other.value)
        else:
            pass
    def __le__(self, other):
        """
        self <= other
        
        Returns true if the Card 'self' is less than or equal to Card 'other'.
        """
        if self.suitRank == False:
            return values.index(self.value) <= values.index(other.value)
        else:
            pass
    def __repr__(self):
        return "%s('%s', '%s')" % (self.__class__.__name__, self.value, self.suit)
    def __str__(self):
        return "%s: value = '%s', suit = '%s'" % (self.__class__.__name__, self.value, suits.get(self.suit))

class Hand:
    """
    This class takes 5 instances of class Card as arguments.

    Attributes:
    -- card1 (instance of class Card)
    -- card2 (instance of class Card)
    -- card3 (instance of class Card)
    -- card4 (instance of class Card)
    -- card5 (instance of class Card)
    -- hand (list of 5 Card instances above)
    -- sort (method for sorting Hand in place)
    """
    def __init__(self, card1, card2, card3, card4, card5):
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.card4 = card4
        self.card5 = card5
        self.hand = [card1, card2, card3, card4, card5]
    def sort(self):
        """
        Sorts the Hand in place in ascending order and return None.
        """
        hand = self.hand[:]
        n = len(hand)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if hand[j] > hand[j+1]:
                    hand[j], hand[j+1] = hand[j+1], hand[j]
        self.card1, self.card2, self.card3, self.card4, self.card5 = hand[0], hand[1], hand[2], hand[3], hand[4]
    def getValues(self, *, distinctvalues=False):
        """
        Returns the values of all Cards in the Hand.
        """
        v = []
        if distinctvalues == True:
            for c in self.hand:
                val = c.getValue()
                if val not in v:
                    v.append(val)
        else:
            for c in self.hand:
                v.append(c.getValue())
        return v
    def getSuits(self, *, distinctsuits=False):
        """
        Returns the suits of all Cards in the Hand.
        """
        s = []
        if distinctsuits == True:
            for c in self.hand:
                val = c.getSuit()
                if val not in s:
                    s.append(val)
        else:
            for c in self.hand:
                s.append(c.getSuit())
        return s
    def __getitem__(self, index):
        """Fetches the Card at the given index."""
        return self.hand[index]
    def __len__(self):
        """Returns the length of 'self.hand'."""
        return len(self.hand)
    def __iter__(self):
        """Returns an instance of iterator class 'hand_iterator'."""
        return hand_iterator(self.hand)
    def __repr__(self):
        return '%s(%s, %s, %s, %s, %s)' % (self.__class__.__name__,  repr(self.card1), repr(self.card2), repr(self.card3), repr(self.card4), repr(self.card5))
    def __str__(self):
        return '%s:\ncard1 = [%s],\ncard2 = [%s],\ncard3 = [%s],\ncard4 = [%s],\ncard5 = [%s]' % (self.__class__.__name__,self.card1, self.card2, self.card3, self.card4, self.card5)

class hand_iterator:
    """
    Iterator returned for the Hand iterable class.
    """
    def __init__(self, hand):
        self.hand = hand
        self.counter = 0
    def __next__(self):
        """
        Returns the next Card in the Hand until the Hand is empty.
        """
        if self.counter == len(self.hand):
            raise StopIteration
        n = self.hand[self.counter]
        self.counter += 1
        return n

class Deck:
    pass

if __name__ == '__main__':
    a = Card('6', 's')
    b = Card('6', 'd')
    c = Card('6', 'c')
    d = Card('8', 'd')
    e = Card('8', 'c')
    h = Hand(a, b, c, d, e)
    l = [isRoyalFlush, isStraightFlush, isFourOfAKind, isFullHouse, isFlush, isStraight, isThreeOfAKind, isTwoPairs]
    print('%s : %s' % ('~~~Hand type'.ljust(15, '~'), '~~~Result'.ljust(13, '~')))
    for func in l:
        print("%s : %s" % (func.__name__.ljust(15), func(h)))
    #print(isTwoPairs(h))