#! /usr/bin/env python3
# https://projecteuler.net/problem=54

from utillib import values, suits

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
        if isinstance(other, Card):
            if self.suitRank == False:
                return values.index(self.value) == values.index(other.value)
            else:
                pass
        return False

    def __ne__(self, other):
        """
        self != other
        
        Returns true if the Cards are not equal.
        """
        if isinstance(other, Card):
            if self.suitRank == False:
                return values.index(self.value) != values.index(other.value)
            else:
                pass
        return False
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

class Hand(list):
    """
    This class extends the 'list' built-in type and adds methods for processing
    instances of class Card.
    """
    def __init__(self, *pargs):
        list.__init__([])
        self.extend([*pargs])
    def getValues(self, *, distinctvalues=False):
        """
        Returns the values of all Cards in the Hand.
        """
        v = []
        if distinctvalues == True:
            for c in self:
                val = c.getValue()
                if val not in v:
                    v.append(val)
        else:
            for c in self:
                v.append(c.getValue())
        return v
    def getSuits(self, *, distinctsuits=False):
        """
        Returns the suits of all Cards in the Hand.
        """
        s = []
        if distinctsuits == True:
            for c in self:
                val = c.getSuit()
                if val not in s:
                    s.append(val)
        else:
            for c in self:
                s.append(c.getSuit())
        return s
    def getHighCard(self):
        hand = sorted(self)
        return hand[-1]
    def __str__(self):
        result = "%s:\n" % self.__class__.__name__
        pos = 1
        for c in self:
            result = '%s%s\t%s\n' % (result, pos, str(c))
            pos += 1

        return result
    def __repr__(self):
        result = self.__class__.__name__
        tup = tuple()

        for c in self:
             tup += (c,)
        
        if len(tup) == 1:
            result = result + repr(tup)[:-2] + ')'
        else:
            result = result + repr(tup)
        
        return result

class Deck:
    # [Card(x,y) for x in suits for y in values]
    pass

if __name__ == '__main__':
    from pokerlib import handrankfuncs
    a = Card('a', 'd')
    b = Card('k', 'd')
    c = Card('q', 'd')
    d = Card('j', 'd')
    e = Card('t', 'd')
    h = Hand(a,b,c,d,e)
    print('%s : %s' % ('~~~Hand type'.ljust(15, '~'), '~~~Result'.ljust(13, '~')))
    for func in handrankfuncs:
        print("%s : %s" % (func.__name__.ljust(15), func(h)))
    print('High card: %s' % h.getHighCard())
    