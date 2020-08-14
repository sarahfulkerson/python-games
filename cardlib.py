#! /usr/bin/env python3
# https://projecteuler.net/problem=54

# TODO: abstract base classes!
from collections.abc import MutableSequence
from pokerlib import countOfValues, isHighCard, isOnePair, isTwoPairs, isThreeOfAKind, isStraight, isFlush, isFullHouse, isFourOfAKind, isStraightFlush, isRoyalFlush, handrankfuncs
from utillib import values, suits, sortedOnIndex

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
    def getHighCard(self):
        handvalues = sortedOnIndex(self.getValues(), values)
        return handvalues[-1]
    def __getitem__(self, key):
        """Fetches the Card at the given index."""
        return self.hand[key]
    def __setitem__(self, key, value):
        #TODO
        pass
    def __delitem__(self, key):
        #TODO
        pass
    def __contains__(self, key):
        #
        pass
    def __add__(self, value):
        #TODO
        pass
    def __iadd__(self, value):
        #TODO
        pass
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
    # [Card(x,y) for x in suits for y in values]
    pass

if __name__ == '__main__':
    a = Card('a', 'd')
    b = Card('k', 'd')
    c = Card('q', 'd')
    d = Card('j', 'd')
    e = Card('t', 'd')
    h = Hand(a, b, c, d, e)
    print('%s : %s' % ('~~~Hand type'.ljust(15, '~'), '~~~Result'.ljust(13, '~')))
    for func in handrankfuncs:
        print("%s : %s" % (func.__name__.ljust(15), func(h)))
    print(h.getHighCard())